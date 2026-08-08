import numpy as np

def solve_eigen(matrix_data):
    """
    Compute eigenvalues and eigenvectors with detailed step-by-step mathematical solutions.
    """
    try:
        A = np.array(matrix_data, dtype=float)
        n = A.shape[0]
        if A.shape[0] != A.shape[1]:
            return {"error": "Matrix must be square (n×n) to compute eigenvalues."}

        steps = []
        steps.append(f"📌 Step 1: Characteristic Equation Setup")
        steps.append(f"  • Formula: det(A - λI) = 0")
        steps.append(f"  • Matrix A ({n}×{n}):")
        steps.append(_format_matrix(A))

        eigenvalues, eigenvectors = np.linalg.eig(A)

        if n == 2:
            a, b = A[0, 0], A[0, 1]
            c, d = A[1, 0], A[1, 1]
            tr = a + d
            det = (a * d) - (b * c)
            steps.append(f"\n📌 Step 2: Characteristic Polynomial for 2×2 Matrix")
            steps.append(f"  • Formula: λ² - trace(A)·λ + det(A) = 0")
            steps.append(f"  • trace(A) = {a:.4g} + {d:.4g} = {tr:.4g}")
            steps.append(f"  • det(A)   = ({a:.4g} × {d:.4g}) - ({b:.4g} × {c:.4g}) = {det:.4g}")
            steps.append(f"  • Characteristic Equation: λ² - ({tr:.4g})λ + ({det:.4g}) = 0")
            
            disc = (tr**2) - (4 * det)
            steps.append(f"\n📌 Step 3: Solve Roots using Quadratic Formula")
            steps.append(f"  • Discriminant Δ = tr² - 4·det = ({tr:.4g})² - 4({det:.4g}) = {disc:.4g}")
            
        else:
            steps.append(f"\n📌 Step 2: Compute Roots of det(A - λI) = 0")

        evals = [round(float(v.real), 6) for v in eigenvalues]
        evecs = []
        steps.append(f"\n✅ Step 3: Extracted Eigenvalues (λ):")
        for idx, val in enumerate(evals):
            steps.append(f"  • λ_{idx+1} = {val}")

        steps.append(f"\n📌 Step 4: Solve for Corresponding Eigenvectors (A - λ_i·I)v_i = 0")
        for i in range(eigenvectors.shape[1]):
            col = eigenvectors[:, i]
            vec_rounded = [round(float(v.real), 6) for v in col]
            evecs.append(vec_rounded)
            lam = evals[i]
            
            steps.append(f"\n  🔍 For Eigenvalue λ_{i+1} = {lam}:")
            shifted_A = A - lam * np.eye(n)
            steps.append(f"  • (A - {lam}I):")
            steps.append(_format_matrix(shifted_A))
            steps.append(f"  • Eigenvector v_{i+1} = {vec_rounded}")

        return {
            "eigenvalues": evals,
            "eigenvectors": evecs,
            "steps": "\n".join(steps)
        }

    except Exception as e:
        return {"error": str(e)}


def _format_matrix(M):
    lines = []
    for row in M:
        formatted_row = "  ".join(f"{v:8.4g}" for v in row)
        lines.append(f"  [ {formatted_row} ]")
    return "\n".join(lines)
