import random

from oe.com.models import Population


class Inversion:

    def __init__(self, invert_probability: float):
        self.invert_probability = invert_probability

    def invert(self, population: Population):
        for chromosomes in population.get_population():
            if random.uniform(0, 1) <= self.invert_probability:
                for j in range(population.get_number_of_variables()):
                    bit1_index = random.randint(0, population.get_number_of_bits() - 1)

                    # while loop to make sure that both indexes are different
                    while True:
                        bit2_index = random.randint(0, population.get_number_of_bits() - 1)
                        if bit2_index != bit1_index:
                            break

                    if bit2_index < bit1_index:
                        tmp = bit2_index
                        bit2_index = bit1_index
                        bit1_index = tmp

                    chrom_bits = chromosomes[j].get_bits_array()

                    for i in range((bit2_index + 1 - bit1_index) // 2):
                        tmp = chrom_bits[bit1_index + i]
                        chrom_bits[bit1_index + i] = chrom_bits[bit2_index - i]
                        chrom_bits[bit2_index - i] = tmp
