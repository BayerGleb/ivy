"""
Collection of Numpy general functions, wrapped to fit Ivy syntax and signature.
"""

# global
import logging
import numpy as _np
import math as _math
from operator import mul as _mul
from functools import reduce as _reduce
import multiprocessing as _multiprocessing

# local
import ivy
from ivy.functional.ivy.old import default_dtype
from ivy.functional.backends.numpy.device import _dev_callable

copy_array = lambda x: x.copy()

def is_array(x, exclusive=False):
    if isinstance(x, _np.ndarray):
        return True
    return False