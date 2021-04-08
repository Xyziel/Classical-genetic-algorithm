from oe.com.gui.Application import Application
from oe.com.models import *
from oe.com.mutations import *
from oe.com.crossovers import *
from oe.com.selections import *
from oe.com.elite import *
from oe.com.io import *
from oe.com.plot import *

import tkinter as tk
import time
import statistics
import os
import matplotlib.pyplot as plt


def f(x):
    # return x[0] ** 2 + x[1] ** 2
    return (1.5 - x[0] + x[0]*x[1]) ** 2 + (2.25 - x[0] + x[0]*(x[1] ** 2)) ** 2 + (2.625 - x[0] + x[0]*(x[1] ** 3)) ** 2


def calculate(app):
    values = app.get_all_values()
    a = values['beginning']
    b = values['end']
    bits = values['bits']
    size = values['population']
    epochs = values['epochs']
    cross_prob = values['cross_prob']
    mutate_prob = values['mutation_prob']
    invert_prob = values['inversion_prob']
    elite_number = values['elite']
    maximization = values['max']
    if values['selection'] == 'Tournament':
        k = values['k']
        selection = TournamentSelection(k)
    elif values['selection'] == 'The Best Ones':
        k = values['k']
        selection = TheBestOnesSelection(k)
    else:
        selection = RouletteWheelSelection()

    if values['crossover'] == 'One Point':
        crossover = OnePointCrossover(cross_prob)
    elif values['crossover'] == 'Two Points':
        crossover = TwoPointsCrossover(cross_prob)
    elif values['crossover'] == 'Three Points':
        crossover = ThreePointsCrossover(cross_prob)
    else:
        crossover = UniformCrossover(cross_prob)

    if values['mutation'] == 'Edge Bit':
        mutation = EdgeBitFlipMutation(mutate_prob)
    elif values['mutation'] == 'One Bit':
        mutation = OneBitFlipMutation(mutate_prob)
    else:
        mutation = TwoBitsFlipMutation(mutate_prob)

    inversion = Inversion(invert_prob)
    elite = ElitismStrategy(elite_number)
    maxi = maximization == 1

    # start_timer
    start_timer = time.perf_counter()

    population = Population()
    population.create_random_population(size, 2, bits)
    fun = MyFunction(f)
    population_decimal = population.get_population_decimal(a, b)
    values = fun.get_values_population_dec(population_decimal)

    value_in_each_it = []

    # przygotowanie kontenerow do wykresow
    std_values = []
    mean_values = []

    for i in range(epochs):
        elite_population = elite.choose_n_best(population, values, maxi)
        selected_parents = selection.select_parents(population, values, maxi)
        if isinstance(selection, RouletteWheelSelection):
            population = crossover.cross(selected_parents, 2)
            while population.get_size() < size - elite_number:
                population += crossover.cross(selected_parents, 2)
            if population.get_size() > size - elite_number:
                population.delete_chromosomes_index(population.get_size() - 1)
        else:
            population = crossover.cross(selected_parents, size - elite_number)

        mutation.mutate(population)
        inversion.invert(population)

        population + elite_population

        population_dec = population.get_population_decimal(a, b)

        # przypisanie nowych wartosci na potrzeby create_timer_window
        population_decimal = population_dec

        values = fun.get_values_population_dec(population_dec)
        std_values.append(statistics.pstdev(values))
        mean_values.append(statistics.mean(values))

        if maxi:
            value_in_each_it.append(max(values))
        else:
            value_in_each_it.append(min(values))

    # end_timer
    end_timer = time.perf_counter()

    # generating txt values
    print(os.getcwd())
    txt_generator = TxtGenerator(os.getcwd() + "/data/values/")
    txt_generator.create_file("Standard deviation.txt", std_values)
    txt_generator.create_file("Mean values.txt", mean_values)
    txt_generator.create_file("Best values.txt", value_in_each_it)

    iterations_list = [i + 1 for i in range(len(value_in_each_it))]

    # generating plots
    png_generator = PngGenerator(os.getcwd() + "/data/plots/")
    png_generator.create_file("Best values.jpg",
                                          PlotGenerator.create_plot("Values for each iteration", x_label="Iterations",
                                                                    y_label="Values",
                                                                    x_data=iterations_list,
                                                                    y_data=value_in_each_it))
    png_generator.create_file("Standard deviation.jpg",
                                          PlotGenerator.create_plot("Standard deviation for each iteration",
                                                                    x_label="Iterations",
                                                                    y_label="Values",
                                                                    x_data=iterations_list,
                                                                    y_data=std_values))
    png_generator.create_file("Mean values.jpg",
                                          PlotGenerator.create_plot("Mean values for each iteration",
                                                                    x_label="Iterations",
                                                                    y_label="Values",
                                                                    x_data=iterations_list,
                                                                    y_data=mean_values))


    if maxi:
        print("Wartosc max (powinna byc bliska 200): " + str(max(values)))
        # create_timer_window
        app.create_timer_window(end_timer - start_timer, population_decimal[values.index(max(values))], max(values))

    else:
        print("Wartosc min (powinna byc bliska 0): " + str(min(values)))
        # create_timer_window
        app.create_timer_window(end_timer - start_timer, population_decimal[values.index(min(values))], min(values))

    print("Jak zmienialy sie wartosci")
    print(value_in_each_it)


def main():
    # # Przykladowe dane
    # a = -10  # poczatek przedzialu
    # b = 10  # koniec przedzialu
    # bits = 25  # liczba bitow genu # Pytanie czy moga byc bity czy ustawiac dokladnosc?
    # n = 2  # liczba zmiennych
    # size = 100  # rozmiar populacji
    # i = 10  # liczba iteracji
    # k = 5  # liczba grup turniejowych
    # cross_prob = 0.85  # prawdopodobienstwa krzyzowania
    # mutate_prob = 0.15  # prawd. mutacji
    # invert_prob = 0.15  # prawd. inwersji
    # population_percent = 0.1  # procent populacji w selekcji najlepszych oraz ruletce
    # maximum = False  # czy maksymalizacja
    # elite_number = 5  # liczba elitarnych osobnikow
    #
    # population = Population()
    # population.create_random_population(size, n, bits)
    # fun = MyFunction(f)
    # population_decimal = population.get_population_decimal(a, b)
    # values = fun.get_values_population_dec(population_decimal)
    #
    # selection = RouletteWheelSelection()
    # crossover = UniformCrossover(cross_prob)
    # mutation = EdgeBitFlipMutation(mutate_prob)
    # inversion = Inversion(invert_prob)
    # elite = ElitismStrategy(elite_number)
    #
    # value_in_each_it = []
    #
    # for i in range(i):
    #     elite_population = elite.choose_n_best(population, values, maximum)
    #     selected_parents = selection.select_parents(population, values, maximum)
    #     if isinstance(selection, RouletteWheelSelection):
    #         population = crossover.cross(selected_parents, 2)
    #         while population.get_size() < size - elite_number:
    #             population += crossover.cross(selected_parents, 2)
    #         if population.get_size() > size - elite_number:
    #             population.delete_chromosomes_index(population.get_size() - 1)
    #     else:
    #         population = crossover.cross(selected_parents, size - elite_number)
    #     mutation.mutate(population)
    #     inversion.invert(population)
    #
    #     population + elite_population
    #
    #     population_dec = population.get_population_decimal(a, b)
    #     values = fun.get_values_population_dec(population_dec)
    #
    #     if maximum:
    #         value_in_each_it.append(max(values))
    #     else:
    #         value_in_each_it.append(min(values))
    #
    # if maximum:
    #     print("Wartosc max (powinna byc bliska 200): " + str(max(values)))
    #
    # else:
    #     print("Wartosc min (powinna byc bliska 0): " + str(min(values)))
    # print("Jak zmienialy sie wartosci")
    # print(value_in_each_it)

    root = tk.Tk()
    root.title("Genetic Algorithms")
    root.config(bg='#ccc')
    app = Application(master=root)
    app.start_button.config(command=lambda: calculate(app))
    app.mainloop()


if __name__ == '__main__':
    main()
