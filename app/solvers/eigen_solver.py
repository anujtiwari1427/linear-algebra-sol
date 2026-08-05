import numpy as np


def solve_eigen(matrix_data):
    """
    Compute eigenvalues and eigenvectors.
    Returns dict with 'eigenvalues', 'eigenvectors', 'steps' or 'error'.
    """
    try:
        A = np.array(matrix_data, dtype=float)
        if A.shape[0] != A.shape[1]:
            return {"error": "Matrix must be square to compute eigenvalues."}

        eigenvalues, eigenvectors = np.linalg.eig(A)

        # Round for display
        evals = [round(float(v.real), 6) for v in eigenvalues]
        evecs = []
        for i in range(eigenvectors.shape[1]):
            col = eigenvectors[:, i]
            evecs.append([round(float(v.real), 6) for v in col])

        steps = f"Solve det(A - λI) = 0 for λ. A is {A.shape[0]}×{A.shape[1]}."
        return {
            "eigenvalues": evals,
            "eigenvectors": evecs,
            "steps": steps
        }

    except Exception as e:
        return {"error": str(e)}
