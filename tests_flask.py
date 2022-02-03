import json
from main import app


def test_get_available_moves():
    app.config["DEBUG"] = True
    app.config["TESTING"] = True
    response = app.test_client().get("/api/v1/rook/h1")
    res = json.loads(response.data.decode("utf-8"))
    assert res["availableMoves"] == [
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
    assert res["error"] is None
    assert res["figure"] == "Rook"


def test_get_move():
    app.config["DEBUG"] = True
    app.config["TESTING"] = True
    response = app.test_client().get("/api/v1/queen/e4/g4")
    res = json.loads(response.data.decode("utf-8"))
    assert res["figure"] == "Queen"
    assert res["error"] is None
    assert res["move"] == "Valid"
