def oddoccurring(arr):
    res = 0
    for element in arr:
        res = res ^ element
        print(res)
    return res
arr =[]
n = int(input("enter array size : "))
while(n):
    num = int(input("enter number : "))
    arr.append(num)
    n -= 1
print("\n\nodd occurring number is : ", oddoccurring(arr))