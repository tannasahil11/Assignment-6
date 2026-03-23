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
    