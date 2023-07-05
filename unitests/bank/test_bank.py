from bank import value

def test_value():
    assert value("Yo homie?") == 100
    assert  value("Hola!!") == 20
    assert  value("How are you? What's going on ? ") == 20