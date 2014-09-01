__author__ = 'ahmed'

import math
from pylab import*
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

v_circle_area = np.vectorize(circle_area)


S = np.linspace(0, 10)  # our side lengths

A = v_circle_area(S)  # the areas


plot(S, A, '-r', label="Area")


xlabel('radius')
ylabel('geo values')
title('circle Geo Properties')
legend(loc='upper right')

show()

