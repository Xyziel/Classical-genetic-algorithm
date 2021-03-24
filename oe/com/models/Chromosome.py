import random


class Chromosome:

    def __init__(self, *args):
        if type(args[0]) is int:
            number_of_bits = args[0]
            self.__bits_array = [random.randint(0, 1) for _ in range(number_of_bits)]
        if type(args[0]) is list:
            self.__bits_array = args[0]

    def get_bits_array(self) -> list:
        return self.__bits_array

    def get_number_of_bits(self) -> int:
        return len(self.__bits_array)



