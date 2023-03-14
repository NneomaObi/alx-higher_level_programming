#!/usr/bin/python3
# 6-print_matrix_integer.py
# Nneoma Obidegwu <obidegwu.nneoma@yahoo.com>

def multiple_returns(sentence):
    """Returns the length of a string and its first character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
