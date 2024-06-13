from fuel import convert, gauge
import pytest

def test_standard_convert():
    assert convert("1/2") == 50
    assert convert("1/3") == 33
    assert convert("1/100") == 1
    assert convert("1/1000") == 0

def test_convert_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("3/2")

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(.5) == "E"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
