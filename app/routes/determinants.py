from flask import Blueprint, render_template, request, jsonify
from app.solvers.determinant_solver import solve_determinant

determinants = Blueprint("determinants", __name__)


@determinants.route("/calculators/determinants/")
def determinants_page():
    return render_template("pages/determinant.html")


@determinants.route("/api/determinants", methods=["POST"])
def api_determinants():
    data = request.get_json()
    matrix_data = data.get("matrix", [])
    result = solve_determinant(matrix_data)
    return jsonify(result)
