import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from flask import Flask
from app.routes.home import home
from app.routes.matrix import matrix
from app.routes.vectors import vectors
from app.routes.systems import systems
from app.routes.eigen import eigen
from app.routes.determinants import determinants
from app.routes.transform import transform

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "app", "templates"),
    static_folder=os.path.join(BASE_DIR, "app", "static")
)

app.register_blueprint(home)
app.register_blueprint(matrix)
app.register_blueprint(vectors)
app.register_blueprint(systems)
app.register_blueprint(eigen)
app.register_blueprint(determinants)
app.register_blueprint(transform)
