from oe.com.models import *
from oe.com.mutations import *
from oe.com.crossovers import *
from oe.com.selections import *
from oe.com.elite import *

def f(x):
    return x[0] ** 2 + x[1] ** 2


def main():

    # Przykladowe dane
    a = -10  # poczatek przedzialu
    b = 10  # koniec przedzialu
    bits = 20  # liczba bitow genu # Pytanie czy moga byc bity czy ustawiac dokladnosc?
    n = 2  # liczba zmiennych
    size = 100  # rozmiar populacji
    i = 100  # liczba iteracji
    k = 5  # liczba grup turniejowych
    cross_prob = 0.85  # prawdopodobienstwa krzyzowania
    mutate_prob = 0.15  # prawd. mutacji
    invert_prob = 0.15  # prawd. inwersji
    population_percent = 0.1  # procent populacji w selekcji najlepszych oraz ruletce
    maximum = False  # czy maksymalizacja
    elite_number = 5  # liczba elitarnych osobnikow

    population = Population()
    population.create_random_population(size, n, bits)
    fun = MyFunction(f)
    population_decimal = population.get_population_decimal(a, b)
    values = fun.get_values_population_dec(population_decimal)

    selection = TheBestOnesSelection(population_percent)
    crossover = OnePointCrossover(cross_prob)
    mutation = OneBitFlipMutation(mutate_prob)
    inversion = Inversion(invert_prob)
    elite = ElitismStrategy(elite_number)

    value_in_each_it = []

    for i in range(i):
        elite_population = elite.choose_n_best(population, values, maximum)
        selected_parents = selection.select_parents(population, values, maximum)
        population = crossover.cross(selected_parents, size - elite_number)
        mutation.mutate(population)
        inversion.invert(population)

        population + elite_population

        population_dec = population.get_population_decimal(a, b)
        values = fun.get_values_population_dec(population_dec)

        if maximum:
            value_in_each_it.append(max(values))
        else:
            value_in_each_it.append(min(values))

    if maximum:
        print("Wartosc max (powinna byc bliska 200): " + str(max(values)))
        print("Jak zmienia")
    else:
        print("Wartosc min (powinna byc bliska 0): " + str(min(values)))
        print("Jak zmienia")
    print(value_in_each_it)


if __name__ == '__main__':
    main()
