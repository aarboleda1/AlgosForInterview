import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))

"""11.10 Find the duplicate and missing elements

If an array contains n - 1 integers, each between 0 and n - 1, inclusive, and
all number in the array are distinct, then it must be the case that exactly one
number between 0 and n - 1 is absent.

Basic Algorithm:
For each element, perform a circular swap and place the element n at the correct
index.
A = [0, 2, 2, 1]
[0, 1, 2, 2]
"""
def swap(i, j, A):
    A[j], A[i] = A[i], A[j]

def find_duplicate_missing(A):
    last_mismatch = 0
    for i in range(len(A)):
        while i != A[i] and A[A[i]] != A[i]:
            swap(i, A[i], A)

    for i in range(len(A)):
        if i != A[i]:
            return DuplicateAndMissing(A[i], i)

def find_duplicate_missing(A):

    # Compute the XOR of all numbers from 0 to |A| - 1 and all entries in A.
    miss_XOR_dup = functools.reduce(lambda v, i: v ^ i[0] ^ i[1], enumerate(A),
                                    0)

    # We need to find a bit that's set to 1 in miss_XOR_dup. Such a bit must
    # exist if there is a single missing number and a single duplicated number
    # in A.
    #
    # The bit-fiddling assignment below sets all of bits in differ_bit
    # to 0 except for the least significant bit in miss_XOR_dup that's 1.
    differ_bit, miss_or_dup = miss_XOR_dup & (~(miss_XOR_dup - 1)), 0
    for i, a in enumerate(A):
        # Focus on entries and numbers in which the differ_bit-th bit is 1.
        if i & differ_bit:
            miss_or_dup ^= i
        if a & differ_bit:
            miss_or_dup ^= a

    # miss_or_dup is either the missing value or the duplicated entry.
    # If miss_or_dup is in A, miss_or_dup is the duplicate;
    # otherwise, miss_or_dup is the missing value.
    return (DuplicateAndMissing(miss_or_dup, miss_or_dup ^ miss_XOR_dup)
            if miss_or_dup in A else DuplicateAndMissing(
                miss_or_dup ^ miss_XOR_dup, miss_or_dup))


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_missing_element.py",
            'find_missing_and_duplicate.tsv',
            find_duplicate_missing,
            res_printer=res_printer))
