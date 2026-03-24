import pytest
from mymath.factorial import factorial


def test_0():
    assert factorial(0) == 1

def test_3():
    assert factorial(3) == 6

def test_5():
    assert factorial(5) == 120

def test_negative():
    with pytest.raises(ValueError):
        factorial(-1)

def test_float():
    with pytest.raises(TypeError):
        factorial(0.5)