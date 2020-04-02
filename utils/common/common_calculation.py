import math


@staticmethod
def round_up(value, multiplier=1, minimum_value=0):
    """Round up the value to the next multiple of 'multiplier' with a minimum of 'minimum_value'"""
    value = max(value, minimum_value)
    return math.ceil(value/multiplier) * multiplier


@staticmethod
def round_down(value, multiplier=1, minimum_value=0):
    """Round up the value to the next multiple of 'multiplier' with a minimum of 'minimum_value'"""
    value = max(value, minimum_value)
    return math.floor(value/multiplier) * multiplier


