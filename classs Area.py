'''write a program in python that has class circle. use class variable to define value of pi.
use this class variable to calculate area and circumference of circle with specified radius'''
from math import pi


class Circle:
    Pi = pi


    def __init__(self, radius):
        self.radius = radius

    def Circumference(self):
        circumference = 2 * Circle.Pi * self.radius
        print("Circumference of circle is", circumference)

    def Area(self):
        area = Circle.Pi * (self.radius ** 2)
        print("Area of circle is", area)


circle1 = Circle(5)
circle1.Circumference()
circle1.Area()
