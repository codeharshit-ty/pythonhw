with open('codingal.txt','w') as file:
    file.write("hi! I am harshit and I am 14 years old. ")
file.close()
with open('codingal.txt','r') as file:
    data = file.readlines()
    print("words in this file are....")
    for line in data:
        word = line.split()
        print(word)
file.close()