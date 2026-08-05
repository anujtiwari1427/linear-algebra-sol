from flask import Blueprint, render_template, request, jsonify
from app.solvers.eigen_solver import solve_eigen

eigen = Blueprint("eigen", __name__)


@eigen.route("/calculators/eigen/")
def eigen_page():
    return render_template("pages/eigen.html")


@eigen.route("/api/eigen", methods=["POST"])
def api_eigen():
    data = request.get_json()
    matrix_data = data.get("matrix", [])
    result = solve_eigen(matrix_data)
    return jsonify(result)
