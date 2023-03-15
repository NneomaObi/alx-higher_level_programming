#!/usr/bin/python3
# 0-square_matrix_simple.py
# Nneoma Obidegwu <obidegwu.nneoma@yahoo.com>

def uniq_add(my_list=[]):
    """Add all unique integers in a list (once for each integer)."""
    result = 0
    for x in set(my_list):
        result += x
    return (result)
