from plates import is_valid

def test_is_valid():
    assert is_valid("HELLO") == True
    assert is_valid("Hello, World") == False
    assert is_valid("Goodbye") == False
    assert is_valid("Hey012") == False
    assert is_valid("AA2A22") == False
    assert is_valid("213214") == False
    assert is_valid("inc0rr") == False
    assert is_valid("BGH2!") == False
