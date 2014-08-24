__author__ = 'julz'
# Think of binary numbers: sequences of 0's and 1's.
# How many n-digit binary numbers are there that don't have
# two adjacent 1 bits?
# For example, for three-digit numbers,
# five of the possible eight combinations meet the criteria:
# 000, 001, 010, XXX011, 100, 101, XXX110, XXX111.

# What is the number for sequences of length 4, 5, 10, n?

# http://codekata.com/kata/kata15-a-diversion/


def has_adjacent_digits(binarystring):
    return '11' in binarystring

def generate_binary_string(dec):
    """
     Turn a decimal number into binary, but as a string.
    """
    return str(bin(dec))[2:]


def count_non_adjacent_digits(n,total=0):
    """
    Note: simple recursion
    Naive: doesn't cache nor optimized..
    """
    if n>=0:
        n_has_no_adjacent_digits = not has_adjacent_digits(generate_binary_string(n))
        return count_non_adjacent_digits(n-1,total+n_has_no_adjacent_digits)
    else:
        return total
