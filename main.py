import chess
from flask import Flask, jsonify, abort

app = Flask(__name__)


@app.errorhandler(409)
def conflict_error(error):
    return jsonify(error=error.description), 409


@app.errorhandler(404)
def not_found_error(error):
    return jsonify(error=error.description), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify(error=str(error)), 500


def check_figure_class_exists(chess_figure: str):
    try:
        figure_class = getattr(chess, chess_figure.capitalize())
        return figure_class
    except AttributeError:
        return None


@app.route("/api/v1/<chess_figure>/<current_field>")
def get_available_moves(chess_figure: str, current_field: str):
    current_field = current_field.capitalize()
    board = chess.ChessBoard()
    figure_class = check_figure_class_exists(chess_figure)

    # check if class exists
    if figure_class is None:
        abort(404, description="There is no such figure")

    # create instance of class
    figure = figure_class(board, current_field)

    # check if field exists
    if not board.check_if_field_exists(current_field):
        abort(403, description="There is no such field")

    return jsonify(
        availableMoves=figure.list_available_moves(),
        error=None,
        figure=type(figure).__name__,
        currentField=current_field,
    )


@app.route("/api/v1/<chess_figure>/<current_field>/<dest_field>")
def get_move(chess_figure: str, current_field: str, dest_field: str):
    current_field = current_field.capitalize()
    dest_field = dest_field.capitalize()
    board = chess.ChessBoard()
    figure_class = check_figure_class_exists(chess_figure)

    # check if class exists
    if figure_class is None:
        abort(404, description="There is no such figure")

    # create instance of class
    figure = figure_class(board, current_field)

    # check if fields exists
    if not board.check_if_field_exists(
        current_field
    ) or not board.check_if_field_exists(dest_field):
        abort(403, description="There is no such field")

    move = figure.validate_move(dest_field)

    return jsonify(
        move="Valid" if move else "Invalid",
        error=None if move else "Current move is not permitted",
        figure=type(figure).__name__,
        currentField=current_field,
        destField=dest_field,
    )


if __name__ == "__main__":
    app.run()
