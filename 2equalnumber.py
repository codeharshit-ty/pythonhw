def checkiFSame(number1,number2):
    if ((number1^number2) != 0):
        print("number are not equal")
    else:
        print("both number are equal ")
number1 = int(input("enter first number to compare"))
number2 = int(input("enter secound number to compare"))
checkiFSame(number1,number2)