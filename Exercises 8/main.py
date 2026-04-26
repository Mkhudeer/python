#1. Rectangles Measurement
#Create a version of the Rectangle class that is safe by assuring that 
# both width and height are positive values (how you do that is up to you). 
# Expand it with methods that calculate its surface area and its circumference. 
# Also, provide a method that returns the bottom-right corner of the rectangle as a Point. Finally, create a method that gets a second Rectangle object as a parameter, 
# and returns the overlapping area of 
# the two rectangles as a new Rectangle object 
# (the last one is much harder than the other ones).


# Exercise 1: Rectangle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, x, y, w, h):
        if w <= 0 or h <= 0:
            raise ValueError("Width and Height must be positive")

        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def circumference(self):
        return 2 * (self.w + self.h)

    def bottom_right(self):
        return Point(self.x + self.w, self.y + self.h)

    def overlap(self, other):
        x1 = max(self.x, other.x)
        y1 = max(self.y, other.y)
        x2 = min(self.x + self.w, other.x + other.w)
        y2 = min(self.y + self.h, other.y + other.h)

        if x1 < x2 and y1 < y2:
            return Rectangle(x1, y1, x2 - x1, y2 - y1)
        return None
    
    print("=== Exercise 1: Rectangle ===")
r1 = Rectangle(0, 0, 10, 5)
r2 = Rectangle(5, 2, 10, 5)

print("Area:", r1.area())
print("Circumference:", r1.circumference())

br = r1.bottom_right()
print("Bottom right:", br.x, br.y)

overlap = r1.overlap(r2)
if overlap:
    print("Overlap area:", overlap.area())
else:
    print("No overlap")


# 2. Inrolled Students
#A student has the last name, a first name, a date of birth 
# (either a year, month, and day, or a DateTime object if you took the liberty of studying the DateTime module already), 
#and an administration number. 
#A course has a name and a number. 
#can enroll in courses. 
#Create a class Student and a class Course.
 #Create several students and several courses. 
 #Enroll each student in some of the courses. 
 #Display a list of students, showing their number, first name, last name, and age, 
 #and per student which courses he or she is enrolled in.

# Exercise 2: Student & Course
# =========================

from datetime import date

class Student:
    def __init__(self, first_name, last_name, birth_year, admin_number):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.admin_number = admin_number
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def age(self):
        return date.today().year - self.birth_year


class Course:
    def __init__(self, name, number):
        self.name = name
        self.number = number


print("\n=== Exercise 2: Students ===")
c1 = Course("Math", 101)
c2 = Course("Programming", 102)

s1 = Student("mohamad", "khudeer", 2000, 1)
s2 = Student("Lekaa", "Kassab", 1998, 2)

s1.enroll(c1)
s1.enroll(c2)
s2.enroll(c2)

students = [s1, s2]

for s in students:
    print(s.admin_number, s.first_name, s.last_name, "- Age:", s.age())
    for c in s.courses:
        print("  -", c.name)


#3. Square Measurement
#Below I give a Rectangle class that is created with the x and y 
# coordinate of the top-left corner, a width w, and a height h.
#  Now create a Square class that inherits as much as possible from the Rectangle class.

#class Rectangle:
#   def __init__( self , x, y, w, h ):
#      self.x = x
#     self.y = y
#    self.w = w
    
#   self.h = h

#def area( self ):
#   return self.w * self.h
#     #def circumference( self ):
#   return 2*( self.w + self.h)

# Exercise 3: Square
# =========================

class Square(Rectangle):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)



print("\n=== Exercise 3: Square ===")
sq = Square(0, 0, 5)
print("Square area:", sq.area())




#Rectangle and a Square can be considered shapes. 
#There are, of course, different kinds of shapes that are
#defined differently but share with rectangles and squares that they
#  have an area and circumference. Define an interface class Shape, 
# of which Rectangle and Square are sub(sub)classes. 
# Also, define a class Circle that you derive from Shape.

# Exercise 4: Shape + Circle
# =========================

import math

class Shape:
    def area(self):
        pass

    def circumference(self):
        pass


class RectangleShape(Rectangle, Shape):
    pass


class SquareShape(Square, Shape):
    pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius
    
print("\n=== Exercise 4: Shapes ===")
circle = Circle(3)
print("Circle area:", circle.area())
print("Circle circumference:", circle.circumference())    









