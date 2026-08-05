from flask import Blueprint, render_template, request, jsonify
from app.solvers.matrix_solver import solve_matrix

matrix = Blueprint("matrix", __name__)


@matrix.route("/calculators/matrix/")
def matrix_page():
    return render_template("pages/matrix.html")


@matrix.route("/api/matrix", methods=["POST"])
def api_matrix():
    data = request.get_json()
    operation = data.get("operation", "")
    matrix_a = data.get("matrix_a", [])
    matrix_b = data.get("matrix_b", None)
    result = solve_matrix(operation, matrix_a, matrix_b)
    return jsonify(result)
