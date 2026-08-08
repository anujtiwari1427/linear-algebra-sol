import numpy as np

def solve_determinant(matrix_data):
    """
    Compute determinant with detailed step-by-step Laplace expansion and cofactor matrices.
    """
    try:
        A = np.array(matrix_data, dtype=float)
        n = A.shape[0]

        if A.shape[0] != A.shape[1]:
            return {"error": "Matrix must be square (n×n) to compute determinant."}

        det = round(float(np.linalg.det(A)), 8)
        steps = []
        steps.append(f"📌 Step 1: Input Matrix A ({n}×{n}):")
        steps.append(_format_matrix(A))

        if n == 1:
            steps.append(f"\n📌 Step 2: 1×1 Determinant:")
            steps.append(f"  • det(A) = {A[0,0]:.4g}")

        elif n == 2:
            a, b, c, d = A[0,0], A[0,1], A[1,0], A[1,1]
            steps.append(f"\n📌 Step 2: 2×2 Determinant Formula: det(A) = (a × d) - (b × c)")
            steps.append(f"  • a = {a:.4g}, b = {b:.4g}, c = {c:.4g}, d = {d:.4g}")
            steps.append(f"  • det(A) = ({a:.4g} × {d:.4g}) - ({b:.4g} × {c:.4g})")
            steps.append(f"         = {a*d:.4g} - {b*c:.4g} = {det:.6g}")

        elif n == 3:
            steps.append(f"\n📌 Step 2: Laplace Expansion along First Row (Row 1):")
            steps.append(f"  Formula: det(A) = a₁₁·C₁₁ + a₁₂·C₁₂ + a₁₃·C₁₃")
            terms = []
            for j in range(3):
                minor = np.delete(np.delete(A, 0, axis=0), j, axis=1)
                minor_det = round(float(np.linalg.det(minor)), 6)
                sign_val = 1 if (j % 2 == 0) else -1
                sign_str = "+" if sign_val == 1 else "−"
                entry = A[0, j]
                term_val = entry * minor_det * sign_val
                terms.append(term_val)
                steps.append(f"\n  🔍 Term {j+1} (Entry A[1,{j+1}] = {entry:.4g}):")
                steps.append(f"    • Submatrix M[1,{j+1}]:")
                steps.append(_format_matrix(minor))
                steps.append(f"    • Minor det(M[1,{j+1}]) = {minor_det:.6g}")
                steps.append(f"    • Term value = {sign_str} ({entry:.4g}) × ({minor_det:.6g}) = {term_val:.6g}")

            steps.append(f"\n📌 Step 3: Sum Expansion Terms:")
            steps.append(f"  • det(A) = " + " + ".join(f"{t:.6g}" for t in terms) + f" = {det:.6g}")

        else:
            steps.append(f"\n📌 Step 2: {n}×{n} Matrix Determinant via LU Decomposition")
            steps.append(f"  • det(A) = {det:.6g}")
            rank = int(np.linalg.matrix_rank(A))
            steps.append(f"  • Matrix Rank: rank(A) = {rank}")

        steps.append(f"\n📌 Step 3: Invertibility & Singularity Check")
        if abs(det) < 1e-10:
            steps.append("  • det(A) = 0 ➔ Matrix A is SINGULAR (Non-invertible).")
        else:
            steps.append(f"  • det(A) = {det:.6g} ≠ 0 ➔ Matrix A is NON-SINGULAR (Invertible).")

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


def _format_matrix(M):
    lines = []
    for row in M:
        formatted_row = "  ".join(f"{v:8.4g}" for v in row)
        lines.append(f"  [ {formatted_row} ]")
    return "\n".join(lines)
