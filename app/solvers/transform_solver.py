import numpy as np
import math


def solve_transform(transform_type, params, vector=None):
    """
    Build a transformation matrix and optionally apply it to a vector/point.

    transform_type: rotation_2d | rotation_3d_x | rotation_3d_y | rotation_3d_z |
                    scale | shear_x | shear_y | reflect_x | reflect_y |
                    reflect_origin | project_x | project_y | custom
    params: dict of parameters (angle_deg, sx, sy, sz, shear, matrix)
    vector: list of numbers to transform (optional)
    """
    try:
        T = _build_matrix(transform_type, params)
        if T is None:
            return {"error": f"Unknown transform type: {transform_type}"}

        matrix_list = [[round(float(v), 6) for v in row] for row in T.tolist()]
        result = {
            "transform_matrix": matrix_list,
            "steps": _describe(transform_type, params, T)
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


def _describe(t, p, T):
    deg = p.get("angle_deg", 0)
    lines = []
    labels = {
        "rotation_2d":   f"2D rotation by {deg}°",
        "rotation_3d_x": f"3D rotation around X-axis by {deg}°",
        "rotation_3d_y": f"3D rotation around Y-axis by {deg}°",
        "rotation_3d_z": f"3D rotation around Z-axis by {deg}°",
        "scale":         f"Scale: sx={p.get('sx',1)}, sy={p.get('sy',1)}" + (f", sz={p.get('sz','')}" if p.get("sz") else ""),
        "shear_x":       f"Horizontal shear (k={p.get('shear',0)}): x' = x + k·y",
        "shear_y":       f"Vertical shear (k={p.get('shear',0)}): y' = k·x + y",
        "reflect_x":     "Reflection across X-axis: y → −y",
        "reflect_y":     "Reflection across Y-axis: x → −x",
        "reflect_origin":"Reflection through origin: (x,y) → (−x,−y)",
        "project_x":     "Orthogonal projection onto X-axis: y → 0",
        "project_y":     "Orthogonal projection onto Y-axis: x → 0",
        "custom":        "Custom transformation matrix",
    }
    lines.append(labels.get(t, t))
    det = round(float(np.linalg.det(T)), 6)
    lines.append(f"det(T) = {det}  (scale factor of the transformation)")
    if abs(det) < 1e-10:
        lines.append("det = 0: this transform collapses space (not invertible).")
    elif abs(abs(det) - 1) < 1e-6:
        lines.append("det = ±1: this is a rigid/orthogonal transform (preserves lengths).")
    return "\n".join(lines)
