import fuel
import pytest

def test_convert():

    assert fuel.convert("1/4") == 25
    assert fuel.convert("2/4") == 50
    assert fuel.convert("3/4") == 75
    assert fuel.convert("4/4") == 100

def test_gauge():
    assert fuel.gauge(0.5) == 'E'
    assert fuel.gauge(0) == 'E'
    assert fuel.gauge(1) == 'E'

    assert fuel.gauge(99.5) == 'F'
    assert fuel.gauge(99) == 'F'
    assert fuel.gauge(100) == 'F'

    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(75) == "75%"
    assert fuel.gauge(35) == "35%"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):
        fuel.convert("2/1")