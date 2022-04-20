from typing import List

from sqlalchemy import false, true

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    carry = true
    for i in reversed(range(len(A))):
        if A[i] is 9 and carry:
            A[i] = 0
        elif carry: # digit is not 9
            A[i] += 1
            return A
    # need one more digit
    if carry:
        A[0] = 1
        A.append(0)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
