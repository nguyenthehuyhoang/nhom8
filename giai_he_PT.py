#bài này giải hệ phương trình x+2y=5 và 3x+4y =6
# Yêu cầu hoàn chỉnh lại đoạn code
#để có 1 app giải hệ phương trình có n phương trình n ẩn

import numpy as np

def solve_linear_equations(nhapsopt, an):
    try:
        A = np.array(nhapsopt)# biểu diễn các hệ số ẩn thành ma trận
        B = np.array(an)# biểu diễn các hệ số tự do thành ma trận
        A_inv = np.linalg.inv(A)##  tính ma trận nghịch đảo của ma trận A
        X = np.dot(A_inv, B)#  tính tích của ma trận nghịch đảo A_inv và ma trận B
        return X
    except np.linalg.LinAlgError: ## nếu ma trận không thể nghịch đảo
        return None

def main():
    nhapsopt = None
    while nhapsopt is None:
        try:
            nhapsopt = int(input("Nhập số lượng phương trình: "))
            if nhapsopt <= 0:
                print("Số lượng phương trình phải lớn hơn 0. Vui lòng nhập lại.")
                nhapsopt = None
        except ValueError:
            print("Giá trị không hợp lệ. Vui lòng nhập lại.")
    an = None
    while an is None:
        try:
            an = int(input("Nhập số lượng ẩn: "))
            if an <= 0:
                print("Số lượng phương trình phải lớn hơn 0. Vui lòng nhập lại.")
                an = None
        except ValueError:
            print("Giá trị không hợp lệ. Vui lòng nhập lại.")


    hesoan_matrix = []
    hesotudo_matrix = []

    print("Nhập hệ số các phương trình:")
    for i in range(nhapsopt):
        matrix_tam = []
        for j in range(an):
            hesoan = None
            while hesoan is None:
                try:
                    hesoan = float(input(f"Nhập hệ số của ẩn x{j+1} trong phương trình {i+1}: "))
                    if hesoan <= 0:
                        print("Số lượng phương trình phải lớn hơn 0. Vui lòng nhập lại.")
                        hesoan = None
                except ValueError:
                    print("Giá trị không hợp lệ. Vui lòng nhập lại.")


            matrix_tam.append(hesoan)
        hesoan_matrix.append(matrix_tam)
        hesotudo = None
        while hesotudo is None:
            try:
                hesotudo = float(input(f"Nhập hệ số tự do trong phương trình {i + 1}: "))
                if hesoan <= 0:
                    print("Số lượng phương trình phải lớn hơn 0. Vui lòng nhập lại.")
                    hesotudo = None
            except ValueError:
                print("Giá trị không hợp lệ. Vui lòng nhập lại.")


        hesotudo_matrix.append(hesotudo)

    nghiem= solve_linear_equations(hesoan_matrix, hesotudo)

    if nghiem is not None:
        print("Nghiệm của hệ phương trình:")
        for i, value in enumerate(nghiem):
            print(f"x{i+1} = {value}")
    else:
        print("Hệ phương trình vô nghiệm hoặc vô số nghiệm.")

if __name__ == "__main__":
    main()

