def lu_decomposition(A):
    n = len(A)

    L = []      # สร้างเมทริกซ์ L เป็นเมทริกซ์เอกลักษณ์
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        L.append(row)

    U = []      # สร้างเมทริกซ์ U โดยคัดลอกเมทริกซ์ A
    for i in range(n):
        U.append(A[i][:])

    for i in range(n):
        for k in range(i + 1, n):
            factor = U[k][i] / U[i][i]      # หาตัวคูณเพื่อลบให้เป็น 0 ไปเก็บใน L
            L[k][i] = factor
            for j in range(i, n):
                U[k][j] -= factor * U[i][j] # row operation เพื่อลบให้เป็น 0

    return L, U


def solve_lu(L, U, b):
    if L is None or U is None:
        print("LU decomposition failed.")
        return None
    
    n = len(L)
    y = [0] * n
    x = [0] * n

    # Forward Substitution: หา y จาก Ly = b
    for i in range(n):
        sum = 0
        for j in range(i):
            sum += L[i][j] * y[j]       # บวกผลคูณ L กับ y ที่หาได้ก่อนหน้า
        y[i] = b[i] - sum               # หาค่า y โดยเอา b ลบผลรวมที่ได้
    
    # Backward Substitution: หา x จาก Ux = y
    for i in range(n - 1, -1, -1):      # วนแถวย้อนกลับล่างขึ้นบน
        sum = 0
        for j in range(i + 1, n):
            sum += U[i][j] * x[j]       # บวกผลคูณ U กับ x ที่หาได้ก่อนหน้า
        x[i] = (y[i] - sum) / U[i][i]   # หาค่า x โดยเอา y ลบผลรวมแล้วหารด้วย U ที่เส้นทแยงมุม
        
    return x


def answer(A, b):
    L, U = lu_decomposition(A)
    
    if L is None:
        print("Matrix decomposition failed.")
        return
    
    print("L Matrix:")
    for row in L:
        value = []
        for i in row:
            value.append(round(i, 2))
        print(value)
    print()
    print("U Matrix:")
    for row in U:
        value = []
        for i in row:
            value.append(round(i, 2))
        print(value)
    print()
    
    x = solve_lu(L, U, b)
    if x is not None:
        print("x:")
        for i in x:
            print([round(i, 2)])
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
