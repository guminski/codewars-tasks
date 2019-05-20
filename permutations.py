from unittest import TestCase
from itertools import permutations as perm

"""In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
"""


def permutations(string):
    return sorted(set(map(lambda x: "".join(x), list(perm(string, len(string))))))


TestCase().assertEqual(sorted(permutations('a')), ['a'])
TestCase().assertEqual(sorted(permutations('ab')), ['ab', 'ba'])
TestCase().assertEqual(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
