from fuel import convert as c
from fuel import gauge as g
from pytest import raises

def test_convert():
    assert c("1/4") == 25
    assert c("2/4") == 50
    assert c("3/4") == 75
    assert c("4/4") == 100

    with raises(ValueError):
        c("Cat/Dog")

    with raises(ZeroDivisionError):
        c("1/0")


def test_gauge():
    assert g(25) == "25%"
    assert g(50) == "50%"
    assert g(1) == "E"
    assert g(99) == "F"