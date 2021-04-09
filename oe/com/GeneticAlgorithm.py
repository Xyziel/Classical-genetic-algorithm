from oe.com.gui.Application import Application
from oe.com.models import *
from oe.com.mutations import *
from oe.com.selections import *
from oe.com.elite import *
from oe.com.io import *
from oe.com.plot import *

import time
import statistics
import os


class GeneticAlgorithm:

    def __init__(self, app: Application):
        self.__app = app
        self.__values = app.get_all_values()
        self.__a = self.__values['beginning']
        self.__b = self.__values['end']
        self.__bits = self.__values['bits']
        self.__size = self.__values['population']
        self.__epochs = self.__values['epochs']
        self.__cross_prob = self.__values['cross_prob']
        self.__mutate_prob = self.__values['mutation_prob']
        self.__invert_prob = self.__values['inversion_prob']
        self.__elite_number = self.__values['elite']
        self.__maximization = self.__values['max']
        self.__calculate()

    def __calculate(self):
        selection = self.__create_instance_using_str("selection", "Selection", self.__values['k'])
        crossover = self.__create_instance_using_str("crossover", "Crossover", self.__cross_prob)
        mutation = self.__create_instance_using_str("mutation", "FlipMutation", self.__mutate_prob)

        inversion = Inversion(self.__invert_prob)
        elite = ElitismStrategy(self.__elite_number)
        maxi = self.__maximization == 1

        # starting timer
        start_timer = time.perf_counter()

        population = Population()
        population.create_random_population(self.__size, 2, self.__bits)
        fun = MyFunction(f)
        population_decimal = population.get_population_decimal(self.__a, self.__b)

        # values containers
        value_in_each_it = []
        std_values = []
        mean_values = []

        for i in range(self.__epochs):
            values = fun.get_values_population_dec(population_decimal)
            std_values.append(statistics.pstdev(values))
            mean_values.append(statistics.mean(values))
            elite_population = elite.choose_n_best(population, values, maxi)
            selected_parents = selection.select_parents(population, values, maxi)

            if isinstance(selection, RouletteWheelSelection):
                population = crossover.cross(selected_parents, 2)
                while population.get_size() < self.__size - self.__elite_number:
                    population += crossover.cross(selected_parents, 2)
                if population.get_size() > self.__size - self.__elite_number:
                    population.delete_chromosomes_index(population.get_size() - 1)
            else:
                population = crossover.cross(selected_parents, self.__size - self.__elite_number)

            mutation.mutate(population)
            inversion.invert(population)

            population + elite_population

            population_dec = population.get_population_decimal(self.__a, self.__b)

            population_decimal = population_dec

            if maxi:
                value_in_each_it.append(max(values))
            else:
                value_in_each_it.append(min(values))

        end_timer = time.perf_counter()

        self.__generate_txt_files([value_in_each_it, mean_values, std_values])
        self.__generate_png_files([value_in_each_it, mean_values, std_values])

        if maxi:
            # create_timer_window
            self.__app.create_timer_window(end_timer - start_timer, population_decimal[values.index(max(values))],
                                           max(values))

        else:
            # create_timer_window
            self.__app.create_timer_window(end_timer - start_timer, population_decimal[values.index(min(values))],
                                           min(values))




    def __create_instance_using_str(self, name, suffix, param):
        class_name = self.__values[name].replace(" ", "") + suffix
        obj = globals()[class_name](param)
        return obj

    def __generate_txt_files(self, data):
        txt_generator = TxtGenerator(os.getcwd() + "/oe/com/data/values/")
        txt_generator.create_file("Best values.txt", data[0])
        txt_generator.create_file("Mean values.txt", data[1])
        txt_generator.create_file("Standard deviation.txt", data[2])

    def __generate_png_files(self, data):
        file_names = ["Best values.jpg", "Mean values.jpg", "Standard deviation.jpg"]
        titles = ["Values for each iteration", "Mean values for each iteration",
                  "Standard deviation for each iteration"]
        iterations_list = [i + 1 for i in range(len(data[0]))]

        png_generator = PngGenerator(os.getcwd() + "/oe/com/data/plots/")

        for i in range(len(data)):
            png_generator.create_file(file_names[i],
                                      PlotGenerator.create_plot(titles[i], x_label="Iterations", y_label="Values",
                                                                x_data=iterations_list, y_data=data[i]))


def f(x):
    # return x[0] ** 2 + x[1] ** 2

    # bayes
    return (1.5 - x[0] + x[0] * x[1]) ** 2 + (2.25 - x[0] + x[0] * (x[1] ** 2)) ** 2 + (
            2.625 - x[0] + x[0] * (x[1] ** 3)) ** 2

    # ackley
    # a = 20.0
    # b = 0.2
    # c = 2 * 3.14
    # return ((-a * math.exp(-b * math.sqrt(sum([i ** 2 for i in x]) / len(x)))) - (
    #     math.exp(sum(math.cos(c * i) for i in x) / len(x))) +
    #         a + math.exp(1))