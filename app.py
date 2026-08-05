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
    template_folder="app/templates",
    static_folder="app/static"
)

app.register_blueprint(home)
app.register_blueprint(matrix)
app.register_blueprint(vectors)
app.register_blueprint(systems)
app.register_blueprint(eigen)
app.register_blueprint(determinants)
app.register_blueprint(transform)

if __name__ == "__main__":
    app.run(debug=True)