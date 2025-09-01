from numb3rs import validate
import pytest

def test_separater():
    assert validate("12.32") == False
    assert validate("12.32.12") == False
    assert validate("43..123.432") == False
    assert validate("34.23.12.43") == True

def test_range():
    assert validate("23.422.12.43") == False
    assert validate("23.212.324.32") == False
    assert validate("21.43.0.1") == True

