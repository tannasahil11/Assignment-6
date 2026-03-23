"""
Tests the fibonnaci module
"""
import pytest
from fibonacci import Fibonacci

def test_value_error_with_str():
    """Raises ValueError if the user enters a string"""
    with pytest.raises(ValueError):
        obj = Fibonacci("test")

def test_value_error_with_float():
    """Raises ValueError if the user enters a floating point number"""
    with pytest.raises(ValueError):
        obj = Fibonacci(5.6)

def test_output_for_value_0():
    """Test iterator output for base value of 0 steps"""
    assert list(Fibonacci(0)) == [0]

def test_output_for_value_1():
    """Test iterator output for 1 step in the sequence"""
    assert list(Fibonacci(1)) == [0, 1]

def test_output_for_value_2():
    """Test iterator output for 2 steps in the sequence"""
    assert list(Fibonacci(2)) == [0, 1, 1]

def test_output_for_value_4():
    """Test iterator output for 4 steps in the sequence"""
    assert list(Fibonacci(4)) == [0, 1, 1, 2, 3]    

def test_output_for_value_10():
    """Test iterator output for 10 steps in the sequence"""
    assert list(Fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]  

def test_output_for_negative_value():
    """Test iterator output for negative steps in the sequence"""
    assert list(Fibonacci(-10)) == []  