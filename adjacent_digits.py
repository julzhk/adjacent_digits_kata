__author__ = 'julz'
# Think of binary numbers: sequences of 0's and 1's.
# How many n-digit binary numbers are there that don't have
# two adjacent 1 bits?
# For example, for three-digit numbers,
# five of the possible eight combinations meet the criteria:
# 000, 001, 010, XXX011, 100, 101, XXX110, XXX111.

# What is the number for sequences of length 4, 5, 10, n?

# http://codekata.pragprog.com/2007/01/code_kata_fifte.html#more


def has_adjacent_digits(binarystring):
    return '11' in binarystring

def generate_binary_string(dec):
    return str(bin(dec))[2:]

def count_non_adjacent_digits(n):
    total = 0
    for i in xrange(0,n+1):
        if not has_adjacent_digits(generate_binary_string(i)):
            total +=1
    return total