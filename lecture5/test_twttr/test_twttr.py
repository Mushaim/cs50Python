from twttr import shorten
import pytest

def test_lower():
    assert shorten("twitter") == "twttr"

def test_upper():
    assert shorten("TWITTER") == "TWTTR"

def test_number():
    assert shorten("twitter01") == "twttr01"

def test_punctuation():
    assert shorten("twitter!") == "twttr!"
