from unittest import TestCase

'''
    There is a queue for the self-checkout tills at the supermarket.
    Your task is write a function to calculate the total time required for all the customers to check out!

    The function has two input variables:

    customers: an array (list in python) of positive integers representing the queue.
    Each integer represents a customer, and its value is the amount of time they require to check out.
    n: a positive integer, the number of checkout tills.

    The function should return an integer, the total time required.
'''

def queue_time(customers, n):
    pass


TestCase().assertEqual(queue_time([], 1), 0, msg="wrong answer for case with an empty queue")
TestCase().assertEqual(queue_time([5], 1), 5, msg="wrong answer for a single person in the queue")
TestCase().assertEqual(queue_time([2], 5), 2, msg="wrong answer for a single person in the queue")
TestCase().assertEqual(queue_time([1,2,3,4,5], 1), 15, msg="wrong answer for a single till")
TestCase().assertEqual(queue_time([1,2,3,4,5], 100), 5, msg="wrong answer for a case with a large number of tills")
TestCase().assertEqual(queue_time([2,2,3,3,4,4], 2), 9, msg="wrong answer for a case with two tills")
