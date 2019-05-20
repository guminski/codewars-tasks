from unittest import TestCase

"""
Compare two strings by comparing the sum of their values (ASCII character code).

    For comparing treat all letters as UpperCase
    null/NULL/Nil/None should be treated as empty strings
    If the string contains other characters than letters, treat the whole string as it would be empty

Your method should return true, if the strings are equal and false if they are not equal.
Examples:

"AD", "BC"  -> equal
"AD", "DD"  -> not equal
"gf", "FG"  -> equal
"zz1", ""   -> equal (both are considered empty)
"ZzZz", "ffPFF" -> equal
"kl", "lz"  -> not equal
null, ""    -> equal
"""


def compare(s1, s2):
    a, b = (sum(ord(x) for x in s.upper()) if s and s.isalpha() else '' for s in (s1, s2))
    return a == b


TestCase().assertEqual(compare("AD", "BC"), True, "\'AD\' vs \'BC\'")
TestCase().assertEqual(compare("AD", "DD"), False, "\'AD\' vs \'DD\'")
TestCase().assertEqual(compare("gf", "FG"), True, "\'gf\' vs \'FG\'")
TestCase().assertEqual(compare("Ad", "DD"), False, "\'Ad\' vs \'DD\'")
TestCase().assertEqual(compare("zz1", ""), True, "\'zz1\' vs \'\'")
TestCase().assertEqual(compare("ZzZz", "ffPFF"), True, "\'ZzZz\' vs \'ffPFF\'")
TestCase().assertEqual(compare("kl", "lz"), False, "\'kl\' vs \'lz\'")
TestCase().assertEqual(compare(None, ""), True, "\'<null>\' vs \'\'")
TestCase().assertEqual(compare("!!", "7476"), True, "\'!!\' vs \'7476\'")
TestCase().assertEqual(compare("##", "1176"), True, "\'##\' vs \'1176\'")
