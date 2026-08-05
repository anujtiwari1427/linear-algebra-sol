import numpy as np


def solve_matrix(operation, matrix_a, matrix_b=None):
    """
    Perform a matrix operation.
    Returns a dict with 'result' or 'error'.
    """
    try:
        A = np.array(matrix_a, dtype=float)

        if operation == "transpose":
            result = A.T.tolist()
            return {"result": result, "steps": f"Transpose: flip rows and columns of A."}

        if operation == "inverse":
            if A.shape[0] != A.shape[1]:
                return {"error": "Matrix must be square to find its inverse."}
            det = np.linalg.det(A)
            if abs(det) < 1e-10:
                return {"error": "Matrix is singular (det ≈ 0) — inverse does not exist."}
            result = np.linalg.inv(A).tolist()
            return {"result": result, "steps": f"det(A) = {det:.4f} ≠ 0, so inverse exists."}

        if operation == "determinant":
            if A.shape[0] != A.shape[1]:
                return {"error": "Matrix must be square to compute determinant."}
            det = np.linalg.det(A)
            return {"result": [[round(det, 6)]], "steps": f"det(A) = {det:.6f}"}

        if operation == "rank":
            r = np.linalg.matrix_rank(A)
            return {"result": [[r]], "steps": f"rank(A) = {r}"}

        if operation == "trace":
            if A.shape[0] != A.shape[1]:
                return {"error": "Matrix must be square to compute trace."}
            t = np.trace(A)
            return {"result": [[round(t, 6)]], "steps": f"trace(A) = sum of diagonal = {t:.6f}"}

        if matrix_b is None:
            return {"error": "Second matrix (B) is required for this operation."}

        B = np.array(matrix_b, dtype=float)

        if operation == "add":
            if A.shape != B.shape:
                return {"error": "Matrices must have the same dimensions to add."}
            result = (A + B).tolist()
            return {"result": result, "steps": "A + B: add corresponding elements."}

        if operation == "subtract":
            if A.shape != B.shape:
                return {"error": "Matrices must have the same dimensions to subtract."}
            result = (A - B).tolist()
            return {"result": result, "steps": "A - B: subtract corresponding elements."}

        if operation == "multiply":
            if A.shape[1] != B.shape[0]:
                return {"error": f"A columns ({A.shape[1]}) must equal B rows ({B.shape[0]}) for multiplication."}
            result = (A @ B).tolist()
            return {"result": result, "steps": f"A × B: ({A.shape[0]}×{A.shape[1]}) × ({B.shape[0]}×{B.shape[1]}) = ({A.shape[0]}×{B.shape[1]})"}

        return {"error": f"Unknown operation: {operation}"}

    except Exception as e:
        return {"error": str(e)}
