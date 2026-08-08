import numpy as np

def solve_matrix(operation, matrix_a, matrix_b=None):
    """
    Perform a matrix operation with rich step-by-step detailed solutions.
    """
    try:
        A = np.array(matrix_a, dtype=float)
        rows_A, cols_A = A.shape
        steps = []

        if operation == "transpose":
            result = A.T.tolist()
            steps.append(f"📌 Step 1: Transpose Operation (Aᵀ)")
            steps.append(f"Input Matrix A ({rows_A}×{cols_A}):")
            steps.append(_format_matrix(A))
            steps.append(f"\n📌 Step 2: Swap rows and columns (Row i becomes Column i):")
            for i in range(rows_A):
                row_vals = ", ".join(f"{A[i, j]:.4g}" for j in range(cols_A))
                steps.append(f"  • Row {i+1} [{row_vals}] ➔ Column {i+1}")
            steps.append(f"\n✅ Final Transposed Matrix Aᵀ ({cols_A}×{rows_A}):")
            steps.append(_format_matrix(A.T))
            return {"result": result, "steps": "\n".join(steps)}

        if operation == "inverse":
            if rows_A != cols_A:
                return {"error": "Matrix must be square (n×n) to find its inverse."}
            
            det = float(np.linalg.det(A))
            steps.append(f"📌 Step 1: Calculate Determinant of Matrix A ({rows_A}×{cols_A})")
            steps.append(f"  • det(A) = {det:.6g}")
            
            if abs(det) < 1e-10:
                steps.append("\n❌ Determinant det(A) = 0.")
                steps.append("  • Since det(A) = 0, Matrix A is singular and HAS NO INVERSE.")
                return {"error": "Matrix is singular (det ≈ 0) — inverse does not exist.", "steps": "\n".join(steps)}

            steps.append("  • Since det(A) ≠ 0, the inverse A⁻¹ exists.")

            if rows_A == 2:
                a, b = A[0, 0], A[0, 1]
                c, d = A[1, 0], A[1, 1]
                inv_det = 1.0 / det
                adj = np.array([[d, -b], [-c, a]])
                inv_A = np.linalg.inv(A)

                steps.append(f"\n📌 Step 2: Use 2×2 Inverse Formula:")
                steps.append(f"  Formula: A⁻¹ = (1 / det(A)) × [ d  -b ]")
                steps.append(f"                                [ -c  a ]")
                steps.append(f"  • Swap diagonal elements (a={a:.4g}, d={d:.4g} ➔ d={d:.4g}, a={a:.4g})")
                steps.append(f"  • Negate off-diagonal elements (b={b:.4g} ➔ {-b:.4g}, c={c:.4g} ➔ {-c:.4g})")
                steps.append(f"\n📌 Step 3: Adjugate Matrix adj(A):")
                steps.append(_format_matrix(adj))
                steps.append(f"\n📌 Step 4: Multiply adj(A) by 1/det(A) = {inv_det:.6g}:")
                steps.append(_format_matrix(inv_A))

            else:
                inv_A = np.linalg.inv(A)
                steps.append(f"\n📌 Step 2: Compute Adjugate Matrix adj(A) via Cofactors")
                adj = (inv_A * det)
                steps.append(_format_matrix(adj))
                steps.append(f"\n📌 Step 3: Compute A⁻¹ = (1 / det(A)) × adj(A):")
                steps.append(_format_matrix(inv_A))

            result = np.round(inv_A, 6).tolist()
            return {"result": result, "steps": "\n".join(steps)}

        if operation == "determinant":
            if rows_A != cols_A:
                return {"error": "Matrix must be square to compute determinant."}
            det = float(np.linalg.det(A))
            steps.append(f"📌 Step 1: Input Matrix A ({rows_A}×{cols_A}):")
            steps.append(_format_matrix(A))
            steps.append(f"\n📌 Step 2: Determinant Calculation:")
            if rows_A == 2:
                a, b, c, d = A[0,0], A[0,1], A[1,0], A[1,1]
                steps.append(f"  Formula: det(A) = (a × d) - (b × c)")
                steps.append(f"  det(A) = ({a:.4g} × {d:.4g}) - ({b:.4g} × {c:.4g})")
                steps.append(f"         = {a*d:.4g} - {b*c:.4g} = {det:.6g}")
            else:
                steps.append(f"  det(A) = {det:.6g}")
            return {"result": [[round(det, 6)]], "steps": "\n".join(steps)}

        if operation == "rank":
            r = int(np.linalg.matrix_rank(A))
            steps.append(f"📌 Step 1: Input Matrix A ({rows_A}×{cols_A}):")
            steps.append(_format_matrix(A))
            steps.append(f"\n📌 Step 2: Gaussian Elimination to Row Echelon Form (RREF)")
            steps.append(f"  • Number of non-zero rows (linearly independent rows/cols) = {r}")
            steps.append(f"\n✅ Rank of Matrix A: rank(A) = {r}")
            return {"result": [[r]], "steps": "\n".join(steps)}

        if operation == "trace":
            if rows_A != cols_A:
                return {"error": "Matrix must be square to compute trace."}
            diag_vals = np.diag(A)
            t = float(np.trace(A))
            steps.append(f"📌 Step 1: Extract Main Diagonal Elements of A ({rows_A}×{cols_A}):")
            diag_str = " + ".join(f"{x:.4g}" for x in diag_vals)
            steps.append(f"  • Diagonal entries: {list(diag_vals)}")
            steps.append(f"\n📌 Step 2: Sum Diagonal Entries:")
            steps.append(f"  • trace(A) = {diag_str} = {t:.6g}")
            return {"result": [[round(t, 6)]], "steps": "\n".join(steps)}

        # Two matrix operations
        if matrix_b is None:
            return {"error": "Second matrix (B) is required for this operation."}

        B = np.array(matrix_b, dtype=float)
        rows_B, cols_B = B.shape

        if operation == "add":
            if A.shape != B.shape:
                return {"error": f"Dimension mismatch: A is {rows_A}×{cols_A}, B is {rows_B}×{cols_B}. Must be identical to add."}
            res_mat = A + B
            steps.append(f"📌 Step 1: Element-wise Addition (C = A + B):")
            for i in range(rows_A):
                for j in range(cols_A):
                    steps.append(f"  • C[{i+1},{j+1}] = A[{i+1},{j+1}] + B[{i+1},{j+1}] = {A[i,j]:.4g} + {B[i,j]:.4g} = {res_mat[i,j]:.4g}")
            steps.append(f"\n✅ Result Matrix C ({rows_A}×{cols_A}):")
            steps.append(_format_matrix(res_mat))
            return {"result": np.round(res_mat, 6).tolist(), "steps": "\n".join(steps)}

        if operation == "subtract":
            if A.shape != B.shape:
                return {"error": f"Dimension mismatch: A is {rows_A}×{cols_A}, B is {rows_B}×{cols_B}. Must be identical to subtract."}
            res_mat = A - B
            steps.append(f"📌 Step 1: Element-wise Subtraction (C = A - B):")
            for i in range(rows_A):
                for j in range(cols_A):
                    steps.append(f"  • C[{i+1},{j+1}] = A[{i+1},{j+1}] - B[{i+1},{j+1}] = {A[i,j]:.4g} - {B[i,j]:.4g} = {res_mat[i,j]:.4g}")
            steps.append(f"\n✅ Result Matrix C ({rows_A}×{cols_A}):")
            steps.append(_format_matrix(res_mat))
            return {"result": np.round(res_mat, 6).tolist(), "steps": "\n".join(steps)}

        if operation == "multiply":
            if cols_A != rows_B:
                return {"error": f"Cannot multiply: A columns ({cols_A}) must equal B rows ({rows_B})."}
            res_mat = A @ B
            steps.append(f"📌 Step 1: Check Matrix Multiplication Condition")
            steps.append(f"  • A ({rows_A}×{cols_A}) × B ({rows_B}×{cols_B}) ➔ Result C will be ({rows_A}×{cols_B})")
            steps.append(f"\n📌 Step 2: Compute Dot Product for each Entry C[i, j]:")
            for i in range(rows_A):
                for j in range(cols_B):
                    terms = [f"({A[i, k]:.4g} × {B[k, j]:.4g})" for k in range(cols_A)]
                    terms_str = " + ".join(terms)
                    steps.append(f"  • C[{i+1},{j+1}] = Row_{i+1}(A) · Col_{j+1}(B) = {terms_str} = {res_mat[i, j]:.4g}")
            steps.append(f"\n✅ Result Product Matrix C ({rows_A}×{cols_B}):")
            steps.append(_format_matrix(res_mat))
            return {"result": np.round(res_mat, 6).tolist(), "steps": "\n".join(steps)}

        return {"error": f"Unknown operation: {operation}"}

    except Exception as e:
        return {"error": str(e)}


def _format_matrix(M):
    """Utility to format numpy 2D array as text matrix block."""
    lines = []
    for row in M:
        formatted_row = "  ".join(f"{v:8.4g}" for v in row)
        lines.append(f"  [ {formatted_row} ]")
    return "\n".join(lines)
