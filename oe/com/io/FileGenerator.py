from abc import ABC, abstractmethod


class FileGenerator(ABC):

    @abstractmethod
    def create_file(self, name: str, data):
        pass
