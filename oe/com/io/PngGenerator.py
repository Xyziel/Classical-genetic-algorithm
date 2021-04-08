from oe.com.io.FileGenerator import FileGenerator
import matplotlib.figure
import matplotlib.pyplot as plt


class PngGenerator(FileGenerator):

    def __init__(self, directory):
        self.__directory = directory

    def create_file(self, name: str, data: list):
        pass

    def create_file_from_figure(self, name: str, figure: matplotlib.figure):
        plt.figure(figure.number)
        plt.savefig(self.__directory + name)


