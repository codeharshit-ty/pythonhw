def fun1(n):
    return n*(n+1)/2
print(fun1(4))
#so, the no of iteration will be 1 for any input

def fun2(n):
    sum = 0
    for i in range(1,n+1):
        sum+=1
    return sum
print  (fun2(4))
#no of iteration = no of input

def fun3(n):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum+=1
    return sum
print  (fun3(4))