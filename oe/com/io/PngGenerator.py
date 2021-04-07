from oe.com.io.FileGenerator import FileGenerator
import matplotlib.figure
import matplotlib.pyplot as plt


class PngGenerator(FileGenerator):

    def __init__(self, directory):
        self.__directory = directory

    def create_file(self, name: str, data: list):
        pass
        # file = open(self.values_directory + name, "w")
        # print(len(data))
        # [file.write(f"{i + 1} {str(data[i])}\n") for i in range(len(data))]
        # file.close()

    def create_file_from_figure(self, name: str, figure: matplotlib.figure):
        plt.figure(figure.number)
        plt.savefig(self.__directory + name)


