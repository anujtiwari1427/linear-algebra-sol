import numpy as np
import math

def solve_transform(transform_type, params, vector=None):
    """
    Build transformation matrix and provide detailed step-by-step mathematical solutions.
    """
    try:
        T = _build_matrix(transform_type, params)
        if T is None:
            return {"error": f"Unknown transform type: {transform_type}"}

        matrix_list = [[round(float(v), 6) for v in row] for row in T.tolist()]
        steps = _describe_detailed(transform_type, params, T, vector)

        result = {
            "transform_matrix": matrix_list,
            "steps": steps
        }

        if vector is not None:
            v = np.array(vector, dtype=float)
            if v.shape[0] != T.shape[1]:
                return {"error": f"Vector length ({v.shape[0]}) must match matrix columns ({T.shape[1]})."}
            tv = T @ v
            result["input_vector"] = [round(float(x), 6) for x in v.tolist()]
            result["output_vector"] = [round(float(x), 6) for x in tv.tolist()]

        return result

    except Exception as e:
        return {"error": str(e)}


def _build_matrix(t, p):
    deg = float(p.get("angle_deg", 0))
    rad = math.radians(deg)
    cos, sin = math.cos(rad), math.sin(rad)

    if t == "rotation_2d":
        return np.array([[cos, -sin],
                         [sin,  cos]])

    if t == "rotation_3d_x":
        return np.array([[1,   0,    0],
                         [0,  cos, -sin],
                         [0,  sin,  cos]])

    if t == "rotation_3d_y":
        return np.array([[ cos, 0, sin],
                         [  0,  1,   0],
                         [-sin, 0, cos]])

    if t == "rotation_3d_z":
        return np.array([[cos, -sin, 0],
                         [sin,  cos, 0],
                         [0,     0,  1]])

    if t == "scale":
        sx = float(p.get("sx", 1))
        sy = float(p.get("sy", 1))
        sz = p.get("sz", None)
        if sz is not None:
            return np.array([[sx, 0, 0],
                             [0, sy, 0],
                             [0,  0, float(sz)]])
        return np.array([[sx, 0],
                         [0, sy]])

    if t == "shear_x":
        k = float(p.get("shear", 0))
        return np.array([[1, k],
                         [0, 1]])

    if t == "shear_y":
        k = float(p.get("shear", 0))
        return np.array([[1, 0],
                         [k, 1]])

    if t == "reflect_x":
        return np.array([[1,  0],
                         [0, -1]])

    if t == "reflect_y":
        return np.array([[-1, 0],
                         [0,  1]])

    if t == "reflect_origin":
        return np.array([[-1, 0],
                         [0, -1]])

    if t == "project_x":
        return np.array([[1, 0],
                         [0, 0]])

    if t == "project_y":
        return np.array([[0, 0],
                         [0, 1]])

    if t == "custom":
        m = p.get("matrix", [[1, 0], [0, 1]])
        return np.array(m, dtype=float)

    return None


def _describe_detailed(t, p, T, vector=None):
    steps = []
    deg = float(p.get("angle_deg", 0))
    rad = math.radians(deg)
    det = float(np.linalg.det(T))

    steps.append(f"📌 Step 1: Transformation Matrix Construction ({T.shape[0]}×{T.shape[1]})")
    
    if "rotation" in t:
        steps.append(f"  • Angle θ = {deg}° ({rad:.4f} rad)")
        steps.append(f"  • cos({deg}°) = {math.cos(rad):.4g}, sin({deg}°) = {math.sin(rad):.4g}")

    steps.append(_format_matrix(T))

    steps.append(f"\n📌 Step 2: Determinant & Geometric Scale Factor")
    steps.append(f"  • det(T) = {det:.6g}")
    if abs(det) < 1e-10:
        steps.append("  • det = 0: Transformation collapses space into a lower dimension (Non-invertible).")
    elif abs(abs(det) - 1.0) < 1e-6:
        steps.append("  • det = ±1: Rigid transformation (preserves area / volume & distances).")
    else:
        steps.append(f"  • Area/Volume scaling factor is |det(T)| = {abs(det):.4g}.")

    if vector is not None:
        v = np.array(vector, dtype=float)
        tv = T @ v
        steps.append(f"\n📌 Step 3: Apply Transformation Matrix T to Vector v = {v.tolist()}")
        steps.append(f"  Matrix-Vector Product Equation T · v = v':")
        for i in range(T.shape[0]):
            terms = [f"({T[i,k]:.4g} × {v[k]:.4g})" for k in range(T.shape[1])]
            terms_str = " + ".join(terms)
            steps.append(f"  • v'[{i+1}] = {terms_str} = {tv[i]:.6g}")
        steps.append(f"\n✅ Transformed Output Vector v' = {[round(float(x), 6) for x in tv.tolist()]}")

    return "\n".join(steps)


def _format_matrix(M):
    lines = []
    for row in M:
        formatted_row = "  ".join(f"{v:8.4g}" for v in row)
        lines.append(f"  [ {formatted_row} ]")
    return "\n".join(lines)
