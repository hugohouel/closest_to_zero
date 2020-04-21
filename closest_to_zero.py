from functools import reduce


def closest_to_zero(arr: 'Integer iterable') -> int:
    """ Given an array of integers, returns the closest number to zero.

    Arguments:
    arr: any python integer iterable such as list, set, tuple...

    Implementation details:
    If the closest number in arr could be either negative or positive, returns the positive one.
    If arr is empty or of the wrong type, returns 0.
    """

    def positive_min(closest: int, x: int) -> int:
        """ Lambda to be called in the reduce operation."""
        if abs(x) < abs(closest) or (closest < 0 and x == -closest):
            return x
        return closest

    try:
        return reduce(positive_min, arr)
    except TypeError:
        return 0
