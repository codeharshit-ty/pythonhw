class cat:
    def __init__(self,name,age):
        self.age = age
        self.name = name
    def info (self): 
        print(f"i am a cat . my name is {self.name}. i am {self.age} years old. ")
    def make_sound(self):
        print("meow")
class dog:
     def __init__(self,name,age):
        self.age = age
        self.name = name
     def info (self): 
        print(f"i am a dog . my name is {self.name}. i am {self.age} years old. ")
     def make_sound(self):
        print("bark")
cat1 = cat("dodo",2.5)   
dog1 = dog("lion",7)
for objects in (cat1,dog1):
    objects.info()
    objects.make_sound()