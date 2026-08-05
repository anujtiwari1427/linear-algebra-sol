import numpy as np


def solve_vector(operation, vec_a, vec_b=None, scalar=None):
    """
    Perform a vector operation.
    Returns dict with 'result' or 'error'.
    """
    try:
        a = np.array(vec_a, dtype=float)

        if operation == "magnitude":
            mag = float(np.linalg.norm(a))
            return {"result": round(mag, 6), "steps": f"|a| = sqrt({' + '.join(f'{x}²' for x in vec_a)}) = {mag:.6f}"}

        if operation == "normalize":
            mag = np.linalg.norm(a)
            if mag == 0:
                return {"error": "Cannot normalize a zero vector."}
            result = (a / mag).tolist()
            return {"result": result, "steps": f"Unit vector = a / |a| = a / {mag:.4f}"}

        if operation == "scalar_multiply":
            if scalar is None:
                return {"error": "Scalar value is required."}
            result = (float(scalar) * a).tolist()
            return {"result": result, "steps": f"{scalar} × a"}

        if vec_b is None:
            return {"error": "Second vector (b) is required for this operation."}

        b = np.array(vec_b, dtype=float)

        if len(a) != len(b):
            return {"error": "Vectors must have the same length."}

        if operation == "add":
            result = (a + b).tolist()
            return {"result": result, "steps": "a + b: add corresponding components."}

        if operation == "subtract":
            result = (a - b).tolist()
            return {"result": result, "steps": "a - b: subtract corresponding components."}

        if operation == "dot":
            d = float(np.dot(a, b))
            return {"result": round(d, 6), "steps": f"a · b = {' + '.join(f'{x}×{y}' for x, y in zip(vec_a, vec_b))} = {d:.6f}"}

        if operation == "cross":
            if len(a) != 3 or len(b) != 3:
                return {"error": "Cross product requires 3D vectors."}
            result = np.cross(a, b).tolist()
            return {"result": result, "steps": "a × b (cross product of two 3D vectors)"}

        if operation == "angle":
            dot = np.dot(a, b)
            mag_a = np.linalg.norm(a)
            mag_b = np.linalg.norm(b)
            if mag_a == 0 or mag_b == 0:
                return {"error": "Cannot compute angle with a zero vector."}
            cos_theta = dot / (mag_a * mag_b)
            cos_theta = max(-1, min(1, cos_theta))
            angle_rad = np.arccos(cos_theta)
            angle_deg = float(np.degrees(angle_rad))
            return {"result": round(angle_deg, 4), "steps": f"θ = arccos(a·b / |a||b|) = {angle_deg:.4f}°"}

        if operation == "projection":
            mag_b_sq = np.dot(b, b)
            if mag_b_sq == 0:
                return {"error": "Cannot project onto a zero vector."}
            scalar_proj = np.dot(a, b) / np.linalg.norm(b)
            vector_proj = (np.dot(a, b) / mag_b_sq) * b
            return {
                "result": [round(x, 6) for x in vector_proj.tolist()],
                "steps": f"proj_b(a) = (a·b / |b|²) × b, scalar projection = {scalar_proj:.4f}"
            }

        return {"error": f"Unknown operation: {operation}"}

    except Exception as e:
        return {"error": str(e)}
