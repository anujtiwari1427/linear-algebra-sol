import numpy as np

def solve_vector(operation, vec_a, vec_b=None, scalar=None):
    """
    Perform vector operations with detailed step-by-step mathematical solutions.
    """
    try:
        a = np.array(vec_a, dtype=float)
        dim_a = len(a)
        steps = []

        if operation == "magnitude":
            sq_terms = [f"({x:.4g})²" for x in vec_a]
            sq_vals = [x**2 for x in vec_a]
            sum_sq = sum(sq_vals)
            mag = float(np.linalg.norm(a))
            steps.append(f"📌 Step 1: Formula for Vector Magnitude |a|")
            steps.append(f"  • |a| = √(a₁² + a₂² + ... + aₙ²)")
            steps.append(f"\n📌 Step 2: Compute Component Squares:")
            steps.append(f"  • |a| = √(" + " + ".join(sq_terms) + ")")
            steps.append(f"  • |a| = √(" + " + ".join(f"{v:.4g}" for v in sq_vals) + ") = √(" + f"{sum_sq:.4g}" + ")")
            steps.append(f"\n✅ Final Magnitude: |a| = {mag:.6g}")
            return {"result": round(mag, 6), "steps": "\n".join(steps)}

        if operation == "normalize":
            mag = float(np.linalg.norm(a))
            if mag == 0:
                return {"error": "Cannot normalize a zero vector (magnitude is 0)."}
            norm_a = (a / mag).tolist()
            steps.append(f"📌 Step 1: Compute Vector Magnitude |a|")
            steps.append(f"  • |a| = {mag:.6g}")
            steps.append(f"\n📌 Step 2: Divide Each Component by Magnitude (u = a / |a|):")
            for i, val in enumerate(vec_a):
                steps.append(f"  • u_{i+1} = {val:.4g} / {mag:.4g} = {norm_a[i]:.6g}")
            steps.append(f"\n✅ Unit Vector u = {[round(x, 6) for x in norm_a]}")
            return {"result": [round(x, 6) for x in norm_a], "steps": "\n".join(steps)}

        if operation == "scalar_multiply":
            if scalar is None:
                return {"error": "Scalar value is required."}
            s = float(scalar)
            res = (s * a).tolist()
            steps.append(f"📌 Step 1: Multiply Each Component of Vector a by Scalar c = {s:.4g}")
            for i, val in enumerate(vec_a):
                steps.append(f"  • ({s:.4g}) × ({val:.4g}) = {res[i]:.6g}")
            steps.append(f"\n✅ Result Vector c·a = {[round(x, 6) for x in res]}")
            return {"result": [round(x, 6) for x in res], "steps": "\n".join(steps)}

        # Operations requiring vector B
        if vec_b is None:
            return {"error": "Second vector (b) is required for this operation."}

        b = np.array(vec_b, dtype=float)
        if len(a) != len(b):
            return {"error": f"Vector dimension mismatch: vector a has length {len(a)}, vector b has length {len(b)}."}

        if operation == "add":
            res = (a + b).tolist()
            steps.append(f"📌 Step 1: Add Corresponding Components (a + b):")
            for i in range(dim_a):
                steps.append(f"  • Component {i+1}: {a[i]:.4g} + {b[i]:.4g} = {res[i]:.6g}")
            steps.append(f"\n✅ Result Vector a + b = {[round(x, 6) for x in res]}")
            return {"result": [round(x, 6) for x in res], "steps": "\n".join(steps)}

        if operation == "subtract":
            res = (a - b).tolist()
            steps.append(f"📌 Step 1: Subtract Corresponding Components (a - b):")
            for i in range(dim_a):
                steps.append(f"  • Component {i+1}: {a[i]:.4g} - {b[i]:.4g} = {res[i]:.6g}")
            steps.append(f"\n✅ Result Vector a - b = {[round(x, 6) for x in res]}")
            return {"result": [round(x, 6) for x in res], "steps": "\n".join(steps)}

        if operation == "dot":
            terms = [f"({x:.4g} × {y:.4g})" for x, y in zip(vec_a, vec_b)]
            prods = [x * y for x, y in zip(vec_a, vec_b)]
            d = float(np.dot(a, b))
            steps.append(f"📌 Step 1: Formula for Dot Product (a · b)")
            steps.append(f"  • a · b = a₁b₁ + a₂b₂ + ... + aₙbₙ")
            steps.append(f"\n📌 Step 2: Component Products and Sum:")
            steps.append(f"  • a · b = " + " + ".join(terms))
            steps.append(f"  • a · b = " + " + ".join(f"{v:.4g}" for v in prods) + f" = {d:.6g}")
            steps.append(f"\n✅ Final Dot Product: a · b = {d:.6g}")
            return {"result": round(d, 6), "steps": "\n".join(steps)}

        if operation == "cross":
            if dim_a != 3 or len(b) != 3:
                return {"error": "Cross product (a × b) is strictly defined for 3D vectors (length 3)."}
            res = np.cross(a, b).tolist()
            ax, ay, az = a[0], a[1], a[2]
            bx, by, bz = b[0], b[1], b[2]
            cx = (ay * bz) - (az * by)
            cy = (az * bx) - (ax * bz)
            cz = (ax * by) - (ay * bx)
            steps.append(f"📌 Step 1: Cross Product Formula using 3×3 Determinant Expansion:")
            steps.append(f"  |  i   j   k  |")
            steps.append(f"  | {ax:4g} {ay:4g} {az:4g} |")
            steps.append(f"  | {bx:4g} {by:4g} {bz:4g} |")
            steps.append(f"\n📌 Step 2: Component Breakdown:")
            steps.append(f"  • i: (ay·bz - az·by) = ({ay:.4g}×{bz:.4g}) - ({az:.4g}×{by:.4g}) = {cx:.4g}")
            steps.append(f"  • j: (az·bx - ax·bz) = ({az:.4g}×{bx:.4g}) - ({ax:.4g}×{bz:.4g}) = {cy:.4g}")
            steps.append(f"  • k: (ax·by - ay·bx) = ({ax:.4g}×{by:.4g}) - ({ay:.4g}×{bx:.4g}) = {cz:.4g}")
            steps.append(f"\n✅ Result Cross Product Vector a × b = {[round(x, 6) for x in res]}")
            return {"result": [round(x, 6) for x in res], "steps": "\n".join(steps)}

        if operation == "angle":
            dot = float(np.dot(a, b))
            mag_a = float(np.linalg.norm(a))
            mag_b = float(np.linalg.norm(b))
            if mag_a == 0 or mag_b == 0:
                return {"error": "Cannot compute angle with a zero vector."}
            cos_theta = dot / (mag_a * mag_b)
            cos_theta = max(-1.0, min(1.0, cos_theta))
            angle_rad = float(np.arccos(cos_theta))
            angle_deg = float(np.degrees(angle_rad))

            steps.append(f"📌 Step 1: Compute Magnitudes & Dot Product")
            steps.append(f"  • |a| = {mag_a:.6g}")
            steps.append(f"  • |b| = {mag_b:.6g}")
            steps.append(f"  • a · b = {dot:.6g}")
            steps.append(f"\n📌 Step 2: Compute cos(θ)")
            steps.append(f"  • cos(θ) = (a · b) / (|a| × |b|) = {dot:.6g} / ({mag_a:.4g} × {mag_b:.4g}) = {cos_theta:.6g}")
            steps.append(f"\n📌 Step 3: Calculate Inverse Cosine arccos(cos(θ)):")
            steps.append(f"  • Angle in Radians: {angle_rad:.6g} rad")
            steps.append(f"  • Angle in Degrees: {angle_deg:.4g}°")
            return {"result": round(angle_deg, 4), "steps": "\n".join(steps)}

        if operation == "projection":
            mag_b_sq = float(np.dot(b, b))
            if mag_b_sq == 0:
                return {"error": "Cannot project onto a zero vector."}
            dot = float(np.dot(a, b))
            mag_b = float(np.linalg.norm(b))
            scalar_proj = dot / mag_b
            vector_proj = (dot / mag_b_sq) * b

            steps.append(f"📌 Step 1: Projection Formula: proj_b(a) = ((a · b) / |b|²) × b")
            steps.append(f"  • Dot Product a · b = {dot:.6g}")
            steps.append(f"  • Magnitude Squared |b|² = {mag_b_sq:.6g}")
            steps.append(f"  • Scalar Projection comp_b(a) = (a · b) / |b| = {scalar_proj:.6g}")
            steps.append(f"\n📌 Step 2: Multiply Vector b by Scale Factor (a · b) / |b|² = {dot/mag_b_sq:.6g}:")
            res_v = [round(float(x), 6) for x in vector_proj.tolist()]
            for i in range(dim_a):
                steps.append(f"  • Component {i+1}: ({dot/mag_b_sq:.4g}) × {b[i]:.4g} = {res_v[i]:.6g}")
            steps.append(f"\n✅ Vector Projection proj_b(a) = {res_v}")
            return {"result": res_v, "steps": "\n".join(steps)}

        return {"error": f"Unknown operation: {operation}"}

    except Exception as e:
        return {"error": str(e)}
