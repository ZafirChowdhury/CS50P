from working import convert as c
import pytest


def test_errors():
    with pytest.raises(ValueError):
        c("9:60 AM to 5:60 PM")

    with pytest.raises(ValueError):
        c("9 AM - 5 PM")

    with pytest.raises(ValueError):
        c("09:00 AM - 17:00 PM")


def test_with_colon():
    assert c("9 AM to 5 PM") == "09:00 to 17:00"
    assert c("10 PM to 8 AM") == "22:00 to 08:00"


def test_without_colon():
    assert c("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert c("10:30 PM to 8:50 AM") == "22:30 to 08:50"
