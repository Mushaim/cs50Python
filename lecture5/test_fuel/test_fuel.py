from fuel import convert, gauge
import pytest

def test_zerodivision():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ZeroDivisionError):
        convert("32/0")

def test_value():
    with pytest.raises(ValueError):
        convert("cat/20")
    with pytest.raises(ValueError):
        convert("200/12")

def test_negative():
    with pytest.raises(ValueError):
        convert("-2/4")
    with pytest.raises(ValueError):
        convert("3/-4")

def test_convert():
    assert convert("2/10") == 20
    assert convert("45/100") == 45

def test_E():
    assert gauge(0.5) == "E"
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_f():
    assert gauge(99.8) == "F"
    assert gauge(99) == "F"

def test_valid():
    assert gauge(45) == "45%"
