from flask import Blueprint, render_template, request, jsonify
from app.solvers.vector_solver import solve_vector

vectors = Blueprint("vectors", __name__)


@vectors.route("/calculators/vectors/")
def vectors_page():
    return render_template("pages/vectors.html")


@vectors.route("/api/vectors", methods=["POST"])
def api_vectors():
    data = request.get_json()
    operation = data.get("operation", "")
    vec_a = data.get("vec_a", [])
    vec_b = data.get("vec_b", None)
    scalar = data.get("scalar", None)
    result = solve_vector(operation, vec_a, vec_b, scalar)
    return jsonify(result)
