import random

from oe.com.models import Population
from oe.com.selections.Selection import Selection


class RouletteWheelSelection(Selection):

    def __init__(self, percentage):
        self.__percentage = percentage

    def select_parents(self, population: Population, values: list, maximum: bool) -> Population:
        selected_parents = Population()

        if maximum:
            sum_of_values = sum(values)
            probabilities = [(values[i]) / sum_of_values for i in range(len(values))]
        else:
            sum_of_values = sum([1 / x for x in values])
            probabilities = [(1 / values[i]) / sum_of_values for i in range(len(values))]
        # number_of_parents = round(population.get_size() * self.__percentage)
        number_of_parents = 2
        distribution = []
        sum_dist = 0
        for x in probabilities:
            sum_dist += x
            distribution.append(sum_dist)

        for i in range(number_of_parents):
            random_value = random.uniform(0, 1)
            for j in range(population.get_size()):
                if random_value <= distribution[j]:
                    selected_parents.add_chromosomes(population.get_population()[j])
                    break

        return selected_parents
