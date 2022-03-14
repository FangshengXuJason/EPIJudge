import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s: list):
    stack = []
    word = ''
    for letter in s:
        if letter == ' ':
            stack.append(word)
            word = ''
            continue
        word = word + letter
    if word: # the check is possibly unecessary
     stack.append(word)

    res = ' '.join(reversed(stack))

    res = list(res)
    # TODO: Why does it work? It is supposed to work!
    return res

# def reverse_words(s):
#     def reverse_range(s, start, finish):
#         while start < finish:
#             s[start], s[finish] = s[finish], s[start]
#             start, finish = start + 1, finish - 1

#     # First, reverse the whole string.
#     reverse_range(s, 0, len(s) - 1)

#     start = 0
#     while True:
#         finish = start
#         while finish < len(s) and s[finish] != ' ':
#             finish += 1
#         if finish == len(s):
#             break
#         # Reverses each word in the string.
#         reverse_range(s, start, finish - 1)
#         start = finish + 1
#     # Reverses the last word.
#     reverse_range(s, start, len(s) - 1)


# if s is a string,
# I have this solution: ' '.join(reversed(s.split(' ')))

@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
