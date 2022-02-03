import chess
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/v1/<chess_figure>/<current_field>")
def index(chess_figure, current_field):
    current_field = (
        current_field.capitalize()
    )  # for passing to function of ChessBoard class
    board = chess.ChessBoard()

    try:
        figure_class = getattr(chess, chess_figure.capitalize())
        figure = figure_class(board, current_field)
    except AttributeError:
        return jsonify(
            availableMoves=[],
            error="No figure with such name",
            figure=None,
            current_field=current_field,
        )

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


if __name__ == "__main__":
    app.run()
