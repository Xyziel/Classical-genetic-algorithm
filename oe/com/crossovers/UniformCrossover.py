import random

from oe.com.crossovers.Crossover import Crossover
from oe.com.models import Population, Chromosome


class UniformCrossover(Crossover):

    def cross(self, parents: Population, new_gen_size: int) -> Population:
        new_gen = Population()
        while new_gen.get_size() < new_gen_size:
            if random.uniform(0, 1) <= self.cross_probability:
                tmp_parents = parents.get_population().copy()
                parent1 = random.choice(tmp_parents)
                # remove parent1 from the list so it cannot be chosen
                tmp_parents.remove(parent1)
                parent2 = random.choice(tmp_parents)

                parent1_bits = [parent1[i].get_bits_array() for i in range(parents.get_number_of_variables())]
                parent2_bits = [parent2[i].get_bits_array() for i in range(parents.get_number_of_variables())]

                child1_bits = []
                child2_bits = []
                for i in range(parents.get_number_of_variables()):
                    # single variable from each child
                    variable_child1 = []
                    variable_child2 = []
                    for j in range(parents.get_number_of_bits()):
                        if random.randint(0, 1) == 0:
                            variable_child1.append(parent1_bits[i][j])
                            variable_child2.append(parent2_bits[i][j])
                        else:
                            variable_child1.append(parent2_bits[i][j])
                            variable_child2.append(parent1_bits[i][j])
                    child1_bits.append(variable_child1)
                    child2_bits.append(variable_child2)

                # add child 1
                child = [Chromosome(child1_bits[i]) for i in range(parents.get_number_of_variables())]
                new_gen.add_chromosomes(child)

                # add child 2
                child = [Chromosome(child2_bits[i]) for i in range(parents.get_number_of_variables())]
                new_gen.add_chromosomes(child)

        # if elite strategy makes new population too long the last element needs to be deleted
        if new_gen.get_size() > new_gen_size:
            new_gen.delete_chromosomes_index(new_gen.get_size() - 1)

        return new_gen
