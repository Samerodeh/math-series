from math_series import __version__
from math_series.series import *


def test_version():
    assert __version__ == '0.1.0'

def test1_fibonacci():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test2_fibonacci():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test3_fibonacci():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected  


def test1_lucas():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test2_lucas():
    actual = lucas(1)
    expected = 3
    assert actual == expected

def test3_lucas():
    actual = lucas(2)
    expected = 5
    assert actual == expected 

    
def test1_sum_series():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test2_sum_series():
    actual = sum_series(0,0)
    expected = 0
    assert actual == expected

def test3_sum_series():
    actual = sum_series(0,0,1)
    expected = 0
    assert actual == expected