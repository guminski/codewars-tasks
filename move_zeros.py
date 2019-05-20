from unittest import TestCase

'''
    Write an algorithm that takes an iterable and moves all of the zeros to the end,
    preserving the order of the other elements.

    move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
'''


def move_zeros(iterable):
    main = []
    tail = []
    for index, elem in enumerate(iterable):
        if elem == 0 or elem == 0.0:
            if type(elem) == int or type(elem) == float:
                tail.append(elem)
            else:
                main.append(elem)
        else:
            main.append(elem)
    return main + tail


TestCase().assertEqual(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]), [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
TestCase().assertEqual(move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
                       [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
TestCase().assertEqual(move_zeros(["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
                       ["a", "b", "c", "d", 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
TestCase().assertEqual(
    move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]),
    ["a", "b", None, "c", "d", 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
TestCase().assertEqual(move_zeros([0, 1, None, 2, False, 1, 0]), [1, None, 2, False, 1, 0, 0])
TestCase().assertEqual(move_zeros(["a", "b"]), ["a", "b"])
TestCase().assertEqual(move_zeros(["a"]), ["a"])
TestCase().assertEqual(move_zeros([0, 0]), [0, 0])
TestCase().assertEqual(move_zeros([0]), [0])
TestCase().assertEqual(move_zeros([False]), [False])
TestCase().assertEqual(move_zeros([]), [])
