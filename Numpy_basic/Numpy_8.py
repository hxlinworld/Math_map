import numpy as np
a = np.arange(4)

b=a
c=a
d=b

a[0]=11
# print(a)
# print((b is a))
# print(b)
# print(c)
# print(d)
d[1:3] = [22,33]
# print(d)

b = a.copy() # deep copy b不会因为a的改变而改变

print(b)
a[3]=44
print(a)
print(b)