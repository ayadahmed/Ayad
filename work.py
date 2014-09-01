__author__ = 'ahmed'
import math
from numbers import Number
from numpy import *

def circle_area(Number)->Number:
    """
    calculat the erea of a circle given the radius
    :param radius : radius of the circle
    :return : area of the circle( in units of radius )
    """
    return math.pi*radius**2
print(circle_area(5.0))