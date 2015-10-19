import os
import ctypes
from timeit import timeit

# -----------------------------------------------------------------------------
#
# Pure-python implementations
#
# -----------------------------------------------------------------------------


def n_squared(iterations):
    """
    A contrived function that should run in O(n^2) time based on the
    size of the input.

    """
    result = 0
    i = 0

    # n-squared
    while i < iterations:
        j = 0
        while j < iterations:
            result += i + j
            j += 1
        i += 1
    return result


def linear(iterations):
    """
    A contrived function that should run in O(n) time based on the
    size of the input.

    """
    result = 0
    i = 0
    while i < iterations:
        result += i
        i += 1
    return result


def log_n(iterations):
    result = 0
    i = 0
    while i < iterations:
        result += i
        iterations = iterations / 2
        i += 1
    return result

# -----------------------------------------------------------------------------
#
# C implementations
#
# -----------------------------------------------------------------------------


_file = 'src/libalgo.1.dylib'
_path = os.path.join(*(os.path.split(__file__)[:-1] + (_file,)))
_mod = ctypes.cdll.LoadLibrary(_path)

# int n_squred(int)
c_n_squared = _mod.n_squared
c_n_squared.argtypes = (ctypes.c_int, )
c_n_squared.restype = ctypes.c_int


# int linear(int)
c_linear = _mod.linear
c_linear.argtypes = (ctypes.c_int, )
c_linear.restype = ctypes.c_int

# int log_n(int)
c_log_n = _mod.log_n
c_log_n.argtypes = (ctypes.c_int, )
c_log_n.restype = ctypes.c_int

# -----------------------------------------------------------------------------
#
# Timing
#
# -----------------------------------------------------------------------------

def time_complexity(func, max_iterations):
    """
    Run this in ipython, save the results, then do:

    >>> %pylab
    >>> plot(results)

    This should let you see a chart of the increasing time complexity.

    """
    times = []
    for i in range(max_iterations):
        runstring = "{}({})".format(func, i)
        setup = "from main import {}".format(func)
        time = timeit(runstring, setup=setup, number=1000)
        times.append(time)
    return times


if __name__ == "__main__":
    print(n_squared(100))
