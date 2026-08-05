from flask import Blueprint, render_template, request, jsonify
from app.solvers.transform_solver import solve_transform

transform = Blueprint("transform", __name__)


@transform.route("/calculators/transform/")
def transform_page():
    return render_template("pages/transform.html")


@transform.route("/api/transform", methods=["POST"])
def api_transform():
    data = request.get_json()
    transform_type = data.get("transform_type", "rotation_2d")
    params = data.get("params", {})
    vector = data.get("vector", None)
    result = solve_transform(transform_type, params, vector)
    return jsonify(result)
