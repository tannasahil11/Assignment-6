import pytest
from fibonacci import Fibonacci

def test_value_error_with_str():
    with pytest.raises(ValueError):
        obj = Fibonacci("test")

def test_value_error_with_float():
    with pytest.raises(ValueError):
        obj = Fibonacci(5.6)