from abc import ABC, abstractmethod
from custom_list import CustomList

relation_let_to_num = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
}


class ChessBoard:
    _letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    def __init__(self):
        self._board_grid = CustomList()
        self._generate_board()

    def _generate_board(self):
        for square in range(1, 9):
            append_list = CustomList([(letter + str(square)) for letter in self._letters])
            self._board_grid.append(append_list)

    def show_board(self):
        for row in self._board_grid:
            print(row)

    def __iter__(self):
        return self._board_grid

    def get_position(self, row, col):
        try:
            return self._board_grid[row][col]
        except IndexError:
            raise IndexError