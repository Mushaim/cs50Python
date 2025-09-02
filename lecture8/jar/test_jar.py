from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        Jar(-3)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    assert str(jar) == ""
    with pytest.raises(ValueError):
        jar.deposit(6)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.withdraw(6)
