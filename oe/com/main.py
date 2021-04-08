from oe.com.gui.Application import Application
from oe.com.GeneticAlgorithm import GeneticAlgorithm

import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Genetic Algorithms")
    root.config(bg='#ccc')
    app = Application(master=root)
    app.start_button.config(command=lambda: GeneticAlgorithm(app))
    app.mainloop()


if __name__ == '__main__':
    main()
