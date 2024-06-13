from bank import value

def test_value():
    assert value("Hello") == 0
    assert value("hey") == 20
    assert value("What") == 100
    assert value("lowercase") == 100
    assert value("Heyo") == 20
