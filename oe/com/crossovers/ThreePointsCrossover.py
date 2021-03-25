import random

from oe.com.crossovers.Crossover import Crossover
from oe.com.models import Population, Chromosome


class ThreePointsCrossover(Crossover):

    def cross(self, parents: Population, new_gen_size: int) -> Population:
        new_gen = Population()
        while new_gen.get_size() < new_gen_size:
            if random.uniform(0, 1) <= self.cross_probability:

                # draw first random cross point for every variable
                cross_points = [[random.randint(0, parents.get_number_of_bits() - 1)] for _ in
                                range(parents.get_number_of_variables())]

                # draw second and third different from each other and the first
                for i in range(parents.get_number_of_variables()):
                    while True:
                        cross_points[i].append(random.randint(0, parents.get_number_of_bits() - 1))
                        cross_points[i].append(random.randint(0, parents.get_number_of_bits() - 1))
                        if cross_points[i][0] != cross_points[i][1] and cross_points[i][1] != cross_points[i][2] and \
                                cross_points[i][0] != cross_points[i][2]:
                            break
                        else:
                            cross_points[i].pop(1)
                            cross_points[i].pop(1)

                for i in range(parents.get_number_of_variables()):
                    cross_points[i].sort()

                tmp_parents = parents.get_population().copy()
                parent1 = random.choice(tmp_parents)
                # remove parent1 from the list so it cannot be chosen
                tmp_parents.remove(parent1)
                parent2 = random.choice(tmp_parents)

                parent1_bits = [parent1[i].get_bits_array() for i in range(parents.get_number_of_variables())]
                parent2_bits = [parent2[i].get_bits_array() for i in range(parents.get_number_of_variables())]

                # choosing the lower or upper interval
                if random.randint(0, 1) == 0:
                    # lower interval
                    child1_bits = [
                        parent2_bits[i][0:cross_points[i][0]] + parent1_bits[i][cross_points[i][0]:cross_points[i][1]] +
                        parent2_bits[i][cross_points[i][1]: cross_points[i][2]] + parent1_bits[i][cross_points[i][2]:]
                        for i in range(parents.get_number_of_variables())]
                    child2_bits = [
                        parent1_bits[i][0:cross_points[i][0]] + parent2_bits[i][cross_points[i][0]:cross_points[i][1]] +
                        parent1_bits[i][cross_points[i][1]: cross_points[i][2]] + parent2_bits[i][cross_points[i][2]:]
                        for i in range(parents.get_number_of_variables())]
                else:
                    # upper interval
                    child1_bits = [
                        parent1_bits[i][0:cross_points[i][0]] + parent2_bits[i][cross_points[i][0]:cross_points[i][1]] +
                        parent1_bits[i][cross_points[i][1]: cross_points[i][2]] + parent2_bits[i][cross_points[i][2]:]
                        for i in range(parents.get_number_of_variables())]
                    child2_bits = [
                        parent2_bits[i][0:cross_points[i][0]] + parent1_bits[i][cross_points[i][0]:cross_points[i][1]] +
                        parent2_bits[i][cross_points[i][1]: cross_points[i][2]] + parent1_bits[i][cross_points[i][2]:]
                        for i in range(parents.get_number_of_variables())]

                child = [Chromosome(child1_bits[i]) for i in range(parents.get_number_of_variables())]
                new_gen.add_chromosomes(child)

                child = [Chromosome(child2_bits[i]) for i in range(parents.get_number_of_variables())]
                new_gen.add_chromosomes(child)

        # if elite strategy makes new population too long the last element needs to be deleted
        if new_gen.get_size() > new_gen_size:
            new_gen.delete_chromosomes_index(new_gen.get_size() - 1)

        return new_gen
