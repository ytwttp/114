def lu_decomposition(A, pivot=False):
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

    P = None    # สร้างเวกเตอร์มาสลับแถวถ้าเลือกใช้ pivot
    if pivot:
        P = []
        for i in range(n):
            P.append(i)

    for i in range(n):
        if pivot:               # สลับแถวเอาเลขมากสุดมาหาร
            max_row = i
            for k in range(i + 1, n):
                if abs(U[k][i]) > abs(U[max_row][i]):
                    max_row = k

            if i != max_row:
                U[i], U[max_row] = U[max_row], U[i]     # สลับแถวใน U
                P[i], P[max_row] = P[max_row], P[i]     # สลับแถวใน P
                for j in range(i):
                    L[i][j], L[max_row][j] = L[max_row][j], L[i][j] # สลับแถวใน L ที่อยู่ก่อนหน้า

        if abs(U[i][i]) < 1e-10:    # เช็คว่าตัวหารเป็น 0 ในเส้นทแยงมุมมั้ย
            return None, None, None # ถ้าใช่ = แก้สมการไม่ได้ คืนค่า None ทั้งสามตัว
        
        for k in range(i + 1, n):
            factor = U[k][i] / U[i][i]      # หาตัวคูณเพื่อลบให้เป็น 0 ไปเก็บใน L
            L[k][i] = factor
            for j in range(i, n):
                U[k][j] -= factor * U[i][j] # row operation เพื่อลบให้เป็น 0

    return L, U, P


def solve_lu(L, U, b, P=None):
    if L is None or U is None:
        print("LU decomposition failed.")
        return None
    
    n = len(L)

    if P is not None:
        b_permuted = []     # สร้าง b ที่ถูกสลับแถวตาม P
        for i in range(n):
            b_permuted.append(b[P[i]])  # เอา b แถวที่ถูกสลับมาใส่
    else:
        b_permuted = b[:]   # ไม่สลับ = ใช้ b เดิม
    
    y = [0] * n
    x = [0] * n

    # Forward Substitution: หา y จาก Ly = b
    for i in range(n):
        sum = 0
        for j in range(i):
            sum += L[i][j] * y[j]       # บวกผลคูณ L กับ y ที่หาได้ก่อนหน้า
        y[i] = b_permuted[i] - sum      # หาค่า y โดยเอา b ลบผลรวมที่ได้
    
    # Backward Substitution: หา x จาก Ux = y
    for i in range(n - 1, -1, -1):      # วนแถวย้อนกลับล่างขึ้นบน
        sum = 0
        for j in range(i + 1, n):
            sum += U[i][j] * x[j]       # บวกผลคูณ U กับ x ที่หาได้ก่อนหน้า
        x[i] = (y[i] - sum) / U[i][i]   # หาค่า x โดยเอา y ลบผลรวมแล้วหารด้วย U ที่เส้นทแยงมุม
        
    return x


def answer(A, b, pivot=False):
    L, U, P = lu_decomposition(A, pivot=pivot)
    
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

    if P is not None:
        print("Permutation Vector P:", P)
        print()
    
    x = solve_lu(L, U, b, P)
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