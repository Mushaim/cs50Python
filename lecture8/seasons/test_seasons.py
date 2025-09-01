from seasons import get_age
import pytest

def test_valid():
    with pytest.raises(SystemExit):
        get_age("Semptember,9 2001")

def test_last_year():
    assert get_age("2024-8-31") == "Five hundred twenty-five thousand, six hundred minutes"



