#import necessary packages
from abc import ABC, abstractmethod
#create a base class
class Animal(ABC):
    #abstract method
    #should it be implemented by all sub-classes
    def move(self):
        pass
    # sub classes
class Human(Animal):
    def move(self):
        print("i can walk and run")

class Snake(Animal):
    def move(self):
        print("i can crawl")

class dog(Animal):
    def move(self):
        print("i can bark")

class lion(Animal):
    def move(self):
        print("i can roar")
#driver code
R = Human()
R.move()

K=Snake()
K.move

R=Dog()
R.move()

K=Lion()
K.move