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

class Figure(ABC):
    def __init__(self, board: ChessBoard, field: str):
        self.board = board
        self.field = field

    @abstractmethod
    def list_available_moves(self):
        pass

    @abstractmethod
    def validate_move(self, dest_field: str):
        pass


class King(Figure):
    def list_available_moves(self):
        king_moves = ((1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0))
        available_moves = []
        # get indexes of figure position
        pos_row = int(self.field[1]) - 1
        pos_col = int(relation_let_to_num[self.field[0]]) - 1

        for move in king_moves:
            row, col = move
            try:
                available_moves.append(self.board.get_position(pos_row + row, pos_col + col))
            except IndexError:
                pass

        return available_moves

    def validate_move(self, dest_field: str):
        return dest_field in self.list_available_moves()

class Queen(Figure):
    def list_available_moves(self):
        diagonal_directions = ((-1, -1), (-1, 1), (1, 1), (1, -1))
        directions = ((0, -1), (-1, 0), (0, 1), (1, 0))  # left, up, right, down
        available_moves = []
        # get indexes of figure position
        pos_row = int(self.field[1]) - 1
        pos_col = int(relation_let_to_num[self.field[0]]) - 1

        for d in diagonal_directions:
            for i in range(1, 8):
                try:
                    if d == (-1, -1):
                        available_moves.append(self.board.get_position(pos_row - i, pos_col - i))
                    elif d == (-1, 1):
                        available_moves.append(self.board.get_position(pos_row - i, pos_col + i))
                    elif d == (1, 1):
                        available_moves.append(self.board.get_position(pos_row + i, pos_col + i))
                    elif d == (1, -1):
                        available_moves.append(self.board.get_position(pos_row + i, pos_col - i))
                except IndexError:
                    pass

        for d in directions:
            for i in range(1, 8):
                try:
                    if d == (0, -1):
                        available_moves.append(self.board.get_position(pos_row, pos_col - i))
                    elif d == (-1, 0):
                        available_moves.append(self.board.get_position(pos_row - i, pos_col))
                    elif d == (0, 1):
                        available_moves.append(self.board.get_position(pos_row, pos_col + i))
                    elif d == (1, 0):
                        available_moves.append(self.board.get_position(pos_row + i, pos_col))
                except IndexError:
                    pass

        return available_moves

    def validate_move(self, dest_field: str):
        return dest_field in self.list_available_moves()


class Bishop(Figure):
    def list_available_moves(self):
        directions = ((-1, -1), (-1, 1), (1, 1), (1, -1))
        available_moves = []
        # get indexes of figure position
        pos_row = int(self.field[1]) - 1
        pos_col = int(relation_let_to_num[self.field[0]]) - 1

        for d in directions:
            for i in range(1, 8):
                try:
                    if d == (-1, -1):
                        available_moves.append(self.board.get_position(pos_row - i, pos_col - i))
                    elif d == (-1, 1):
                        available_moves.append(self.board.get_position(pos_row - i, pos_col + i))
                    elif d == (1, 1):
                        available_moves.append(self.board.get_position(pos_row + i, pos_col + i))
                    elif d == (1, -1):
                        available_moves.append(self.board.get_position(pos_row + i, pos_col - i))
                except IndexError:
                    pass

        return available_moves

    def validate_move(self, dest_field: str):
        return dest_field in self.list_available_moves()


class Rook(Figure):
    def list_available_moves(self):
        directions = ((0, -1), (-1, 0), (0, 1), (1, 0))  # left, up, right, down
        available_moves = []
        # get indexes of figure position
        pos_row = int(self.field[1]) - 1
        pos_col = int(relation_let_to_num[self.field[0]]) - 1

        for d in directions:
            for i in range(1, 8):
                try:
                    if d == (0, -1):
                        available_moves.append(self.board.get_position(pos_row, pos_col - i))
                    elif d == (-1, 0):
                        available_moves.append(self.board.get_position(pos_row - i, pos_col))
                    elif d == (0, 1):
                        available_moves.append(self.board.get_position(pos_row, pos_col + i))
                    elif d == (1, 0):
                        available_moves.append(self.board.get_position(pos_row + i, pos_col))
                except IndexError:
                    pass

        return available_moves

    def validate_move(self, dest_field: str):
        return dest_field in self.list_available_moves()


class Knight(Figure):
    def list_available_moves(self):
        knight_moves = ((1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1))
        available_moves = []
        # get indexes of figure position
        pos_row = int(self.field[1]) - 1
        pos_col = int(relation_let_to_num[self.field[0]]) - 1

        for move in knight_moves:
            row, col = move
            try:
                available_moves.append(self.board.get_position(pos_row + row, pos_col + col))
            except IndexError:
                pass

        return available_moves

    def validate_move(self, dest_field: str):
        return dest_field in self.list_available_moves()