# intro to oop in python

Python is a multi-paradigm programming language. It supports different programming approaches. One of the popular approaches to solve a programming problem is by creating objects. This is known as Object-Oriented Programming (OOP).

An object has two characteristics:

- attributes
- behavior

```
A parrot is an object, as it has the following properties:

>> name, age, color as attributes
>> singing, dancing as behavior
```

The concept of OOP in Python focuses on creating reusable code. This concept is also known as **__DRY (Don't Repeat Yourself)__**.

## basic concepts

### class

A class is a blueprint for the object.

```
class Ball:
    pass
```

### object

An object (instance) is an instantiation of a class. When class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.

```
beach_ball = Ball()
```

```
# basic example

class Ball:

    # instance attributes
    # contructor
    def __init__(self, name, color = 'white'):
        self.name = name
        self.color = color

    # instance method
    def bounce(self):
        print(f'{name} is bouncing')

# instantiate the object
beach_ball = Ball('beach ball', 'red')
baseball_ball = Ball('baseball ball')

print(beach_ball.bounce())
print(baseball_ball.color)

```

## inheritance

Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).

```
# parent class

class Ball:
    def __init__(self):
        print("Ball is ready")

    def get_class_name(self):
        print("Bird")

    def play(self):
        print("Lets play ball")


class BasketballBall(Ball):
    def __init__(self):
        # call super() function
        super().__init__()
        print("Basketball ball is ready")

    def get_class_name(self):
        print("BasketballBall")

    def play(self):
        print("Lets play basketball")

random_ball 

mikasa = BasketBall()
mikasa.get_class_name()
mikasa.play()
```

## encapsulation

Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.

```
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def set_max_price_(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.set_max_price(1000)
c.sell()
```

## polymorphism

Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).

```
class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def bird_fly(bird):
    bird.fly()

def bird_swim(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
bird_fly(blu)
bird_fly(peggy)

bird_swim(blu)
bird_swim(peggy)


```
