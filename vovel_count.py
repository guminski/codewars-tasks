from unittest import TestCase
"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.
"""


def getCount(inputStr):
    num_vowels = 0
    for e in 'aeiou':
        num_vowels += inputStr.count(e)
    return num_vowels

TestCase().assertEqual(getCount("abracadabra"), 5)