class parrot:
   def __init__(self,name,age):
    self.name = name
    self.age = age
   def sing(self,song):
        return "{} sings {}".format(self.name,song)
   def dance(self):
       return "{} is now dancing".format(self.name)
blu = parrot("blu",10)
print(blu.sing("'happy'"))
print(blu.dance())
green = parrot("green",10)
print(green.sing("'vande matram"))
print(green.dance())
print("age of green is ",green.age)
       
    
