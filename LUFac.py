def lu_decomposition(A, pivot=False):
    """Performs LU Decomposition of matrix A (assumes no pivoting needed)."""
    n = len(A)
    L = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    U = [A[i][:] for i in range(n)]
    P = list(range(n)) if pivot else None # Permutation vector

    for i in range(n):
        # Optional partial pivoting
        if pivot:
            max_row = max(range(i, n), key=lambda k: abs(U[k][i]))
            if i != max_row:
                U[i], U[max_row] = U[max_row], U[i]
                P[i], P[max_row] = P[max_row], P[i]
                for j in range(i):
                    L[i][j], L[max_row][j] = L[max_row][j], L[i][j]

        # Check for zero pivot
        if abs(U[i][i]) < 1e-10:
            return None, None, None
        
        # Eliminate entries below diagonal
        for k in range(i + 1, n):
            factor = U[k][i] / U[i][i]
            L[k][i] = factor
            for j in range(i, n):
                U[k][j] -= factor * U[i][j]

    return L, U, P

def solve_lu(L, U, b, P=None):
    """Solves Ax = b using LU decomposition."""
    if L is None or U is None:
        print("LU decomposition failed.")
        return None
    
    n = len(L)

    # Forward substitution: Ly = b
    if P is not None:
        b_permuted = [b[P[i]] for i in range(n)]
    else:
        b_permuted = b[:]
    
    y = [0.0] * n
    x = [0.0] * n

    # Forward substitution: Ly = b
    for i in range(n):
        y[i] = b_permuted[i] - sum(L[i][j] * y[j] for j in range(i))
    # Backward substitution: Ux = y
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]
        
    return x

def answer(A, b, pivot=False):
    """Solve Ax = b using LU decomposition."""
    L, U, P = lu_decomposition(A, pivot=pivot)
    
    if L is None:
        print("Matrix decomposition failed.")
        return
    
    print("L Matrix:")
    for row in L:
        print([round(x, 2) for x in row])
    print()
    print("U Matrix:")
    for row in U:
        print([round(x, 2) for x in row])
    print()

    if P is not None:
        print("Permutation Vector P:", P)
        print()
    
    x = solve_lu(L, U, b, P)
    if x is not None:
        print("x:")
        for val in x:
            print([round(val, 2)])
        print()


A_test1 = [[2., 1., 3.], 
           [4., 3., 5.], 
           [6., 5., 5.]]
b_test1 = [1., 1., -3.]

A_test2 = [[2., -1., -3., 1.],
           [1., 1., 1., -2.], 
           [3., 2., -3., -4.], 
           [-1., -4., 1., 1.]]
b_test2 = [9., 10., 6., 6.]

answer(A_test1, b_test1)
print()
answer(A_test2, b_test2)