from unittest import TestCase

'''
    The rgb() method is incomplete. Complete the method so that passing in RGB decimal values
    will result in a hexadecimal representation being returned.
    The valid decimal values for RGB are 0 - 255.
    Any (r,g,b) argument values that fall out of that range
    should be rounded to the closest valid value.

    The following are examples of expected output values:

    rgb(255, 255, 255) # returns FFFFFF
    rgb(255, 255, 300) # returns FFFFFF
    rgb(0,0,0) # returns 000000
    rgb(148, 0, 211) # returns 9400D3
'''

def rgb(*args):
    return ''.join('%02x' % max(0, min(e, 255)) for e in args).upper()

TestCase().assertEqual(rgb(0,0,0),"000000", "testing zero values")
TestCase().assertEqual(rgb(1,2,3),"010203", "testing near zero values")
TestCase().assertEqual(rgb(255,255,255), "FFFFFF", "testing max values")
TestCase().assertEqual(rgb(254,253,252), "FEFDFC", "testing near max values")
TestCase().assertEqual(rgb(-20,275,125), "00FF7D", "testing out of range values")
