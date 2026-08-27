import pytest

from calculadora import soma, sub, multi, divi

def test_soma():
    assert soma(5, 5) == 10

def test_sub():
    assert sub(2, 6) == 8

def test_multi():
    assert multi(4, 2) == 8

def test_divi():
    assert divi(10, 2) == 5