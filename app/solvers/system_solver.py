import numpy as np


def solve_system(A_data, b_data):
    """
    Solve the linear system Ax = b.
    Returns dict with 'result' or 'error'.
    """
    try:
        A = np.array(A_data, dtype=float)
        b = np.array(b_data, dtype=float)

        rows, cols = A.shape
        if len(b) != rows:
            return {"error": f"b must have {rows} entries to match A rows."}

        rank_A = np.linalg.matrix_rank(A)
        aug = np.column_stack([A, b])
        rank_aug = np.linalg.matrix_rank(aug)

        steps = []
        steps.append(f"A is {rows}×{cols}, rank(A) = {rank_A}, rank([A|b]) = {rank_aug}")

        if rank_A != rank_aug:
            return {"error": "No solution — system is inconsistent (rank(A) ≠ rank([A|b]))."}

        if rank_A < cols:
            steps.append("Infinitely many solutions — system is underdetermined.")
            # Use least-norm solution
            x, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
            steps.append("Showing least-norm solution:")
            return {"result": [round(float(v), 6) for v in x], "steps": "\n".join(steps)}

        x = np.linalg.solve(A, b)
        steps.append("Unique solution found.")
        return {"result": [round(float(v), 6) for v in x], "steps": "\n".join(steps)}

    except Exception as e:
        return {"error": str(e)}
