from abc import ABC,abstractmethod
class Animal(ABC):
    def move(self):
       pass
class human(Animal):
    def move (self):
        print("i can walk and talk")
class snake(Animal):
    def move (self):
        print("i can crawl")
class dog(Animal):
    def move (self):
        print("i can bark")
class lion (Animal):
    def move (self):
        print("i can roar")
R = human()
R.move()
K = snake()
K.move()
R = dog()
R.move()
K = lion()
K.move()
