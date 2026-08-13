"""
2D Matrix Multiplication Program
This module provides functions to multiply two 2D matrices.
"""

def matrix_multiply(matrix_a, matrix_b):
    """
    Multiply two 2D matrices.
    
    Args:
        matrix_a: First matrix (list of lists)
        matrix_b: Second matrix (list of lists)
    
    Returns:
        The product matrix (list of lists)
    
    Raises:
        ValueError: If matrices cannot be multiplied (incompatible dimensions)
    """
    # Get dimensions of matrices
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0]) if matrix_a else 0
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0]) if matrix_b else 0
    
    # Check if multiplication is possible
    if cols_a != rows_b:
        raise ValueError(
            f"Cannot multiply matrices: Matrix A has {cols_a} columns "
            f"but Matrix B has {rows_b} rows"
        )
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    # Perform multiplication
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    
    return result


def print_matrix(matrix, name="Matrix"):
    """
    Print a matrix in a readable format.
    
    Args:
        matrix: The matrix to print (list of lists)
        name: Name label for the matrix
    """
    print(f"\n{name}:")
    for row in matrix:
        print([f"{val:6.2f}" if isinstance(val, float) else f"{val:6}" for val in row])


def main():
    """
    Main function to demonstrate matrix multiplication.
    """
    # Example 1: Simple 2x3 and 3x2 matrices
    print("=" * 50)
    print("Example 1: 2x3 multiplied by 3x2")
    print("=" * 50)
    
    matrix_a = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    
    matrix_b = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]
    
    print_matrix(matrix_a, "Matrix A (2x3)")
    print_matrix(matrix_b, "Matrix B (3x2)")
    
    result = matrix_multiply(matrix_a, matrix_b)
    print_matrix(result, "Result (2x2)")
    
    # Example 2: 3x3 matrices
    print("\n" + "=" * 50)
    print("Example 2: 3x3 multiplied by 3x3")
    print("=" * 50)
    
    matrix_c = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    matrix_d = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    
    print_matrix(matrix_c, "Matrix C (3x3)")
    print_matrix(matrix_d, "Matrix D (3x3)")
    
    result = matrix_multiply(matrix_c, matrix_d)
    print_matrix(result, "Result (3x3)")
    
    # Example 3: Error handling
    print("\n" + "=" * 50)
    print("Example 3: Error handling (incompatible matrices)")
    print("=" * 50)
    
    matrix_e = [[1, 2], [3, 4]]  # 2x2
    matrix_f = [[5, 6, 7], [8, 9, 10], [11, 12, 13]]  # 3x3
    
    try:
        result = matrix_multiply(matrix_e, matrix_f)
    except ValueError as e:
        print(f"Error caught: {e}")


if __name__ == "__main__":
    main()
