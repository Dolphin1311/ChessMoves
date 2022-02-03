from chess import King, Bishop, Rook, Knight, Queen, Pawn, ChessBoard


def test_king_moves():
    board = ChessBoard()
    king = King(board, "H2")
    assert king.list_available_moves() == ["G3", "G2", "G1", "H1", "H3"]


def test_rook_moves():
    board = ChessBoard()
    rook = Rook(board, "H1")
    assert rook.list_available_moves() == [
        "G1",
        "F1",
        "E1",
        "D1",
        "C1",
        "B1",
        "A1",
        "H2",
        "H3",
        "H4",
        "H5",
        "H6",
        "H7",
        "H8",
    ]


def test_bishop_moves():
    board = ChessBoard()
    bishop = Bishop(board, "E4")
    assert bishop.list_available_moves() == [
        "D3",
        "C2",
        "B1",
        "F3",
        "G2",
        "H1",
        "F5",
        "G6",
        "H7",
        "D5",
        "C6",
        "B7",
        "A8",
    ]


def test_knight_moves():
    board = ChessBoard()
    knight = Knight(board, "E4")
    assert knight.list_available_moves() == [
        "C5",
        "C3",
        "D2",
        "F2",
        "G3",
        "G5",
        "F6",
        "D6",
    ]


def test_queen_moves():
    board = ChessBoard()
    queen = Queen(board, "E4")
    assert queen.list_available_moves() == [
        "D3",
        "C2",
        "B1",
        "F3",
        "G2",
        "H1",
        "F5",
        "G6",
        "H7",
        "D5",
        "C6",
        "B7",
        "A8",
        "D4",
        "C4",
        "B4",
        "A4",
        "E3",
        "E2",
        "E1",
        "F4",
        "G4",
        "H4",
        "E5",
        "E6",
        "E7",
        "E8",
    ]


def test_pawn_moves():
    board = ChessBoard()
    pawn = Pawn(board, "C2")
    assert pawn.list_available_moves() == ["C3"]
