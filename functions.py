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


def plot_function_with_epsilon_delta(func, a, limit_value, epsilon, delta):
    x = np.linspace(a - 3 * delta, a + 3 * delta, 400)
    y = [func(val) for val in x]

    fig, ax = plt.subplots(figsize=(8, 6))

    # Plotting the main function with bright purple
    ax.plot(x, y, label=f'{func.__name__}(x)', color="#292951", lw=3)

    # Highlighting the epsilon region with bright orange
    ax.fill_between(x, limit_value - epsilon, limit_value + epsilon, color="#FFC300", alpha=0.6)

    # Highlighting the delta region with pastel blue
    ax.axvspan(a - delta, a + delta, color="#A7C7E7", alpha=0.6)

    ax.set_title(f"Epsilon-Delta plot for {func.__name__}(x)")
    ax.set_xlabel('x')
    ax.set_ylabel(f'{func.__name__}(x)')
    ax.grid(True)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.legend()
    fig.tight_layout()

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
