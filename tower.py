from unittest import TestCase
"""
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *
For example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]

"""


def tower_builder(n_floors):
    tower = []
    for i in range(1, n_floors + 1):
        spaces = ''.join(' ') * (n_floors - i)
        stars = ''.join('*') * ((i * 2) - 1)
        tower.append(spaces + stars + spaces)
    return tower


TestCase().assertEqual(tower_builder(3), ['  *  ', ' *** ', '*****'])
TestCase().assertEqual(tower_builder(1), ['*', ])
TestCase().assertEqual(tower_builder(2), [' * ', '***'])
