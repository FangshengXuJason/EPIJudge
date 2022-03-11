from sqlalchemy import false, true
from test_framework import generic_test


def reverse(x: int) -> int:
    # TODO - you fill in here.

    res = x % 10
    x = x//10
    while x:
        res = res * 10 + x % 10
        x = x//10

    return  -res if x < 0 else res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
