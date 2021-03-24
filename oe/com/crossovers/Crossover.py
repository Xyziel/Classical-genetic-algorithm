from abc import ABC, abstractmethod

from oe.com.models import Population


class Crossover(ABC):

    def __init__(self, cross_probability):
        self.cross_probability = cross_probability

    @abstractmethod
    def cross(self, parents: Population, new_gen_size: int) -> Population:
        pass

