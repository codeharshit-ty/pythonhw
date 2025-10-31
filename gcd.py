numberlargest = int(input("enter the largest number:"))
numbersmallest = int(input("enter the smallest number:"))
while(numbersmallest):
    numberstore = numbersmallest
    numbersmallest = numberlargest%numbersmallest
    numberlargest = numberstore
    print("HCF is :",numberlargest)