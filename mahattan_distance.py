#!/usr/bin/env python

from math import *


def mahattan_distance(x, y):
    return sum(abs(a-b) for a, b in zip(x, y))


x = [10, 20, 10]
y = [10, 20, 20]

print(mahattan_distance(x, y))
