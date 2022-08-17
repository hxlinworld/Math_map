import numpy as np
import sympy as sp
from scipy.sparse.linalg import eigs
import pylab as plt


# 斐波那契数列求解问题
'''
A = sp.Matrix([[0,1],
               [1,1]])
P,D = A.diagonalize() # 将A相似对角化 P->相似变换矩阵，D->对角矩阵
sp.var('k',positive = True ,integer = True) # positive = True ->属于正数  integer = True->属于整数

Ak= P @ (D ** 'k') @ (P.inv())
a_k = Ak @ (sp.Matrix([1,1]))
s = sp.simplify(a_k[0])
print(s)
sm=[]
for i in range(20):
    sm.append(s.subs('k',i).n(4))
print(sm)
'''

'''
t,c1,c2 = sp.var('t,c1,c2')
t0 = sp.solve(t**2-t-1)
eq1 = c1+c2-1
eq2 = c1*t0[0] + c2*t0[1]
s = sp.solve([eq1,eq2])
print('c1=',s[c1])
print('c2=',s[c2])
'''

''''
k= sp.var('k')
y= sp.Function('y')
f = y(k+2)+y(k+1)-y(k)  # f为使得右边值为0的方程
s = sp.rsolve(f,y(k),{y(0):1,y(1):1})
print(s)
'''

# 莱斯利种群模型
# L = [[a1,a2,...,an-1,an],
#      [b1,0,0,.........0],
#      [0,b2,0,0,........],
#      ...................,
#      [0,0,0..... bn-1,0]]
# L 为莱斯利矩阵
# a[n]为 每个年龄组对应的生育率，b[n]为对应的存活率
# Xk = L**k @ X0 ->求解 L**k -> 求解相似变换矩阵 P -> P的逆矩阵(P**-1)*X0(3*1)得到矩阵C(3*1) -> c为C[0]的第一个元素
# 当 k -> 无穷，Xk = c* (2/3)**k * α1 其中α1为特征值λ1对应的特征向量，P = [α1，α2，α3] D = diag(λ1,λ2,λ3)
'''
X0 = np.array([500,1000,500])
L = np.array([[0,4,3],[0.5,0,0],[0.25,0,0]])
X1 = L @ X0
X2 = L**2 @ X0
Ls = sp.Matrix([[0,4,3],[sp.Rational(1,2),0,0],[0,sp.Rational(1,4),0]])
P,D = Ls.diagonalize()
Pinv = P.inv()
Pinv = sp.simplify(Pinv)
C = Pinv@ X0
print('P=\n',P)
print('c=',C[0])
'''



# PageRank 模型/随机冲浪PageRank模型
L = [(1,2),(2,3),(2,4),(3,4),(3,5),(3,6),(4,1),(5,6),(6,1)]
W = np.zeros((6,6))
for i in range(len(L)):
    W[L[i][0]-1,L[i][1]-1]=1
r = np.sum(W,axis=1,keepdims=True)
P = (1-0.85)/W.shape[0]+0.85*W/r  # 随机模型，阻尼因子d=0.85
# P = W/r    # 矩阵传播
val ,vec = eigs(P.T,1)  # eigs函数求解矩阵的特征值和特征向量，V为包含特征值的对角矩阵，D为包含对应特征向量的矩阵
V = vec.real  # 取实部，忽略无影响
V = V.flatten() # 将V展开成数组
V = V/V.sum()   # 各元素归一化
print('V=',np.round(V,6))
plt.bar(range(1,len(W)+1),V,width =0.6,color = 'g')
plt.show()


