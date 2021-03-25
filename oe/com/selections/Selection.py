from abc import ABC, abstractmethod

from oe.com.models import Population


class Selection(ABC):

    @abstractmethod
    def select_parents(self, population: Population, values: list, maximum: bool) -> Population:
        pass
