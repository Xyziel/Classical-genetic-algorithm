from abc import ABC, abstractmethod


class Mutation(ABC):

    def __init__(self, mutate_probability: float):
        self.mutate_probability = mutate_probability

    @abstractmethod
    def mutate(self, population: list):
        pass

