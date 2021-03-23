from oe.com.models.Chromosome import Chromosome


class Population:

    def __init__(self, size: int, number_of_variables: int, number_of_bits: int):
        self.__size = size
        self.__number_of_variables = number_of_variables
        self.__number_of_bits = number_of_bits
        self.__population = [[Chromosome(number_of_bits) for _ in range(number_of_variables)] for _ in range(size)]

    def get_population(self) -> list:
        return self.__population

    def get_population_bits(self) -> list:
        return [[self.__population[i][j].get_bits_array() for j in range(self.__number_of_variables)]
                for i in range(self.__size)]

    def get_population_decimal(self, a: float, b: float) -> list:
        return [[a + self.__decimal(self.__population[i][n]) * (b - a) / (2 ** self.__number_of_bits - 1)
                 for n in range(self.__number_of_variables)] for i in range(self.__size)]

    def __decimal(self, chromosome: Chromosome):
        bits_array = chromosome.get_bits_array()
        list_to_str = ''.join([str(elem) for elem in bits_array])
        return int(list_to_str, 2)
