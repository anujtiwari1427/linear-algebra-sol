import numpy as np


def solve_determinant(matrix_data):
    """
    Compute determinant with step-by-step cofactor expansion for small matrices.
    """
    try:
        A = np.array(matrix_data, dtype=float)
        n = A.shape[0]

        if A.shape[0] != A.shape[1]:
            return {"error": "Matrix must be square to compute determinant."}

        det = round(float(np.linalg.det(A)), 8)
        steps = []

        if n == 1:
            steps.append(f"det([{A[0,0]}]) = {A[0,0]}")

        elif n == 2:
            a, b, c, d = A[0,0], A[0,1], A[1,0], A[1,1]
            steps.append(f"For a 2×2 matrix:")
            steps.append(f"det(A) = ad - bc")
            steps.append(f"       = ({a})({d}) - ({b})({c})")
            steps.append(f"       = {a*d} - {b*c}")
            steps.append(f"       = {det}")

        elif n == 3:
            steps.append("Using cofactor expansion along first row:")
            for j in range(3):
                minor = np.delete(np.delete(A, 0, axis=0), j, axis=1)
                minor_det = round(float(np.linalg.det(minor)), 6)
                sign = "+" if (0 + j) % 2 == 0 else "−"
                entry = A[0, j]
                steps.append(f"  {sign} a[0][{j}] × M[0][{j}] = {sign} {entry} × {minor_det} = {round(entry * minor_det * (1 if (j%2==0) else -1), 6)}")
            steps.append(f"det(A) = {det}")

        else:
            steps.append(f"Matrix is {n}×{n}. Using numpy LU decomposition.")
            steps.append(f"det(A) = {det}")
            rank = int(np.linalg.matrix_rank(A))
            steps.append(f"rank(A) = {rank}")
            steps.append("A is singular (non-invertible)." if abs(det) < 1e-10 else "A is non-singular (invertible).")

        # Minors and cofactors for n<=4
        minors = []
        cofactors = []
        if n <= 4:
            for r in range(n):
                minor_row = []
                cofactor_row = []
                for c in range(n):
                    sub = np.delete(np.delete(A, r, axis=0), c, axis=1)
                    m = round(float(np.linalg.det(sub)), 6)
                    cof = round(m * ((-1) ** (r + c)), 6)
                    minor_row.append(m)
                    cofactor_row.append(cof)
                minors.append(minor_row)
                cofactors.append(cofactor_row)

        return {
            "det": det,
            "steps": "\n".join(steps),
            "minors": minors if n <= 4 else [],
            "cofactors": cofactors if n <= 4 else [],
            "singular": abs(det) < 1e-10,
            "size": n
        }

    except Exception as e:
        return {"error": str(e)}
