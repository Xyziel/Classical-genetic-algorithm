from oe.com.models import Population
from oe.com.selections.Selection import Selection


class TheBestOnesSelection(Selection):

    def __init__(self, percentage):
        self.__percentage = percentage

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
        number_of_selecting_parents = round(population.get_size() * self.__percentage)
        for i in range(number_of_selecting_parents):
            chroms = value_map[values[i]]
            selected_parents.add_chromosomes(chroms)
        return selected_parents
