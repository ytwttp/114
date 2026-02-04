def identity_matrix(n):
    """Creates an n x n identity matrix."""
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

def inverse_matrix(A):
    """Simple matrix inverse using Gauss-Jordan elimination."""
    n = len(A)
    
    # Create augmented matrix [A | I]
    I = identity_matrix(n)
    M = [A[i][:] + I[i] for i in range(n)]
    
    # Gauss-Jordan elimination
    for i in range(n):
        # Make diagonal element 1
        pivot = M[i][i]
        if pivot == 0:
            return None
            
        for j in range(2 * n):
            M[i][j] /= pivot
        
        # Make other elements in column 0
        for k in range(n):
            if k != i:
                factor = M[k][i]
                for j in range(2 * n):
                    M[k][j] -= factor * M[i][j]
    
    # Extract inverse from right half
    return [M[i][n:] for i in range(n)]


def find_x(A_inv, b):
    """Solves Ax = b using the inverse of A."""
    if A_inv is None:
        print("No x exists.")
        return None
    
    n = len(A_inv)
    x = [sum(A_inv[i][j] * b[j] for j in range(n)) for i in range(n)]
    return x


def answer(A, b=None):
    """Compute inverse and optionally solve Ax = b."""
    A_inv = inverse_matrix(A)
    
    if A_inv is None:
        print("Matrix is singular, no inverse.")
        return
    
    print("Inverse Matrix:")
    for row in A_inv:
        print([round(x, 2) for x in row])
    
    if b is not None:
        x = find_x(A_inv, b)
        print("x:")
        for val in x:
            print([round(val, 2)])


A_test1 = [[1, 2, -3], 
     [-1, 1, -1],
     [0, -2, 3]]

A_test2 = [[1, 2, 3],
           [-1, -1, -1],
           [1, 2, 3]]
b_test2 = [5, 3, -1]

answer(A_test1)
print()
answer(A_test2, b_test2)