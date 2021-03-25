from oe.com.models import Population


class ElitismStrategy:

    def __init__(self, n: int):
        self.__n = n

    def choose_n_best(self, population: Population, values: list, maximum: bool) -> Population:
        i = 0
        selected_parents = Population()
        value_map = {}
        values_copy = values.copy()
        for chromosomes in population.get_population():
            value_map[values_copy[i]] = chromosomes
            i += 1
        if maximum:
            values_copy.sort(reverse=True)
        else:
            values_copy.sort()
        for i in range(self.__n):
            chroms = value_map[values_copy[i]]
            selected_parents.add_chromosomes(chroms)
        return selected_parents
