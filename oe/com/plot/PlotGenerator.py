import matplotlib.pyplot as plt
import statistics


class PlotGenerator:
    pass

    @staticmethod
    def create_plot(title: str, x_label: str, y_label: str, x_data: list, y_data: list):
        fig = plt.figure()
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.plot(x_data, y_data)
        return fig
