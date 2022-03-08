from typing import List
from test_framework import generic_test

# added
import bintrees
import math

# copied from the solution
class Number:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.val = a + b * math.sqrt(2)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

# TODO: add my code
# def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
#     return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
