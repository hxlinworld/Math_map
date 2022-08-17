import numpy as np
a = np.array([10,11,12,13]
            )

b = np.arange(4)
# print(a,b)

c = b**2
c = 10*(np.sin(b)) # cos tan

# print(b<3)


M = np.array([[1,1],
              [0,1]])
N = b.reshape((2,2))
# print(M)
# print(N)
# print(M*N)
# print(np.dot(M,N))
# print(M.dot(N))

a = np.random.random((2,4))
print(a)
print(np.sum(a,axis=0)) # axis=0 ->在列数中寻找，axis=1 ->在行数中寻找
print(np.min(a,axis=1))
print(np.max(a))


