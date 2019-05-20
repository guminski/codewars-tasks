from unittest import TestCase
"""
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.
"""

def add_binary(a,b):
    return bin(a+b)[2:]

TestCase().assertEqual(add_binary(1,1),"10")
TestCase().assertEqual(add_binary(0,1),"1")
TestCase().assertEqual(add_binary(1,0),"1")
TestCase().assertEqual(add_binary(2,2),"100")
TestCase().assertEqual(add_binary(51,12),"111111")