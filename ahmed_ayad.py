__author__ = 'ahmed'
import math
from numbers import Number
from numpy import *


def circle_area(r):
    """
    calculate the area of a circle given r
    :param r : radius of the circle
    :return : area of the circle( in units of r )
    """
    return pi*r**2
print(circle_area(10.0))

def circle_perimeter(r):
    """
    calculate the perimeter of a circle given r
    :param r : radius of the circle
    :return : perimeter of the circle( in units of r )
    """
    return 2.0*pi*r
print(circle_perimeter(10.0))


def sphere_area(r):
    """
    calculate the area of a sphere given r
    :param r : radius of the sphere
    :return : area of the sphere( in units of r )
    """
    return 4*pi*r**2
print(sphere_area(10.0))


def sphere_volume(r):
    """
    calculate the volume of a sphere given the r
    :param r : radius of the sphere
    :return : volume of the sphere( in units of r )
    """
    return (3.0/4.0)*pi*r**3
print(sphere_volume(10.0))


def square_area(a):
    """
    calculate the area of a square given a
    :param a : side length
    :return : area of the square(in units of a)
    """
    return a**2
print (square_area(5.0))


def square_perimeter(a):
    """
    calculate the perimeter of a square given a
    :param a : side length
    :return : perimeter of the square(in units of a)
    """
    return 4*a
print (square_perimeter(5.0))



def rectangle_area(w,h):
    """
    calculate the area of a rectangle given w and h
    :param w : the width of the rectangle
    :param h : the height of the rectangle
    :return : area of the rectangle(in units of w and h)
    """
    return w*h
print (rectangle_area(5.0 , 2.0))


def rectangle_perimeter(w,h):
    """
    calculate the perimeter of a rectangle given w and h
    :param w : the width of the rectangle
    :param h : the height of the rectangle
    :return : perimeter of the rectangle(in units of w and h)
    """
    return 2.0*(w+h)
print (rectangle_perimeter(5.0,2.0))


def triangle_area(b,h):
    """
    calculate the area of a triangle given b and h
    :param b : the base length of the rectangle
    :param h : the vertical height of the rectangle
    :return : area of the triangle(in units of w and h)
    """
    return 0.5*b*h
print (triangle_area(5.0,2.0))


def trapezoid_area(a,b,h):
    """
    calculate the area of a trapezoid given a, b and h
    :param a : the length of the trapezoid's small base
    :param b : the length of the trapezoid's large base
    :param h : the vertical height of the trapezoid
    :return : area of the trapezoid(in units of a,b and h)
    """
    return 0.5*(a+b)*h
print (trapezoid_area(3.0,5.0,2.0))


def ellipse_area(a,b):
    """
    calculate the area of a ellipse given a and b
    :param a : the length of the small radius
    :param b : the the length of the large radius
    :return : area of the ellipse(in units of a and b)
    """
    return pi*a*b
print (ellipse_area(3.0,6.0))
