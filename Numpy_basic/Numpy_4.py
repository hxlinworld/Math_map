import numpy as np
A = np.arange(2,14).reshape(3,4)
print(A)

# print(np.argmin(A))
# print(np.argmax(A))
# print(np.average(A))
# print(np.median(A))
# print(np.cumsum(A))  #累加
# print(np.diff(A))    #累差
# print(np.nonzero(A))
b = np.arange(14,2,-1).reshape((3,4))
# print(b,np.sort(b))

# print(np.transpose(A))
# print(A.T)
# print( (A.T).dot(A))
# print(np.clip(A,5,9))
print(np.mean(A,axis=1))






