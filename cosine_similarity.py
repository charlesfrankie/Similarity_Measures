#!/usr/bin/env python


from math import *


def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])), 3)


def cosine_similarity(x, y):

    numerator = sum(a*b for a, b in zip(x, y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator), 3)


print(cosine_similarity([1, 2, 3], [
      3, 5, 7]))
