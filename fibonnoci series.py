n=int(input("enter a number"))
a=0
b=1
print(a)
print(b)
for i in range(2,n+1):
    c=a+b
    a=b
    b=c
    print(c)