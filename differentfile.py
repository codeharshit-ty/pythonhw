new_file = open('new_file4.txt','x')
new_file.close()
import os
print("checking if my_file exists or not....")
if os.path.exists("new_file2.txt"):
   os.remove("new_file2.txt")
else:
    print("the file does not exists.")
my_file = open("my_file.txt",'w')
my_file.write("hi! I am harshit and I am 14 years old.")
my_file.close()
os.remove('codingal.txt')
os.rmdir('myfolder')