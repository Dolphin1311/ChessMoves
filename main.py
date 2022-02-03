from chess import ChessBoard, King, Bishop, Rook, Pawn, Knight, Queen

if __name__ == "__main__":
    board = ChessBoard()
    board.show_board()
    king = King(board, "H2")
    rook = Rook(board, "H1")
    bishop = Bishop(board, "E4")
    knight = Knight(board, "E4")
    pawn = Pawn(board, "C2")
    queen = Queen(board, "E4")

    print("\n")
    print(queen.list_available_moves())
