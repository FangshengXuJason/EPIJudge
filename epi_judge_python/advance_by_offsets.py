from typing import List

from sqlalchemy import false, true

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    # TODO - you fill in here.
    furthest, i, last_index = 0 , 0, len(A) -1
    while i <= furthest and furthest < last_index:
        furthest = max(furthest, A[i] + i)
        i += 1
    return furthest >= last_index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
