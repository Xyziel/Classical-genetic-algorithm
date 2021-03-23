from oe.com.selections.Selection import Selection


class TournamentSelection(Selection):

    def __init__(self, k: int):
        self.__group_size = k

    def select_parents(self, population: list, values: list) -> list:
        pass
