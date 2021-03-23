class MyFunction:

    def __init__(self, f):
        self.__f = f

    def get_values_population_dec(self, population_decimal: list) -> list:
        return [self.__f(population_decimal[i]) for i in range(len(population_decimal))]
