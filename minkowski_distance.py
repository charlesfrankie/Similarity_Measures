#!/usr/bin/env python
# ** Exponentiation ( Similar to pow(x, y) )

from math import *
from decimal import Decimal


def nth_root(value, n_root):
    root_value = 1/float(n_root)
    return round(Decimal(value) ** Decimal(root_value), 3)
    # return round(pow(Decimal(value), Decimal(root_value)), 3)


def minkowski_distance(x, y, p_value):
    return nth_root(sum(pow(abs(a-b), p_value) for a, b in zip(x, y)), p_value)


x = [0, 3, 4, 5]
y = [7, 6, 3, -1]

print(minkowski_distance(x, y, 3))
