from um import count

def test_counts():
    assert count("Hi, um, hello") == 1
    assert count("what um, is um what") == 2

def test_zero_count():
    assert count("What!!") == 0
    assert count("Hi this is cs50") == 0

def test_word_with_um():
    assert count("Yummy") == 0
    assert count("This is um maximum um number of um, letters") == 3

def test_case():
    assert count("Um is this uM") == 2
    assert count("UM are you sure this is UM it?") == 2
