from jar import Jar
import pytest


def test_invalid_capacity_setter_while_making_obj():
    with pytest.raises(ValueError, match="Invalid capacity"):
        jar = Jar(-2)

def test_deposit(capfd):
    jar = Jar()
    jar.deposit(12)
    print(jar)
    captured = capfd.readouterr()
    assert captured.out.strip() == "🍪" * 12

    jar = Jar(11)
    with pytest.raises(ValueError, match="Capacity overflow"):
        jar.deposit(12)

def test_withdraw(capfd):
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(6)
    print(jar)
    captured = capfd.readouterr()
    assert captured.out.strip() == "🍪" * 6

    with pytest.raises(ValueError, match="Not enough cookies"):
        jar.withdraw(10)

def test_str(capfd):
    jar = Jar(20)
    jar.deposit(12)
    print(jar)
    captured = capfd.readouterr()
    assert captured.out.strip() == "🍪" * 12
