import random

from oe.com.crossovers.Crossover import Crossover
from oe.com.models import Population, Chromosome


class OnePointCrossover(Crossover):

    def cross(self, parents: Population, new_gen_size: int) -> Population:
        new_gen = Population()
        crosspoints = []
        while new_gen.get_size() < new_gen_size:
            if random.uniform(0, 1) <= self.cross_probability:

                # choose random cross points for every variable
                for i in range(parents.get_number_of_variables()):
                    crosspoints.append(random.randint(2, parents.get_number_of_bits() - 2))

                tmp_parents = parents.get_population().copy()
                parent1 = random.choice(tmp_parents)
                # remove parent1 from the list so it cannot be chosen
                tmp_parents.remove(parent1)
                parent2 = random.choice(tmp_parents)
                chrom_bits_p1_x1 = parent1[0].get_bits_array()
                #print(parent1)
                #print(parent2)
                parent1_bits = [parent1[i].get_bits_array() for i in range(parents.get_number_of_variables())]
                parent2_bits = [parent2[i].get_bits_array() for i in range(parents.get_number_of_variables())]
                #print(parent1_bits)
                #print(parent2_bits)
                #print(crosspoints)
                child_bits = [parent1_bits[i][0:crosspoints[i]] + parent2_bits[i][crosspoints[i]:] for i in range(parents.get_number_of_variables())]
                #print(child_bits)
                child = [Chromosome(child_bits[i]) for i in range(parents.get_number_of_variables())]
                #print(child)
                #print(child[0].get_bits_array(), child[1].get_bits_array())
                new_gen.add_chromosomes(child)
        return new_gen

    #
    # def crossover(parents):
    #     #one-point crossover
    #     index1 = random.randint(2, 22)
    #     index2 = random.randint(2, 22)
    #     new_gen = Population()
    #     while new_gen.get_size() < 100:
    #         if random.uniform(0, 1) < 0.85:
    #             tmp = parents.copy()
    #             parent1 = random.choice(tmp)
    #             tmp.remove(parent1)
    #             parent2 = random.choice(tmp)
    #             #print(parent2, parent1)
    #             child = [parent1[0][0:index1] + parent2[0][index1:], parent1[1][0:index2] + parent2[1][index2:]]
    #             new_gen.append(child)
    #     return new_gen