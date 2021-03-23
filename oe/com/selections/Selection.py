from abc import ABC, abstractmethod


class Selection(ABC):

    @abstractmethod
    def select_parents(self, population: list, values: list) -> list:
        pass
