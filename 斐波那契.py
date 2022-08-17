
def fun(n):
    if n <= 2 :
        return 1

    return fun(n-2) + fun(n-1)


for i in range(21):
   print(fun(i))



