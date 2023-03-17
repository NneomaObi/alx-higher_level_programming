#!/usr/bin/python3
# 2-uniq_add.py
# Nneoma Obidegwu <obidegwu.nneoma@yahoo.com>

def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set."""
    return (set_1 ^ set_2)
