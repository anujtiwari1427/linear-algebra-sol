# 🧮 Linear Algebra Solver

> **An interactive, step-by-step web application for solving core linear algebra problems — built with Python (Flask) & NumPy.**

**Developed by:**
| Developer | Roll No. |
|---|---|
| **Anuj Tiwari** | 36 |
| **Dharmendra Pal** | 41 |

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=flat-square&logo=flask)](https://flask.palletsprojects.com)
[![NumPy](https://img.shields.io/badge/NumPy-1.24+-013243?style=flat-square&logo=numpy)](https://numpy.org)
[![Deployed on Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black?style=flat-square&logo=vercel)](https://vercel.com)

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Mathematical Concepts & Formulas](#-mathematical-concepts--formulas)
  - [Matrix Operations](#1-matrix-operations)
  - [Determinants](#2-determinants)
  - [Vector Calculator](#3-vector-calculator)
  - [Systems of Linear Equations](#4-systems-of-linear-equations)
  - [Eigenvalues & Eigenvectors](#5-eigenvalues--eigenvectors)
  - [Geometric Transformations](#6-geometric-transformations)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Deployment](#-deployment)
- [Tech Stack](#-tech-stack)
- [Authors](#-authors)

---

## 🌟 Overview

**Linear Algebra Solver** is a full-stack educational web application that provides elegant, interactive calculators for the most important topics in linear algebra. Every computation is accompanied by **detailed, human-readable step-by-step solutions** — making the tool suitable for students, educators, and anyone needing to verify their mathematical work.

The application is structured as a **Flask Blueprint-based web server**, with each topic having its own isolated route, service, and solver module. All heavy computations are performed by **NumPy** on the server-side, while results are rendered in clean Jinja2 HTML templates.

---

## ✨ Features

| Calculator | Operations Supported |
|---|---|
| **Matrix Operations** | Add, Subtract, Multiply, Transpose, Inverse, Rank, Trace, Determinant |
| **Determinants** | Laplace Cofactor Expansion, Minors Table, Invertibility Check |
| **Vector Calculator** | Magnitude, Normalize, Dot Product, Cross Product, Angle, Projection, Scalar Multiply |
| **Systems of Equations** | Gaussian / Gauss-Jordan Elimination, Rouche-Capelli Consistency Check |
| **Eigenvalues & Eigenvectors** | Characteristic Polynomial, Eigenvalue Extraction, Eigenvector Computation |
| **Geometric Transformations** | 2D/3D Rotation, Scaling, Shearing, Reflection, Projection, Custom Matrix |

All calculators:
- Show **step-by-step mathematical derivations**
- Display **intermediate matrices** at each elimination step
- Highlight **formulas** used at each stage
- Handle **invalid inputs** gracefully with descriptive error messages

---

## 🏛️ Architecture

The project follows a layered **MVC-inspired architecture** with clear separation of concerns between routing, computation, and presentation.

```
┌─────────────────────────────────────────────────────────┐
│                    Browser (Client)                     │
│            Jinja2 HTML Templates + CSS + JS             │
└─────────────────────────┬───────────────────────────────┘
                          │  HTTP Request
                          ▼
┌─────────────────────────────────────────────────────────┐
│              Flask Application Server                   │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │              Blueprint Router Layer              │   │
│  │  home · matrix · vectors · systems · eigen      │   │
│  │  determinants · transform                        │   │
│  └───────────────────┬─────────────────────────────┘   │
│                      │                                  │
│  ┌───────────────────▼─────────────────────────────┐   │
│  │             Services Layer                       │   │
│  │  parser.py · validation.py · latex.py           │   │
│  │  pdf_export.py                                   │   │
│  └───────────────────┬─────────────────────────────┘   │
│                      │                                  │
│  ┌───────────────────▼─────────────────────────────┐   │
│  │             Solvers Layer (Core Math)            │   │
│  │  matrix_solver · vector_solver · system_solver  │   │
│  │  determinant_solver · eigen_solver               │   │
│  │  transform_solver                                │   │
│  └───────────────────┬─────────────────────────────┘   │
│                      │                                  │
│  ┌───────────────────▼─────────────────────────────┐   │
│  │           NumPy Computation Engine               │   │
│  │   np.linalg.eig · np.linalg.solve · np.dot     │   │
│  │   np.linalg.det · np.linalg.inv · np.cross     │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

### Layer Descriptions

| Layer | Path | Responsibility |
|---|---|---|
| **Routes** | `app/routes/` | Flask Blueprints — URL registration, request parsing, response dispatch |
| **Services** | `app/services/` | Input parsing, validation, LaTeX rendering helpers, PDF export |
| **Solvers** | `app/solvers/` | Pure mathematical computation — returns `{result, steps}` dictionaries |
| **Templates** | `app/templates/` | Jinja2 HTML pages (layouts, components, pages) |
| **Static** | `app/static/` | CSS stylesheets and JavaScript files |
| **API** | `api/index.py` | Vercel serverless entrypoint that wraps the Flask app |

### Blueprint Registration (`app/__init__.py`)

```python
from app.routes.home import home
from app.routes.matrix import matrix
from app.routes.vectors import vectors
from app.routes.systems import systems
from app.routes.eigen import eigen
from app.routes.determinants import determinants
from app.routes.transform import transform

app.register_blueprint(home)
app.register_blueprint(matrix)
# ... and so on for each module
```

Each blueprint is completely self-contained — it owns its own route, solver, and template.

---

## 📐 Mathematical Concepts & Formulas

### 1. Matrix Operations

A **matrix** is a rectangular array of numbers A ∈ R^(m×n).

#### Addition / Subtraction
Requires identical dimensions (m × n):

```
C[i][j] = A[i][j] + B[i][j]   (addition)
C[i][j] = A[i][j] - B[i][j]   (subtraction)
```

#### Multiplication
Requires inner dimensions to match: A_(m×k) × B_(k×n) = C_(m×n)

```
C[i][j] = Σ (k=1 to n) A[i][k] × B[k][j]
```

#### Transpose
Swaps rows and columns:

```
(Aᵀ)[i][j] = A[j][i]
```

#### Matrix Inverse (2×2 formula)
Exists only when det(A) ≠ 0:

```
A = | a  b |      A⁻¹ = (1 / det(A)) × |  d  -b |
    | c  d |                             | -c   a |
```

For general n×n matrices:

```
A⁻¹ = (1 / det(A)) × adj(A)
```

#### Rank
The **rank** of a matrix is the number of linearly independent rows (or columns), determined via Gaussian elimination to Row Echelon Form.

#### Trace
The sum of the main diagonal elements:

```
tr(A) = A[1][1] + A[2][2] + ... + A[n][n]
```

---

### 2. Determinants

The **determinant** is a scalar value encoding geometric and algebraic properties of a square matrix.

#### 2×2 Determinant

```
det(A) = | a  b | = (a × d) - (b × c)
         | c  d |
```

#### 3×3 Determinant — Laplace Cofactor Expansion
Expanding along the first row:

```
det(A) = a₁₁·C₁₁ + a₁₂·C₁₂ + a₁₃·C₁₃
```

where the **cofactor** is:

```
C[i][j] = (-1)^(i+j) × M[i][j]
```

and `M[i][j]` is the **minor** — determinant of the submatrix obtained by deleting row `i` and column `j`.

#### Invertibility Check

```
det(A) ≠ 0  →  A is invertible (non-singular)
det(A) = 0  →  A is singular   (no inverse exists)
```

The solver also computes the full **Minors Matrix** and **Cofactors Matrix** for all matrices up to 4×4 size.

---

### 3. Vector Calculator

A **vector** v ∈ R^n is an ordered list of n real numbers.

#### Magnitude (Euclidean Norm)

```
|v| = √(v₁² + v₂² + ... + vₙ²)
```

#### Unit Vector (Normalization)

```
û = v / |v|
```

#### Dot Product

```
a · b = Σ aᵢ × bᵢ = |a||b|cos(θ)
```

#### Angle Between Two Vectors

```
θ = arccos( (a · b) / (|a| × |b|) )
```

#### Cross Product (3D only)
Yields a vector perpendicular to both input vectors:

```
a × b = | î   ĵ   k̂  |
        | ax  ay  az |
        | bx  by  bz |

     = î(ay·bz - az·by) - ĵ(az·bx - ax·bz) + k̂(ax·by - ay·bx)
```

#### Vector Projection

```
proj_b(a) = ((a · b) / |b|²) × b

scalar projection: comp_b(a) = (a · b) / |b|
```

---

### 4. Systems of Linear Equations

Solves the system `Ax = b` where A ∈ R^(m×n), x ∈ R^n, b ∈ R^m.

#### Augmented Matrix
The system is represented as `[A | b]`.

#### Rouché-Capelli Consistency Theorem

| Condition | Result |
|---|---|
| rank(A) ≠ rank([A\|b]) | **No solution** — system is inconsistent |
| rank(A) = rank([A\|b]) = n | **Unique solution** |
| rank(A) = rank([A\|b]) < n | **Infinitely many solutions** |

#### Gauss-Jordan Elimination
The solver performs full **Reduced Row Echelon Form (RREF)** reduction:

1. Form augmented matrix `[A | b]`
2. Forward elimination with partial pivoting (swap rows to avoid zero pivots)
3. Normalize each pivot row: `Rᵢ ← Rᵢ / pivot`
4. Eliminate all other rows: `Rⱼ ← Rⱼ - m × Rᵢ`
5. Read solution from final RREF: `[I | x]`

---

### 5. Eigenvalues & Eigenvectors

For a square matrix A ∈ R^(n×n), a scalar λ and non-zero vector v satisfying:

```
A·v = λ·v
```

are called an **eigenvalue** and its corresponding **eigenvector**.

#### Characteristic Equation
Eigenvalues are roots of the **characteristic polynomial**:

```
det(A - λI) = 0
```

#### For 2×2 Matrices
The characteristic polynomial simplifies to a quadratic:

```
λ² - tr(A)·λ + det(A) = 0
```

Solved with the quadratic formula:

```
λ = [ tr(A) ± √(tr(A)² - 4·det(A)) ] / 2
```

The **discriminant** Δ = tr(A)² - 4·det(A) tells us:

| Δ | Nature of eigenvalues |
|---|---|
| Δ > 0 | Two distinct real eigenvalues |
| Δ = 0 | One repeated (degenerate) eigenvalue |
| Δ < 0 | Two complex conjugate eigenvalues |

#### Eigenvector Computation
For each eigenvalue λᵢ, solve the null space system:

```
(A - λᵢ·I)·vᵢ = 0
```

The solver displays the shifted matrix `(A - λᵢI)` for each eigenvalue and reports the corresponding normalized eigenvector.

---

### 6. Geometric Transformations

Linear transformations are represented as matrices T such that:

```
v' = T · v
```

#### 2D Rotation by angle θ

```
R(θ) = | cos θ  -sin θ |    det(R) = 1
       | sin θ   cos θ |
```

#### 3D Rotation about X-axis

```
Rₓ(θ) = | 1    0       0    |
         | 0   cos θ  -sin θ |
         | 0   sin θ   cos θ |
```

#### 3D Rotation about Y-axis

```
R_y(θ) = |  cos θ  0  sin θ |
          |    0    1    0   |
          | -sin θ  0  cos θ |
```

#### 3D Rotation about Z-axis

```
R_z(θ) = | cos θ  -sin θ  0 |
          | sin θ   cos θ  0 |
          |   0       0    1 |
```

#### Scaling

```
S(sx, sy) = | sx   0 |
            |  0  sy |
```

#### Shearing

```
Shear_x(k) = | 1  k |    Shear_y(k) = | 1  0 |
             | 0  1 |                  | k  1 |
```

#### Reflection

```
Reflect-X       = |  1   0 |    Reflect-Y      = | -1  0 |
                  |  0  -1 |                     |  0  1 |

Reflect-Origin  = | -1   0 |
                  |  0  -1 |
```

#### Geometric Interpretation via Determinant

| det(T) | Interpretation |
|---|---|
| det(T) = ±1 | Rigid transformation — preserves distances and area |
| det(T) = 0 | Collapses space into lower dimension (non-invertible) |
| \|det(T)\| ≠ 1 | Area/volume is scaled by factor \|det(T)\| |

---

## 📁 Project Structure

```
linear-algebra-sol/
│
├── app.py                          # Application entrypoint (local dev)
├── requirements.txt                # Python dependencies
├── vercel.json                     # Vercel deployment configuration
├── Procfile                        # Gunicorn process definition
│
├── api/
│   └── index.py                    # Vercel serverless wrapper
│
└── app/
    ├── __init__.py                  # Flask app factory + Blueprint registration
    │
    ├── routes/                      # Blueprint URL handlers
    │   ├── home.py
    │   ├── matrix.py
    │   ├── vectors.py
    │   ├── systems.py
    │   ├── eigen.py
    │   ├── determinants.py
    │   └── transform.py
    │
    ├── solvers/                     # Core mathematical computation engines
    │   ├── matrix_solver.py         # Matrix ops: add, mul, inv, transpose, rank, trace
    │   ├── vector_solver.py         # Vector ops: dot, cross, angle, projection, normalize
    │   ├── system_solver.py         # Gauss-Jordan solver + Rouche-Capelli check
    │   ├── determinant_solver.py    # Laplace expansion + cofactors matrix builder
    │   ├── eigen_solver.py          # Characteristic polynomial + eigenvectors
    │   └── transform_solver.py      # Geometric transformation matrix builder
    │
    ├── services/                    # Shared utilities
    │   ├── parser.py                # Input parsing helpers
    │   ├── validation.py            # Input validation logic
    │   ├── latex.py                 # LaTeX rendering helpers
    │   └── pdf_export.py            # PDF export service
    │
    ├── templates/
    │   ├── layouts/
    │   │   └── base.html            # Master layout (navbar, footer, MathJax CDN)
    │   ├── components/
    │   │   └── navbar.html          # Shared navigation component
    │   └── pages/
    │       ├── home.html            # Landing page with tool cards
    │       ├── matrix.html          # Matrix operations calculator UI
    │       ├── determinant.html     # Determinant calculator UI
    │       ├── vectors.html         # Vector calculator UI
    │       ├── systems.html         # Systems of equations solver UI
    │       ├── eigen.html           # Eigenvalue / eigenvector calculator UI
    │       ├── transform.html       # Geometric transformation explorer UI
    │       ├── concepts.html        # Mathematical concepts reference page
    │       └── solutions.html       # Solutions viewer
    │
    └── static/
        ├── css/                     # Stylesheets
        └── js/                      # Client-side JavaScript
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.10+**
- `pip` package manager

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/linear-algebra-sol.git
cd linear-algebra-sol

# 2. (Optional) Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Running Locally

```bash
python app.py
```

The application will start at **http://127.0.0.1:5000**

---

## ☁️ Deployment

The application is deployed on **Vercel** using the `@vercel/python` builder.

The `vercel.json` routes all incoming requests to `api/index.py`, which wraps the Flask WSGI application as a serverless function:

```json
{
  "version": 2,
  "builds": [{ "src": "api/index.py", "use": "@vercel/python" }],
  "routes": [{ "src": "/(.*)", "dest": "api/index.py" }]
}
```

For production-like local testing, the `Procfile` uses **Gunicorn**:

```
web: gunicorn app:app
```

---

## 🛠️ Tech Stack

| Technology | Role |
|---|---|
| **Python 3.10+** | Server-side programming language |
| **Flask 3.0+** | Web framework — routing, Blueprints, Jinja2 templating |
| **NumPy 1.24+** | Linear algebra computation engine (linalg, dot, eig, solve, cross) |
| **Jinja2** | HTML templating engine (built into Flask) |
| **MathJax** | Client-side LaTeX formula rendering in browser |
| **Gunicorn** | Production WSGI HTTP server |
| **Vercel** | Serverless cloud deployment platform |

---

## 👥 Authors

| Name | Roll No. | Role |
|---|---|---|
| **Anuj Tiwari** | 36 | Student & Core Developer |
| **Dharmendra Pal** | 41 | Student & Core Developer |

---

> *"Mathematics is the language with which God has written the universe."*  
> — Galileo Galilei
