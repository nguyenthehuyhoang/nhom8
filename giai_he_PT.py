#bài này giải hệ phương trình x+2y=5 và 3x+4y =6
# Yêu cầu hoàn chỉnh lại đoạn code
#để có 1 app giải hệ phương trình có n phương trình n ẩn
import numpy as np
A = np.array([(1,2),(3,4)])
B = np.array([5,6])
A1  = np.linalg.inv(A) # tạo ma trận nghich đảo
print(A)
print(B)
print(A1)
X = np.dot(A1,B)
print('Nghiem cua he:',X)
print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
print('bbbbbbbbbbbbbbbbbbbbbbb')
