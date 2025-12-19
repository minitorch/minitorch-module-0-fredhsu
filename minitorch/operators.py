"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


def mul(x, y):
    return x * y


def id(x):
    return x


def add(x, y):
    return x + y


def neg(x):
    return -x


def lt(x, y):
    return x < y


def eq(x, y):
    return x == y


def max(x, y):
    return x if x > y else y


def is_close(x, y):
    # $f(x) = |x - y| < 1e-2$
    return abs(x - y) < 1e-2


def sigmoid(x):
    # $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
    return 1.0 / (1.0 + math.exp(-x)) if x >= 0 else math.exp(x) / (1.0 + math.exp(x))


def relu(x):
    return x if x > 0 else 0


def log(x):
    return math.log(x)


def exp(x):
    return math.exp(x)


def log_back(x):
    return 1 / x


def inv(x):
    return 1 / x


def inv_back(x):
    return -1 / (x**2)


def relu_back(x, y):
    return y if x > 0 else 0


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce


def map():
    pass


def zipWith():
    pass


def reduce():
    pass


#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


def negList():
    pass


def addLists():
    pass


def sum():
    pass


def prod():
    pass


# TODO: Implement for Task 0.3.
