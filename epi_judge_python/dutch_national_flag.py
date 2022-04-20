import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # TODO - you fill in here.
    # MORE INTUITIVE SOLUTION

    # next_less, next_larger = 0, len(A) - 1
    # p_val = A[pivot_index]

    # # make "less than" partition
    # for i in range(len(A)):
    #     if A[i] < p_val: # swap
    #         A[i], A[next_less] = A[next_less], A[i]
    #         next_less += 1

    # # make "larger than" partition
    # for i in reversed(range(len(A))):
    #     if A[i] > p_val:
    #         A[i], A[next_larger] = A[next_larger], A[i]
    #         next_larger -= 1

    # DIFFERENT SOLUTION
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)
    # keep iterating as long as there is an unclassified element
    while equal < larger:
        if A[equal] < pivot:
            A[equal], A[smaller] = A[smaller], A[equal]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] is pivot:
            equal += 1
        else: # A[equal] > pivot
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]




@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
