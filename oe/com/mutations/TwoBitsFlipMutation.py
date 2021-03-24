import random

from oe.com.models import Population
from oe.com.mutations.Mutation import Mutation


class TwoBitsFlipMutation(Mutation):

    def mutate(self, population: Population):
        for chromosomes in population.get_population():
            if random.uniform(0, 1) <= self.mutate_probability:
                for j in range(population.get_number_of_variables()):
                    bit1_index = random.randint(0, population.get_number_of_bits() - 1)

                    # while loop to make sure that both indexes are different
                    while True:
                        bit2_index = random.randint(0, population.get_number_of_bits() - 1)
                        if bit2_index != bit1_index:
                            break

                    chrom_bits = chromosomes[j].get_bits_array()
                    if chrom_bits[bit1_index] == 0:
                        chrom_bits[bit1_index] = 1
                    else:
                        chrom_bits[bit1_index] = 0

                    if chrom_bits[bit2_index] == 0:
                        chrom_bits[bit2_index] = 1
                    else:
                        chrom_bits[bit2_index] = 0
