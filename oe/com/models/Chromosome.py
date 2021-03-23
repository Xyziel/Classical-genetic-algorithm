import random


class Chromosome:

    def __init__(self, number_of_bits: int):
        self.__bits_array = [random.randint(0, 1) for _ in range(number_of_bits)]

    def get_bits_array(self) -> list:
        return self.__bits_array


