"""
matrix_3d_multiply.py

Utilities for multiplying 3D matrices (a stack/batch of 2D matrices).

Functions:
- multiply_3d_python(A, B): pure-Python implementation. Expects A shape (k, n, p), B shape (k, p, m).
- multiply_3d_numpy(A, B): NumPy implementation; supports broadcasting similar to np.matmul.

Example usage in `__main__` demonstrates both functions.

Author: GitHub Copilot on behalf of gracytheresa
"""
from typing import List


def multiply_3d_python(A: List[List[List[float]]], B: List[List[List[float]]]) -> List[List[List[float]]]:
    """Multiply two 3D matrices (lists) as batches of 2D matrices.

    A: shape (k, n, p)
    B: shape (k, p, m)
    Returns: C of shape (k, n, m)

    This is a straightforward triple-nested implementation and is not optimized for large inputs.
    """
    # Basic validation
    if not isinstance(A, list) or not isinstance(B, list):
        raise TypeError("A and B must be lists (3D lists representing batches of matrices)")
    if len(A) != len(B):
        raise ValueError("Batch size (first dimension) must match for A and B")

    k = len(A)
    C = []
    for batch in range(k):
        a = A[batch]
        b = B[batch]
        if not a or not b:
            raise ValueError("Inner matrices must not be empty")
        n = len(a)
        p = len(a[0])
        if any(len(row) != p for row in a):
            raise ValueError("All rows in A[batch] must have the same length")
        if any(len(row) != len(b[0]) for row in b):
            raise ValueError("All rows in B[batch] must have the same length")
        if len(b) != p:
            raise ValueError("Inner dimensions must match: A[batch] is (n x p) and B[batch] must be (p x m)")
        m = len(b[0])

        # initialize result matrix for this batch
        c = [[0.0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                s = 0.0
                for r in range(p):
                    s += a[i][r] * b[r][j]
                c[i][j] = s
        C.append(c)
    return C


def multiply_3d_numpy(A, B):
    """Multiply two 3D matrices using NumPy.

    A and B can be numpy arrays or array-like. Recommended shapes:
    - (k, n, p) and (k, p, m) -> result (k, n, m)

    This also supports broadcasting for leading dimensions like np.matmul.
    """
    try:
        import numpy as np
    except ImportError as exc:
        raise ImportError("NumPy is required for multiply_3d_numpy") from exc

    a = np.array(A)
    b = np.array(B)
    # Use matmul which handles stacks of matrices
    return np.matmul(a, b)


if __name__ == "__main__":
    # Example: multiply two batches of 2x2 matrices (k=2)
    A_batch = [
        [[1, 2], [3, 4]],  # batch 0
        [[2, 0], [1, 2]],  # batch 1
    ]
    B_batch = [
        [[5, 6], [7, 8]],
        [[1, 1], [0, 1]],
    ]

    print("Pure-Python batch multiply:")
    C = multiply_3d_python(A_batch, B_batch)
    for idx, mat in enumerate(C):
        print(f"Batch {idx} result:")
        for row in mat:
            print(row)

    # If NumPy is available, demonstrate it
    try:
        import numpy as np

        print("\nNumPy batch multiply:")
        a = np.array(A_batch)
        b = np.array(B_batch)
        c = multiply_3d_numpy(a, b)
        for idx, mat in enumerate(c):
            print(f"Batch {idx} result:")
            print(mat)
    except ImportError:
        print("NumPy not installed; skipping NumPy demonstration.")
