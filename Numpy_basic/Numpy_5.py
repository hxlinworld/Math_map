import numpy as np

A = np.arange(3,15)
# print(A)
# print(A[3])
B = np.arange(1,13).reshape((3,4))
# print(B)
# print('B[2]=',B[2])
# print(B[1:,0])
# print(B)
# print(B.T)
for row in B.T:   # B转置得到的矩阵B.T的行row迭代-> 原先B矩阵的列column
   print(row) # -> 得到原来的列

print(B.flatten())
for item in B.flatten():
    print(item)

