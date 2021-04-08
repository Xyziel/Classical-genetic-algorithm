from oe.com.io.FileGenerator import FileGenerator


class TxtGenerator(FileGenerator):

    def __init__(self, directory):
        self.__directory = directory

    def create_file(self, name: str, data: list):
        file = open(self.__directory + name, "w")
        [file.write(f"{i + 1} {str(data[i])}\n") for i in range(len(data))]
        file.close()
