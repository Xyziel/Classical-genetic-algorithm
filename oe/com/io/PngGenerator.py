from oe.com.io.FileGenerator import FileGenerator
import matplotlib.figure
import matplotlib.pyplot as plt


class PngGenerator(FileGenerator):

    def __init__(self, directory):
        self.__directory = directory

    def create_file(self, name: str, data):
        plt.figure(data.number)
        plt.savefig(self.__directory + name)




