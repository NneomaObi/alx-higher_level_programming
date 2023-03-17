#!/usr/bin/python3
# 2-uniq_add.py
# Nneoma Obidegwu <obidegwu.nneoma@yahoo.com>

def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys."""
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
