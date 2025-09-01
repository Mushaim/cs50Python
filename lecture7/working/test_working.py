from working import convert
import pytest

def test_hour():
    with pytest.raises(ValueError):
        convert("13:23 AM to 11:23 PM")

def test_min():
    with pytest.raises(ValueError):
        convert("1:23 AM to 11:65 PM")

def test_format():
    with pytest.raises(ValueError):
        convert("11:23AM to 11:23 PM")
    with pytest.raises(ValueError):
        convert("1:23 AM 11:23 PM")

def test_zone():
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("1:65 AM to 5:00 PM")

def test_valid():
    assert convert("12 AM to 5 PM") == "00:00 to 17:00"
