import math
import matplotlib.pyplot as plt
import numpy as np


def square(x):
    """Returns the square of x."""
    return x ** 2


def cube(x):
    """Returns the cube of x."""
    return x ** 3


def sine(x):
    """Returns the sine of x."""
    return math.sin(x)


def exponential(x):
    """Returns the exponential value of x."""
    return math.exp(x)


def reciprocal(x):
    """Returns 1/x. Not continuous at x=0."""
    if x == 0:
        raise ValueError("Function not defined at x=0.")
    return 1 / x


def square_root(x):
    """Returns the square root of x. Not continuous for x<0."""
    if x < 0:
        raise ValueError("Function not defined for x<0.")
    return math.sqrt(x)


def reciprocal_quadratic(x):
    """Returns 1/(x^2 - 1). Not continuous at x=1 and x=-1."""
    if x in [1, -1]:
        raise ValueError("Function not defined at x=1 or x=-1.")
    return 1 / (x ** 2 - 1)


def cosine(x):
    """Returns the cosine of x."""
    return math.cos(x)


def tangent(x):
    """Returns the tangent of x. Not continuous at odd multiples of pi/2."""
    if (x % math.pi) == math.pi / 2:
        raise ValueError("Function not defined at odd multiples of pi/2.")
    return math.tan(x)


def secant(x):
    """Returns the secant of x. Not continuous where cos(x) = 0."""
    cos_val = math.cos(x)
    if cos_val == 0:
        raise ValueError("Function not defined where cos(x) = 0.")
    return 1 / cos_val


def cosecant(x):
    """Returns the cosecant of x. Not continuous where sin(x) = 0."""
    sin_val = math.sin(x)
    if sin_val == 0:
        raise ValueError("Function not defined where sin(x) = 0.")
    return 1 / sin_val


def cotangent(x):
    """Returns the cotangent of x. Not continuous where sin(x) = 0."""
    sin_val = math.sin(x)
    if sin_val == 0:
        raise ValueError("Function not defined where sin(x) = 0.")
    return 1 / math.tan(x)


def natural_log(x):
    """Returns the natural logarithm of x (base e). Not continuous for x <= 0."""
    if x <= 0:
        raise ValueError("Function not defined for x <= 0.")
    return math.log(x)


def common_log(x):
    """Returns the logarithm of x with base 10. Not continuous for x <= 0."""
    if x <= 0:
        raise ValueError("Function not defined for x <= 0.")
    return math.log10(x)


def absolute_value(x):
    """Returns the absolute value of x."""
    return abs(x)


def epsilon_delta_check(func, a, limit_value, epsilon):
    """
    Check for a suitable delta based on the epsilon-delta definition of limits.
    """
    delta = 1
    while True:
        valid = True
        for x in [a - delta, a + delta]:
            if not (0 < abs(x - a) < delta):
                continue
            if abs(func(x) - limit_value) >= epsilon:
                valid = False
                break
        if valid:
            return delta
        delta *= 0.5


def plot_epsilon_delta(func_name, func, point_of_interest, limit_value, epsilon, delta):
    fig, ax = plt.subplots()

    # Define a range for x, centered around the point of interest
    x = np.linspace(point_of_interest - 3, point_of_interest + 3, 400)
    y = [func(xi) for xi in x]

    # Plot the function
    ax.plot(x, y, label=f'f(x)={func_name}')

    # Draw epsilon range around L
    ax.axhspan(limit_value - epsilon, limit_value + epsilon, color='yellow', alpha=0.5)

    # Draw delta range around x_0
    ax.axvspan(point_of_interest - delta, point_of_interest + delta, color='green', alpha=0.5)

    ax.set_title(f'Visualization for f(x)={func_name}')
    ax.legend()

    return fig


FUNCTIONS = {
    'square': square,
    'cube': cube,
    'sine': sine,
    'exponential': exponential,
    'reciprocal': reciprocal,
    'square_root': square_root,
    'reciprocal_quadratic': reciprocal_quadratic,
    'cosine': cosine,
    'tangent': tangent,
    'secant': secant,
    'cosecant': cosecant,
    'cotangent': cotangent,
    'natural_log': natural_log,
    'common_log': common_log,
    'absolute_value': absolute_value
}
