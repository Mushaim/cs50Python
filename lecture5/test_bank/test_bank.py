from bank import value

def test_hello():
    assert value("hello david") == 0

def test_h():
    assert value("hi david") == 20
    assert value("hoye") == 20

def test_no_greeting():
    assert value("welcome") == 100
    assert value("woohoo") == 100

def test_lower():
    assert value("hi") == 20
    assert value("what") == 100

def test_upper():
    assert value("Hi") == 20
    assert value("WHAT") == 100
