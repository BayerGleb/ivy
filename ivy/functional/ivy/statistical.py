# global
from typing import Union, Tuple, Optional

# local
import ivy
from ivy.framework_handler import current_framework as _cur_framework


# Array API Standard #
# -------------------#

# noinspection PyShadowingBuiltins
def min(x: Union[ivy.Array, ivy.NativeArray],
        axis: Union[int, Tuple[int]] = None,
        keepdims: bool = False) \
        -> ivy.Array:
    """
    Return the minimum value of the input array x.

    :param x: Input array containing elements to min.
    :param axis: Axis or axes along which minimum values must be computed, default is None.
    :param keepdims, optional axis or axes along which minimum values must be computed, default is None.
    :param f: Machine learning framework. Inferred from inputs if None.
    :return: array containing minimum value.
    """
    return _cur_framework.min(x, axis, keepdims)


# noinspection PyShadowingBuiltins
def max(x: Union[ivy.Array, ivy.NativeArray],
        axis: Union[int, Tuple[int]] = None,
        keepdims: bool = False) \
        -> ivy.Array:
    """
    Calculates the maximum value of the input array ``x``.
    .. note::
       When the number of elements over which to compute the maximum value is zero, the maximum value is implementation-defined. Specification-compliant libraries may choose to raise an error, return a sentinel value (e.g., if ``x`` is a floating-point input array, return ``NaN``), or return the minimum possible value for the input array ``x`` data type (e.g., if ``x`` is a floating-point array, return ``-infinity``).
    **Special Cases**
    For floating-point operands,
    -   If ``x_i`` is ``NaN``, the maximum value is ``NaN`` (i.e., ``NaN`` values propagate).
    
    Parameters
    ----------
    x: 
        input array. Should have a numeric data type.
    axis: 
        axis or axes along which maximum values must be computed. By default, the maximum value must be computed over the entire array. If a tuple of integers, maximum values must be computed over multiple axes. Default: ``None``.
    keepdims:
        if ``True``, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes (dimensions) must not be included in the result. Default: ``False``.
    
    Returns
    -------
    out: 
        if the maximum value was computed over the entire array, a zero-dimensional array containing the maximum value; otherwise, a non-zero-dimensional array containing the maximum values. The returned array must have the same data type as ``x``.
    """
    return _cur_framework.max(x, axis, keepdims)


def prod(x: Union[ivy.Array, ivy.NativeArray],
         axis: Optional[Union[int, Tuple[int]]] = None,
         dtype: Optional[Union[ivy.Dtype, str]] = None,
         keepdims: bool = False)\
        -> ivy.Array:
    """
    Calculates the product of input array x elements.

    :param x: input array. Should have a numeric data type.
    :type x: array
    :param axis: axis or axes along which products must be computed. By default, the product must be
     computed over the entire array. If a tuple of integers, products must be computed over multiple axes. Default: None.
    :type axis: Union[int, Tuple[int, ...]
    :param dtype: data type of the returned array. If None,
        if the default data type corresponding to the data type “kind” (integer or floating-point) of x has a smaller 
         range of values than the data type of x (e.g., x has data type int64 and the default data type is int32,
         or x has data type uint64 and the default data type is int64), the returned array must have the same data type as x.
        if x has a floating-point data type, the returned array must have the default floating-point data type.
        if x has a signed integer data type (e.g., int16), the returned array must have the default integer data type.
        if x has an unsigned integer data type (e.g., uint16), the returned array must have an unsigned integer data type
         having the same number of bits as the default integer data type (e.g., if the default integer data type is int32, 
         the returned array must have a uint32 data type).
        If the data type (either specified or resolved) differs from the data type of x, the input array should be cast 
        to the specified data type before computing the product. Default: None.
    :type dtype: dtype
    :param keepdims: if True, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, 
    accordingly, the result must be compatible with the input array (see Broadcasting). Otherwise, if False, the reduced axes 
    (dimensions) must not be included in the result. Default: False.
    :type keepdims: bool

    Returns
    :return out: if the product was computed over the entire array, a zero-dimensional array containing the product; otherwise, 
    a non-zero-dimensional array containing the products. The returned array must have a data type as described by the dtype 
    parameter above.
    :type out: array
    """
    return _cur_framework.prod(x, axis, dtype, keepdims)


# Extra #
# ------#
