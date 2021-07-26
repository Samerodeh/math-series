from math_series import __version__
from math_series.series import *


def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci_1():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_2():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_3():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected  


def test_lucas_1():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_2():
    actual = lucas(1)
    expected = 3
    assert actual == expected

def test_lucas_3():
    actual = lucas(2)
    expected = 5
    assert actual == expected 

    
def test_sum_series_1():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series_2():
    actual = sum_series(0,0)
    expected = 0
    assert actual == expected

def test_sum_series_3():
    actual = sum_series(0,0,1)
    expected = 0
    assert actual == expected