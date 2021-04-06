from oe.com.models import Population
from oe.com.selections.Selection import Selection


class TheBestOnesSelection(Selection):

    def __init__(self, number):
        self.__number = number

    def select_parents(self, population: Population, values: list, maximum: bool) -> Population:
        i = 0
        selected_parents = Population()
        value_map = {}
        for chromosomes in population.get_population():
            value_map[values[i]] = chromosomes
            i += 1
        if maximum:
            values.sort(reverse=True)
        else:
            values.sort()
        for i in range(self.__number):
            chroms = value_map[values[i]]
            selected_parents.add_chromosomes(chroms)
        return selected_parents
