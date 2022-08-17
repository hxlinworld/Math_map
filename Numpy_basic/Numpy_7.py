import numpy as np

A = np.arange(12).reshape(3,4)
print(A)

# print(np.split(A,2,axis=1))
# print(np.array_split(A,3,axis=1))
print(np.vsplit(A,3))  # 纵向分割 ->切割行
print(np.hsplit(A,2))  # 横向分割 ->切割列