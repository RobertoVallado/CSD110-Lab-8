import util

from src.lab8_1 import fib_list

def test_raises_assertion_on_non_integer():
    util.expect_assertion_error(lambda: fib_list(1.5), 'fib_list', 'first', 'is not an integer')
def test_raises_correct_assertion_error_message_on_non_integer():
    util.assert_assertion_message_equals(lambda: fib_list(1.5), "max must be an integer 0 or greater", "first", "is not an integer")

def test_raises_assertion_on_negative_integer():
    util.expect_assertion_error(lambda: fib_list(-1), 'fib_list', 'first', 'is negative')
def test_raises_correct_assertion_error_message_on_negative_integer():
    util.assert_assertion_message_equals(lambda: fib_list(-1), "max must be an integer 0 or greater", "first", "is negative")


def test_0():
    expected = [0]
    assert expected == fib_list(0), "fib_list(0) must be " + str(expected)

def test_1():
    expected = [0, 1, 1]
    assert expected == fib_list(1), "fib_list(1) must be " + str(expected)

def test_2():
    expected = [0, 1, 1, 2]
    assert expected == fib_list(2), "fib_list(2) must be " + str(expected)

def test_3():
    expected = [0, 1, 1, 2, 3, 5, 8]
    assert expected == fib_list(10), "fib_list(10) must be " + str(expected)

def test_100():
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert expected == fib_list(100), "fib_list(10) must be " + str(expected)
