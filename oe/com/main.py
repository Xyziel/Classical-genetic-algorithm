from oe.com.models import *
from oe.com.mutations import *
from oe.com.crossovers import *
from oe.com.selections import *


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
    c_prob = 0.85  # prawdopodobienstwa krzyzowania
    m_prob = 0.05  # prawd. mutacji

    pop = Population()
    pop.create_random_population(size, n, bits)
    fun = MyFunction(f)
    pop_dec = pop.get_population_decimal(a, b)
    values = fun.get_values_population_dec(pop_dec)

    # print(pop_dec)
    # print(values)

    sel = TournamentSelection(k)
    selected_parents = sel.select_parents(pop, values)

    crossover = OnePointCrossover(c_prob)
    new_generation = crossover.cross(selected_parents, size)

    mutation = OneBitFlipMutation(m_prob)
    mutation.mutate(new_generation)

    for i in range(i):
        new_generation_dec = new_generation.get_population_decimal(a, b)
        values = fun.get_values_population_dec(new_generation_dec)
        selected_parents = sel.select_parents(new_generation, values)
        new_generation = crossover.cross(selected_parents, size)
        mutation.mutate(new_generation)

    print("Wartosc min (powinna byc bliska 0): " + str(min(values)))
if __name__ == '__main__':
    main()
