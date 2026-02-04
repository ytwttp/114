def identity_matrix(n):     # สร้างเมทริกซ์เอกลักษณ์
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)   # เติม 0 ให้ครบในแถว
        matrix.append(row)  # เอาแถวใส่ใน list matrix
    
    for i in range(n):
        matrix[i][i] = 1    # เปลี่ยนเส้นทแยงมุมให้เป็น 1
    return matrix


def inverse_matrix(A):      # หาอินเวอร์ส
    n = len(A)
    I = identity_matrix(n)
    M = []
    for i in range(n):
        M.append(A[i][:] + I[i])    # รวมเมทริกซ์ A กับ I

    # ใช้ gauss-jordan สลับให้ฝั่งซ้ายเป็นเอกลักษณ์
    for i in range(n):
        pivot = M[i][i]
        if pivot == 0:              # ถ้าเจอ 0 ในเส้นทแยงมุม แสดงว่าเมทริกซ์นี้ไม่มีอินเวอร์ส
            return None
            
        for j in range(2 * n):      # ทำให้ pivot เป็น 1
            M[i][j] /= pivot        # โดยหารด้วยตัวมันเองทั้งแถว
        
        for k in range(n):
            if k != i:                          # ข้ามแถวที่เป็น pivot
                factor = M[k][i]                # เลขใต้ pivot ที่ต้องทำให้เป็น 0
                # row operation
                for j in range(2 * n):          # ต้องทำ opearion ทั้งฝั่ง A และ I
                    M[k][j] += (-1 * factor) * M[i][j]    # ทำแถวที่จะแก้ด้วยการเอาลบของเลขที่จะแก้คูณกับแถว pivot แล้วบวกกลับเข้าไปเหมือนเดิม
    
    inverse = []
    for i in range(n):
        inverse.append(M[i][n:])    # เอาฝั่งขวาที่เป็นอินเวอร์สออกมา
    return inverse


def find_x(A_inv, b):       # หา x จาก A_inv * b
    if A_inv is None:
        print("No x exists.")
        return None         # ถ้าไม่มี A_inv ก็หาค่า x ไม่ได้
    
    n = len(A_inv)
    x = []
    for i in range(n):              # วนแถว
        sum = 0
        for j in range(n):          # วนคอลัมน์
            sum += A_inv[i][j] * b[j]   # วนคูณ A_inv ในแถว i ให้ครบทุกคอลัมน์กับ b ครบทุกแถว
        x.append(sum)
    return x


def answer(A, b=None):
    A_inv = inverse_matrix(A)
    
    if A_inv is None:
        print("Matrix is singular, no inverse.")
        return
    
    print("Inverse Matrix:")
    for row in A_inv:
        inverse = []
        for i in row:
            inverse.append(round(i, 2))
        print(inverse)
    
    if b is not None:
        x = find_x(A_inv, b)
        print("x:")
        for i in x:
            print([round(i, 2)])


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