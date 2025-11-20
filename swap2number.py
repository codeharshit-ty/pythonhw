#1 method
def swap1(a, b):
    print("before Swapping: a =", a, " b =", b)
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("After Swapping: a =", a, " b =", b)

# 2 method
def swap2(a, b):
    print("before Swapping: a =", a, " b =", b)
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    print("After Swapping: a =", a, " b =", b)
a = int(input("enter the value of a :"))
b = int(input("enter the value of b :"))

swap1(a,b)
swap2(a,b)