import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.selection = tk.StringVar()
        self.selection_label = None
        self.selection_entry = None
        self.selection_entry_number = tk.IntVar()
        self.crossover = tk.StringVar()
        self.crossover_prob = tk.DoubleVar()
        self.mutation = tk.StringVar()
        self.mutation_prob = tk.DoubleVar()
        self.beginning_of_interval = tk.DoubleVar()
        self.end_of_interval = tk.DoubleVar()
        self.number_of_bits = tk.IntVar()
        self.population_size = tk.IntVar()
        self.number_of_epochs = tk.IntVar()
        self.elite_strategy_amount = tk.IntVar()
        self.inversion_prob = tk.DoubleVar()
        self.maximization = tk.IntVar()
        self.start_button = tk.Button()
        self.create_menu()

    def create_menu(self):
        tk.Label(self.master, text="Genetic Algorithms", font=('arial', 12, 'bold'), bg="#ccc").grid(row=0, columnspan=2, sticky='WE', pady=10)
        self.create_menu_left()
        self.create_menu_right()
        self.start_button = tk.Button(self.master, text='Start', width=20, font=('arial', 10, 'bold'), bg='#808080', fg='white')
        self.start_button.grid(row=2, columnspan=2, pady=10)

    def create_menu_left(self):

        frame = tk.Frame(self.master, relief='raised')
        frame.config(bg='#e3e3e3')
        frame.grid(row=1, column=0, padx=(20, 10), pady=10, sticky='N')

        self.create_label_with_entry(frame, 'Beginning of interval:', self.beginning_of_interval)
        self.create_label_with_entry(frame, 'End of internal:', self.end_of_interval)
        self.create_label_with_entry(frame, 'Number of bits:', self.number_of_bits)
        self.create_label_with_entry(frame, 'Population size:', self.population_size)
        self.create_label_with_entry(frame, 'Number of epochs:', self.number_of_epochs)
        self.create_label_with_entry(frame, 'Elite strategy amount:', self.elite_strategy_amount)
        tk.Checkbutton(frame, text='Maximization', variable=self.maximization, bg='#e3e3e3').grid(padx=20, pady=(10, 0), sticky='W')

    def create_label_with_entry(self, frame, title, data, label_pady=(10, 0), entry_pady=(0, 0)):
        label = tk.Label(frame, text=title, bg='#e3e3e3')
        label.grid(padx=20, pady=label_pady, sticky='W')
        entry = tk.Entry(frame, textvariable=data, width=25, bd=3)
        entry.grid(padx=24, pady=entry_pady, sticky='WE')
        return entry

    def create_menu_right(self):
        frame = tk.Frame(self.master, relief='raised')
        frame.config(bg='#e3e3e3')
        frame.grid(row=1, column=1, padx=(10, 20), pady=10, sticky='N')

        self.create_selections_menu(frame)
        self.create_crossovers_menu(frame)
        self.create_mutations_menu(frame)
        self.create_label_with_entry(frame, 'Inversion probability:', self.inversion_prob, entry_pady=(5, 10))

    def create_selections_menu(self, frame):
        selections_menu_label = tk.Label(frame, text="Choose selection option:", bg='#e3e3e3')
        selections_menu_label.grid(padx=50, pady=(10, 0))
        selections = ['Tournament', 'The Best Ones', 'Roulette Wheel']
        self.selection.set(selections[0])
        self.selection.trace('w', self.show)
        menu = tk.OptionMenu(frame, self.selection, *selections)
        menu.config(indicator=0, font=('candara', 12), borderwidth=0, bg='white', width=20)
        menu.grid()
        self.selection_label = tk.Label(frame, text='Number of groups:', bg='#e3e3e3', anchor='w')
        self.selection_label.grid(padx=22, sticky='W')
        self.selection_entry = tk.Entry(frame, textvariable=self.selection_entry_number, bd=3)
        self.selection_entry.grid(padx=24, sticky='WE', pady=(0, 5))

    def create_crossovers_menu(self, frame):
        crossovers_menu_label = tk.Label(frame, text="Choose crossover option:", bg='#e3e3e3')
        crossovers_menu_label.grid(pady=(10, 0))
        crossovers = ["One Point", "Two Points", "Three Points", "Uniform"]
        self.crossover.set(crossovers[0])
        menu = tk.OptionMenu(frame, self.crossover, *crossovers)
        menu.config(indicator=0, font=('candara', 12), borderwidth=0, bg='white', width=20)
        menu.grid()
        tk.Label(frame, text='Crossover probability:', bg='#e3e3e3', anchor='w').grid(padx=22, sticky='W')
        tk.Entry(frame, textvariable=self.crossover_prob, bd=3).grid(padx=24, sticky='WE', pady=(0, 5))

    def create_mutations_menu(self, frame):
        mutations_menu_label = tk.Label(frame, text="Choose mutation option:", bg='#e3e3e3')
        mutations_menu_label.grid(pady=(10, 0))
        mutations = ["Edge Bit", "One Bit", "Two Bits"]
        self.mutation.set(mutations[0])
        menu = tk.OptionMenu(frame, self.mutation, *mutations)
        menu.config(indicator=0, font=('candara', 12), borderwidth=0, bg='white', width=20)
        menu.grid()
        tk.Label(frame, text='Mutation probability:', bg='#e3e3e3', anchor='w').grid(padx=22, sticky='W')
        tk.Entry(frame, textvariable=self.mutation_prob, bd=3).grid(padx=24, sticky='WE', pady=(0, 5))

    def show(self, *args):
        selections = {'Tournament': 0, 'The Best Ones': 1, 'Roulette Wheel': 2}
        selected_option = selections[self.selection.get()]
        if selected_option == 0:
            self.selection_label.config(text='Number of groups:')
            self.selection_label.grid()
            self.selection_entry.grid()
        elif selected_option == 1:
            self.selection_label.config(text='Number of the best ones:')
            self.selection_label.grid()
            self.selection_entry.grid()
        else:
            self.selection_label.grid_remove()
            self.selection_entry.grid_remove()

    def get_all_values(self):
        values = {"selection": self.selection.get(),
                  "crossover": self.crossover.get(),
                  "mutation": self.mutation.get(),
                  "cross_prob": self.crossover_prob.get(),
                  "mutation_prob": self.mutation_prob.get(),
                  "inversion_prob": self.inversion_prob.get(),
                  "beginning": self.beginning_of_interval.get(),
                  "end": self.end_of_interval.get(),
                  "bits": self.number_of_bits.get(),
                  "population": self.population_size.get(),
                  "epochs": self.number_of_epochs.get(),
                  "elite": self.elite_strategy_amount.get(),
                  "max": self.maximization.get()}



        if self.selection.get() == 'Tournament' or self.selection.get() == 'The Best Ones':
            values['k'] = self.selection_entry_number.get()
        else:
            values['k'] = -1

        return values

    def create_timer_window(self, time, arg, value):
        timer_window = tk.Toplevel(self.master)
        tk.Label(timer_window, text=f"Solution found in = {time} seconds. \n Value f({arg}) = {value}.",
                 font=('arial', 12, 'bold'), bg="#ccc").grid(row=0, columnspan=2,
                                                             sticky='WE', pady=10)
