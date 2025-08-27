from plates import is_valid

def test_startdigit():
    assert is_valid("00ad") == False
    assert is_valid("asd34") == True
    assert is_valid("324") == False

def test_digitcenter():
    assert is_valid("as90ds") == False

def test_valid():
    assert is_valid("asdf90") == True

def test_start0():
    assert is_valid("sfa0j") == False
    assert is_valid("as0123") == False

def test_length():
    assert is_valid("asf21043") == False
    assert is_valid("asf24") == True

def test_isalphanum():
    assert is_valid("sad.0") == False
    assert is_valid("sf/sa") == False

def test_startalpha():
    assert is_valid("assk") == True
    assert is_valid("as34") == True
    assert is_valid("23sd4") == False

