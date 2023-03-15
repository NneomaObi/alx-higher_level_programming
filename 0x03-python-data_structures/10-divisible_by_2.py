#!/usr/bin/python3
# 6-print_matrix_integer.py
# Nneoma Obidegwu <obidegwu.nneoma@yahoo.com>

def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)
    return (multiples)
