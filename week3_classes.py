"""
Brainnest Python Training
April 2023
Adnane Habib
Team A6
"""
"""
Week 3 Classes
1.Create a class called Rectangle that has attributes width and height. 
  Add methods area and perimeter that calculate the area and perimeter of the rectangle, respectively.
"""
class Rectangle:
    #constructor for class Rectangle
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height =height
    #class method for perimeter 
    def perimeter(self):
        try:
            return (float(self.width)+float(self.height))*2
        except:
            print("invalid dimensions")
            return 0
    #class method for area
    def area(self):
        try:
            return float(self.width)*float(self.height)
        except:
            print("invalid dimensions")
            return 0
         

    
if __name__=='__main__':
    print("Exercise 1")
    print()

    my_shape = Rectangle(5,2)
    print(f"I am a rectangle with height {my_shape.height} and width {my_shape.width}.")
    print(f"My area is {my_shape.area()} and perimeter is {my_shape.perimeter()}.")

    print()
    print()

"""
Week 3 Classes
2. Create a class called Circle that has attribute radius. 
   Add methods area and circumference that calculate the area and circumference of the circle, respectively.
"""

import math

class Circle:
    #constructor for class Circle
    def __init__(self, radius = 0):
        self.radius = radius
        
    #class method for circumference 
    def circumference(self):
        try:
            return (2*float(self.radius)*math.pi)
        except:
            print("invalid dimensions")
            return 0
    #class method for area
    def area(self):
        try:
            return (pow(float(self.radius),2)*math.pi)
        except:
            print("invalid dimensions")
            return 0

    
if __name__=='__main__':
    print("Exercise 2")
    print()

    my_shape = Circle("5")
    print(f"I am a rectangle with radius {my_shape.radius}.")
    print(f"My area is {my_shape.area()} and circumference is {my_shape.circumference()}.")

    print()
    print()

"""
Week 3 Classes
3. Create a class called Car that has attributes make, model, and year. 
   Add methods start and stop that simulate starting and stopping the car, respectively.
"""
class Car:
    #constructor for class Car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    #class method for starting car 
    def start(self):
        return "Vroom! I am moving!"
    #class method for stopping car
    def stop(self):
        return "Hee! I stopped."

    
if __name__=='__main__':
    print("Exercise 3")
    print()

    my_car = Car("Mazda","CX9",2012)
    print(f"My car is {my_car.make} model {my_car.model} year {my_car.year}.")
    print(my_car.start())
    print(my_car.stop())

    print()
    print()

"""
Week 3 Classes
4. Create a class called Dice that has attribute sides (the number of sides on the dice). 
   Add a method roll that generates a random number between 1 and the number of sides on the dice.
"""
import random
class Dice:
    #constructor for class Dice
    def __init__(self, sides=6):#setting the default value to 6
        try:#handling if the number of sides entered is invalid
            if (isinstance(sides, int)):
                if sides<=1:
                    raise Exception("Sorry, number of sides must be an integer greater than 1!")
                    self.sides=6
                else:
                    self.sides=sides
            else:
                raise Exception("Sorry, number of sides must be an integer greater than 1!")
                self.sides=6
        except Exception as e:
            print(e)
            self.sides=6
        finally:
            print(f"I have {self.sides} sides.")
            
    #class method for dice rolling 
    def roll(self):
        print("Let's roll the dice!") 
        return random.randint(1,self.sides)
    
#testing the class agains various instances    
if __name__=='__main__':
    print("Exercise 4")
    print()

    my_dice = Dice()
    print(my_dice.roll())
    print("Let's roll the dice again!")
    print(my_dice.roll())

    my_dice10 = Dice(10)
    print(my_dice10.roll())
    print("Let's roll the dice again!")
    print(my_dice10.roll())

    my_dice0 = Dice(0)
    print(my_dice0.roll())
    print("Let's roll the dice again!")
    print(my_dice0.roll())

    my_diceS = Dice("capa")
    print(my_diceS.roll())
    print("Let's roll the dice again!")
    print(my_diceS.roll())

    print()
    print()

"""
Week 3 Classes
5. Create a class called Temperature that has attribute celsius (a temperature in degrees Celsius). 
   Add methods to_fahrenheit and to_kelvin that convert the temperature to degrees Fahrenheit and Kelvin, respectively.
"""
class Temperature:
    #constructor for class Circle
    def __init__(self, celsius=0):
        try:
            self.celsius = float(celsius)
        except Exception as e:
            print("Temperature must be a valid number!")
            self.celsius = 0
        finally:
            print("You can convert to_fahrenheit or to_kelvin.")
    #class method for converting to fahrenheit 
    def to_fahrenheit(self):
        return self.celsius*9/5+32
    #class method for converting to kelvin 
    def to_kelvin(self):
        return self.celsius+273.15

    
if __name__=='__main__':#testing Temperature class instances
    print("Exercise 5")
    print()

    my_tempS = Temperature("Mazda")
    print(my_tempS.to_fahrenheit())
    print(my_tempS.to_kelvin())
    
    my_temp100 = Temperature(100)
    print(my_temp100.to_fahrenheit())
    print(my_temp100.to_kelvin())
        
    my_tempMinus5 = Temperature(-5)
    print(my_tempMinus5.to_fahrenheit())
    print(my_tempMinus5.to_kelvin())

    print()
    print()

"""
Week 3 Classes
6. Create a class called Book that has attributes title, author, and publication_year. 
   Add a method get_age that calculates how many years ago the book was published.
"""
import datetime

class Book:
    #constructor for class Book
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    #class method for reporting book age 
    def age(self):#using datetime method to get current year              
        return datetime.date.today().year-self.year

    
if __name__=='__main__':
    print("Exercise 6")
    print()

    my_book = Book("war and peace","tolstoi",1899)
    print(f"The book {my_book.title} from {my_book.author} is {my_book.age()} years old.")

    print()
    print()

"""
Week 3 Classes
7. Create a class called Rectangle that has attributes width and height. 
   Add methods str and repr that return a string representation of the rectangle object..
"""
class Rectangle:
    #constructor for class Rectangle
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height =height
    #class method for perimeter

    def __str__(self): #override str method
        try:
            float(self.width)+float(self.height)
            return f"I am a rectangle with height {my_shape.height} and width {my_shape.width}."
        except:
            return "I am a rectangle with invalid height or invalid width value."

    def __repr__(self): #override repr method
        try:
            float(self.width)+float(self.height)
            return f"height {my_shape.height} with default value 0 and width {my_shape.width} with default value 0.\nObject detects invalid nonnumeric entries but allows negative entries."
        except:
            return "Invalid height with default value 0 or invalid width with default value 0.\nObject detects invalid nonnumeric entries but allows negative entries."
    #class method for perimeter            
    def perimeter(self):
        try:
            return (float(self.width)+float(self.height))*2
        except:
            print("invalid dimensions")
            return 0
    #class method for area
    def area(self):
        try:
            return float(self.width)*float(self.height)
        except:
            print("invalid dimensions")
            return 0
    #class method for drawing shape    
    def draw(self):
        try:
            print()
            w = int(self.width)
            h = int(self.height)
            print(" "+"__"*w)
            for i in range(h-1):
                print("|"+"  "*w+"|")
            print("|"+"__"*w+"|")
        except:
            print("shape cannot be drawn")

        finally:
            print()
    
if __name__=='__main__':
    print("Exercise 7")
    print()

    my_shape = Rectangle(10,3)
    print(f"I am a rectangle with height {my_shape.height} and width {my_shape.width}.")
    print(f"My area is {my_shape.area()} and perimeter is {my_shape.perimeter()}.")
    print()
    print(my_shape.__str__())
    print()
    print(my_shape.__repr__())
    my_shape.draw()

    print()
    print()

    
"""
End of file
Week 3 Classes
"""