__author__ = 'ahmed'

import math
from numbers import Number
from numpy import *
from pylab import *


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

v_circle_area = np.vectorize(circle_area)
v_circle_perimeter = np.vectorize(circle_perimeter)

S = np.linspace(0, 10) # our radius

A = v_circle_area(S)  # the circle areas
P = v_circle_perimeter(S)  # the circle perimeters

plot(S, A, '-r', label="Circle Area")
plot(S, P, ':b', label="Circle Perimeter")


xlabel('Radius')
ylabel('geo values')
title('Circle Geo Properties')
legend(loc='upper right')

show()


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

v_sphere_area = np.vectorize(sphere_area)
v_sphere_volume = np.vectorize(sphere_volume)

S = np.linspace(0, 10) # our radius

A = v_sphere_area(S)  # the sphere areas
P = v_sphere_volume(S)  # the sphere perimeters

plot(S, A, '-r', label="Sphere Area")
plot(S, P, ':b', label="Sphere Perimeter")


xlabel('Radius')
ylabel('geo values')
title('Sphere Geo Properties')
legend(loc='upper right')

show()


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

v_square_area = np.vectorize(square_area)
v_square_perimeter = np.vectorize(square_perimeter)

S = np.linspace(0, 10) # our side lengths

A = v_square_area(S)  # the square areas
P = v_square_perimeter(S)  # the square perimeters

plot(S, A, '-r', label="Square Area")
plot(S, P, ':b', label="Square Perimeter")


xlabel('side length')
ylabel('geo values')
title('Square Geo Properties')
legend(loc='upper right')

show()





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

v_rectangle_area = np.vectorize(rectangle_area)
v_rectangle_perimeter = np.vectorize(rectangle_perimeter)

S = np.linspace(0, 10) # our rectangle width
A = v_rectangle_area(S,10)  # the areas
P = v_rectangle_perimeter(S,10)  # the perimeters

plot(S, A, '-r', label="Rectangle Area")
plot(S, P, ':b', label="Rectangle Perimeter")


xlabel('width')
ylabel('geo values')
title('Rectangle Geo Properties')
legend(loc='upper right')

show()



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

v_triangle_area = np.vectorize(triangle_area)
v_trapezoid_area = np.vectorize(trapezoid_area)
v_ellipse_area = np.vectorize(ellipse_area)


S = np.linspace(0, 10) # our  rectangle base length, trapezoid's small base and ellipse radius
A = v_triangle_area(S,10)  # the triangle areas
P = v_trapezoid_area(S,10,10)  # the trapezoid area
Z = v_ellipse_area(S,10)  # the ellipse area

plot(S, A, '-r', label="Triangle Area")
plot(S, P, ':b', label="Trapezoid Perimeter")
plot(S, Z, '-r', label="Ellipse Area")



xlabel('side length')
ylabel('geo values')
title('Ttiangle, Trapezoid and Ellipse Geo Properties')
legend(loc='upper right')

show()