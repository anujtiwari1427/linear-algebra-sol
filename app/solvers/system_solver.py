import numpy as np

def solve_system(A_data, b_data):
    """
    Solve linear system Ax = b with comprehensive step-by-step Gaussian Elimination solutions.
    """
    try:
        A = np.array(A_data, dtype=float)
        b = np.array(b_data, dtype=float)

        rows, cols = A.shape
        if len(b) != rows:
            return {"error": f"Vector b length ({len(b)}) does not match rows of matrix A ({rows})."}

        steps = []
        steps.append(f"📌 Step 1: Form Augmented Matrix [A | b] ({rows}×{cols+1}):")
        aug = np.column_stack([A, b])
        steps.append(_format_augmented(aug))

        # Check Rouché-Capelli
        rank_A = int(np.linalg.matrix_rank(A))
        rank_aug = int(np.linalg.matrix_rank(aug))

        steps.append(f"\n📌 Step 2: Check System Consistency (Rouché-Capelli Theorem)")
        steps.append(f"  • Rank of Coefficient Matrix rank(A) = {rank_A}")
        steps.append(f"  • Rank of Augmented Matrix rank([A|b]) = {rank_aug}")
        steps.append(f"  • Number of Variables n = {cols}")

        if rank_A != rank_aug:
            steps.append("\n❌ System is INCONSISTENT (rank(A) ≠ rank([A|b])).")
            steps.append("  • Conclusion: NO SOLUTION EXISTS.")
            return {"error": "No solution — system is inconsistent (rank(A) ≠ rank([A|b])).", "steps": "\n".join(steps)}

        if rank_A < cols:
            free_vars = cols - rank_A
            steps.append(f"\n⚠️ System has INFINITELY MANY SOLUTIONS ({free_vars} free variable(s)).")
            steps.append("  • Showing Minimum Norm (Least Squares) Solution:")
            x, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
            res_vals = [round(float(v), 6) for v in x]
            for i, val in enumerate(res_vals):
                steps.append(f"  • x_{i+1} ≈ {val}")
            return {"result": res_vals, "steps": "\n".join(steps)}

        # Perform step-by-step Forward Elimination (Gauss-Jordan)
        steps.append(f"\n📌 Step 3: Forward Elimination to Row Echelon Form")
        M = aug.copy()
        
        for i in range(rows):
            # Pivot selection
            pivot = M[i, i]
            if abs(pivot) < 1e-10:
                # Find non-zero row below to swap
                for k in range(i + 1, rows):
                    if abs(M[k, i]) > 1e-10:
                        M[[i, k]] = M[[k, i]]
                        steps.append(f"  • Swap Row {i+1} ↔ Row {k+1} for pivot.")
                        pivot = M[i, i]
                        break
            
            if abs(pivot) > 1e-10:
                # Normalize pivot row
                M[i] = M[i] / pivot
                steps.append(f"  • Row_{i+1} = Row_{i+1} / {pivot:.4g}:")
                steps.append(_format_augmented(M))
                
                # Eliminate below and above for RREF
                for j in range(rows):
                    if j != i:
                        factor = M[j, i]
                        if abs(factor) > 1e-10:
                            M[j] = M[j] - factor * M[i]
                            steps.append(f"  • Row_{j+1} = Row_{j+1} - ({factor:.4g}) × Row_{i+1}")

        steps.append(f"\n📌 Step 4: Reduced Row Echelon Form [I | x]:")
        steps.append(_format_augmented(M))

        x_sol = M[:, -1]
        res_vals = [round(float(v), 6) for v in x_sol]

        steps.append(f"\n✅ Final Solution:")
        for i, val in enumerate(res_vals):
            steps.append(f"  • x_{i+1} = {val}")

        return {"result": res_vals, "steps": "\n".join(steps)}

    except Exception as e:
        return {"error": str(e)}


def _format_augmented(M):
    lines = []
    rows, cols = M.shape
    for row in M:
        coeff_part = "  ".join(f"{v:8.4g}" for v in row[:-1])
        const_part = f"{row[-1]:8.4g}"
        lines.append(f"  [ {coeff_part}  |  {const_part} ]")
    return "\n".join(lines)
