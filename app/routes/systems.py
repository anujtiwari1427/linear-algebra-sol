from flask import Blueprint, render_template, request, jsonify
from app.solvers.system_solver import solve_system

systems = Blueprint("systems", __name__)


@systems.route("/calculators/systems/")
def systems_page():
    return render_template("pages/systems.html")


@systems.route("/api/systems", methods=["POST"])
def api_systems():
    data = request.get_json()
    A = data.get("A", [])
    b = data.get("b", [])
    result = solve_system(A, b)
    return jsonify(result)
