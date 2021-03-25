import random

from oe.com.crossovers.Crossover import Crossover
from oe.com.models import Population, Chromosome


class OnePointCrossover(Crossover):

    def cross(self, parents: Population, new_gen_size: int) -> Population:
        new_gen = Population()
        cross_points = []
        while new_gen.get_size() < new_gen_size:
            if random.uniform(0, 1) <= self.cross_probability:

                # draw random cross point for every variable
                for i in range(parents.get_number_of_variables()):
                    cross_points.append(random.randint(2, parents.get_number_of_bits() - 2))

                tmp_parents = parents.get_population().copy()
                parent1 = random.choice(tmp_parents)
                # remove parent1 from the list so it cannot be chosen
                tmp_parents.remove(parent1)
                parent2 = random.choice(tmp_parents)

                parent1_bits = [parent1[i].get_bits_array() for i in range(parents.get_number_of_variables())]
                parent2_bits = [parent2[i].get_bits_array() for i in range(parents.get_number_of_variables())]

                # first child
                child1_bits = [parent1_bits[i][0:cross_points[i]] + parent2_bits[i][cross_points[i]:]
                               for i in range(parents.get_number_of_variables())]
                child = [Chromosome(child1_bits[i]) for i in range(parents.get_number_of_variables())]
                new_gen.add_chromosomes(child)

                # second child
                child2_bits = [parent2_bits[i][0:cross_points[i]] + parent1_bits[i][cross_points[i]:]
                               for i in range(parents.get_number_of_variables())]
                child = [Chromosome(child2_bits[i]) for i in range(parents.get_number_of_variables())]
                new_gen.add_chromosomes(child)

        # if elite strategy makes new population too long the last element needs to be deleted
        if new_gen.get_size() > new_gen_size:
            new_gen.delete_chromosomes_index(new_gen.get_size() - 1)

        return new_gen
