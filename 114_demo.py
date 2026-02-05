# ปัดค่าและตัดค่าใกล้ศูนย์
def clean_and_round(x, eps=1e-9, digits=4):
    if abs(x) < eps:
        return 0.0
    return round(x, digits)


# รับค่าระบบสมการจากผู้ใช้
def input_system():
    n = int(input("ป้อนจำนวนตัวแปร : "))

    A = []
    for i in range(n):
        row = list(
            map(float, input(f"แถวที่ {i+1}: ").split())
        )  # รับค่าสัมประสิทธิ์มาทีละบรรทัด [[1,2,3],[2,3,4]]
        A.append(row)  # [[1,2,3],[2,3,4],[4,5,6]]

    print("\nป้อนเวกเตอร์ b : ")
    b = list(map(float, input().split()))  # รับค่าคำตอบแต่ละสมการ

    return A, b


# Gauss Elimination with Pivoting
def gauss_elimination_Pivoting(A, b, eps=1e-10):
    n = len(A)  # จำนวนแถว
    M = [A[i] + [b[i]] for i in range(n)]

    # ทำให้ตัวเลขด้านล่างเส้นทแยงมุมเป็น 0
    for col in range(n):
        # Partial Pivoting
        pivot_row = max(range(col, n), key=lambda r: abs(M[r][col]))
        if abs(M[pivot_row][col]) < eps:
            continue

        # สลับแถว
        M[col], M[pivot_row] = M[pivot_row], M[col]

        # ทำแถวที่มีค่ามากสุดหารตัวมากสุดเพื่อหาคำตอบง่ายๆ
        pivot = M[col][col]
        for j in range(col, n + 1):
            M[col][j] /= pivot

        # Eliminate rows below
        for row in range(col + 1, n):  # เลือกแถวล่างทีละแถว
            factor = M[row][col]  # ไล่แถวใต้ pivot
            for j in range(col, n + 1):  # แก้ทุกคอลัมน์ของแถวนั้น
                M[row][j] -= factor * M[col][j]  # แถวล่าง=แถวล่าง−(factor)×แถว pivot

    # Back Substitution
    x = [0.0] * n
    for i in range(n - 1, -1, -1):  # ไล่จากแถวล่าง
        if abs(M[i][i]) < eps:  # เช็คเลขทแยงมุมว่าเป็น0ไหม
            if abs(M[i][-1]) > eps:
                print("No solution")
                return None
            else:
                print("Infinite solutions")
                return None
        x[i] = (M[i][-1] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][
            i
        ]  # หาค่า x แต่ละตัว

    return x


# 2. Gauss–Jordan Elimination
def gauss_jordan(A, b, eps=1e-10):
    n = len(A)
    M = [A[i] + [b[i]] for i in range(n)]

    row = 0
    for col in range(n):
        pivot_row = max(range(row, n), key=lambda r: abs(M[r][col]))
        if abs(M[pivot_row][col]) < eps:
            continue

        # สลับแถว
        M[row], M[pivot_row] = M[pivot_row], M[row]

        # Normalize pivot row
        pivot = M[row][col]
        for j in range(col, n + 1):
            M[row][j] /= pivot

        # ทำให้เป็น 0 ทั้งบนและล่าง
        for r in range(n):
            if r != row:  # กันไม่ให้เลขทะแยงเปลี่ยนค่า
                factor = M[r][col]
                for j in range(col, n + 1):
                    M[r][j] -= factor * M[row][j]

        row += 1

    # หา x แต่ละตัว
    x = [0.0] * n
    for i in range(n):
        if all(abs(M[i][j]) < eps for j in range(n)):  # เช็กว่ามี 0 หมดไหม
            if abs(M[i][-1]) > eps:
                print("ไม่มีคำตอบ")
                return None
            else:
                print("คำตอบไม่จำกัด")
                return None
        x[i] = M[i][-1]

    return x


# ===============================
# Main Program
# ===============================
print("เลือกวิธีการแก้ระบบสมการ")
print("1. Gauss Elimination with Pivoting")
print("2. Gauss Jordan Elimination")

choice = int(input("เลือก (1 หรือ 2): "))

A, b = input_system()

if choice == 1:
    solution = gauss_elimination_Pivoting(A, b)
elif choice == 2:
    solution = gauss_jordan(A, b)
else:
    print("เลือกวิธีไม่ถูกต้อง")
    solution = None

# แสดงผล + ปัดตัวเลข
if solution is not None:
    print("\nคำตอบของระบบสมการ:")
    for i, val in enumerate(solution):
        val = clean_and_round(val)
        print(f"x{i+1} = {val}")
