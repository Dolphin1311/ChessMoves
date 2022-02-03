import chess
from flask import Flask, jsonify

app = Flask(__name__)


@app.errorhandler(404)
def not_found_error(error):
    return f'Page not found. Error code {error}'

def check_figure_exists(chess_figure: str):
    try:
        figure_class = getattr(chess, chess_figure.capitalize())
        return figure_class
    except AttributeError:
        return None


@app.route("/api/v1/<chess_figure>/<current_field>")
def get_available_moves(chess_figure: str, current_field: str):
    current_field = (
        current_field.capitalize()
    )  # for passing to a function of ChessBoard class
    board = chess.ChessBoard()
    figure_class = check_figure_exists(chess_figure)

    # check if class exists
    if figure_class is None:
        return jsonify(
            availableMoves=[],
            error="No figure with such name",
            figure=None,
            current_field=current_field,
        )

    # create instance of class
    figure = figure_class(board, current_field)

    # check if field exists
    if not board.check_if_field_exists(current_field):
        return jsonify(
            availableMoves=[],
            error="No such field on the board",
            figure=type(figure).__name__,
            current_field=current_field,
        )

    return jsonify(
        availableMoves=figure.list_available_moves(),
        error=None,
        figure=type(figure).__name__,
        current_field=current_field,
    )


@app.route("/api/v1/<chess_figure>/<current_field>/<dest_field>")
def get_move(chess_figure: str, current_field: str, dest_field: str):
    # for passing to a functions of ChessBoard class
    current_field = current_field.capitalize()
    dest_field = dest_field.capitalize()
    board = chess.ChessBoard()
    figure_class = check_figure_exists(chess_figure)

    # check if class exists
    if figure_class is None:
        return jsonify(
            move=None,
            error="No figure with such name",
            figure=None,
            current_field=current_field,
            dest_field=dest_field,
        )

    # create instance of class
    figure = figure_class(board, current_field)

    # check if field exists
    if not board.check_if_field_exists(current_field) or not board.check_if_field_exists(
        dest_field
    ):
        return jsonify(
            move="Invalid",
            error="No such field on the board",
            figure=type(figure).__name__,
            current_field=current_field,
            dest_field=dest_field,
        )

    move = figure.validate_move(dest_field)
    return jsonify(
        move="Valid" if move else "Invalid",
        error=None if move else "Current move is not permitted",
        figure=type(figure).__name__,
        current_field=current_field,
        dest_field=dest_field,
    )


if __name__ == "__main__":
    app.run()
