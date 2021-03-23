from abc import ABC, abstractmethod


class Crossover(ABC):

    def __init__(self, cross_probability):
        self.cross_probability = cross_probability

    @abstractmethod
    def cross(self, parents):
        pass

