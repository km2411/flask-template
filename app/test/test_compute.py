from compute import Compute


def test_fibonacci():
    assert Compute.fibonacci(3) == 2
    assert Compute.fibonacci(-8) == -21


def test_ackermann():


def test_factorial():
    assert Compute.factorial(3)==6
    assert Compute.factorial(0)==1
