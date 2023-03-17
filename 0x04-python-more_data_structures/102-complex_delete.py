#!/usr/bin/python3
# 2-uniq_add.py
# Nneoma Obidegwu <obidegwu.nneoma@yahoo.com>

def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary."""
    while value in a_dictionary.values():
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                break

    return (a_dictionary)
