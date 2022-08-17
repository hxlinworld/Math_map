
import numpy as np

a = np.array([[2,23,4],
              [2,32,4]],dtype=np.float32)
# print(a.dtype)


a = np.zeros((3,4))
# print(a)
a = np.ones((3,4),dtype=np.int16)
# print(a)
a = np.empty((3,4))
# print(a)

a = np.arange(2,10,2).reshape((2,2))
# print(a)
a = np.linspace(1,10,6).reshape(2,3)
print(a)