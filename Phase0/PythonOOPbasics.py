class Car:
    wheels = 4
    def __init__(self,model,year,color):
        self.model = model 
        self.year = year 
        self.color = color

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

car1 = Car("porche911",2018,"Black")
print(car1.model)
car1.describe()
print(car1.wheels)

class Animals:
    def __init__(self, name):
        self.name = name 
        self.alive = True

    def speak(self):
        return self.voice
    
class Dogs(Animals):
    def __init__(self, name):
        super().__init__(name)
        self.voice = "Woof!"

doggy = Dogs("pluto")
print(doggy.name)
print(doggy.speak())

class Shape:
    def __init__(self,color,filled):
        self.color = color 
        self.filled = filled

class Circle(Shape):
    def __init__(self, color, filled,radius):
        super().__init__(color, filled)
        self.area = 3.14*radius*radius

circle1 = Circle("red",True,5)
print(circle1.area) 

#magic methods 
class Complex():
    def __init__(self, real, imaginary):
        self.real = real 
        self.imaginary = imaginary

    def __str__(self):
        return "%s + i%s" % (self.real,self.imaginary)
    def __repr__(self):
        return "rational(%s, %s)" %  (self.real,self.imaginary)
    
complex1 = Complex(1,2)
print(str(complex1))
print(repr(complex1))

#@property
class Portal():
    def __init__(self):
        self._name = ""

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        self._name = val

    @name.deleter
    def name(self):
        self._name = None

# Creating object
p = Portal();

# Setting name
p.name = 'michael jackson'

# Prints name
print (p.name)

# Deletes name
del p.name

# As name is deleted above this 
# will throw an error
print (p.name)

#abstract method
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

class Cats(Animals):
    def __init__(self, name):
        super().__init__(name)
        self.voice = "Meow!"

cat1 = Cats("kitty")
print(cat1.name)
print(cat1.speak())