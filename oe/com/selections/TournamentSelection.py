import random

from oe.com.selections.Selection import Selection


class TournamentSelection(Selection):

    def __init__(self, k: int):
        self.__number_of_groups = k

    def select_parents(self, population: list, values: list) -> list:
        # winners of the tournament
        selected_parents = []
        # indexes that will be chosen to certain groups
        indexes = [i for i in range(len(population))]
        group_sizes = [len(population) // self.__number_of_groups for _ in range(self.__number_of_groups)]

        # if there is not perfect division some groups need to be bigger
        if len(population) % self.__number_of_groups != 0:
            remainder = len(population) % self.__number_of_groups
            i = 0
            while remainder > 0:
                group_sizes[i] += 1
                remainder -= 1
                i += 1

        for i in range(self.__number_of_groups):
            best_index = random.choice(indexes)
            indexes.remove(best_index)
            for j in range(group_sizes[i] - 1):
                index = random.choice(indexes)
                if values[best_index] > values[index]:
                    best_index = index
                indexes.remove(index)
            selected_parents.append(population[best_index])

        return selected_parents
