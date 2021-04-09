import random

from oe.com.models import Population
from oe.com.mutations.Mutation import Mutation


class EdgeBitFlipMutation(Mutation):

    def mutate(self, population: Population):
        for chromosomes in population.get_population():
            if random.uniform(0, 1) <= self.mutate_probability:
                for j in range(population.get_number_of_variables()):
                    if random.uniform(0, 1) <= 0.5:
                        bit_edge_index = population.get_number_of_bits() - 1
                    else:
                        bit_edge_index = 0
                    chrom_bits = chromosomes[j].get_bits_array()
                    if chrom_bits[bit_edge_index] == 0:
                        chrom_bits[bit_edge_index] = 1
                    else:
                        chrom_bits[bit_edge_index] = 0

