from plates import is_valid as v

def test_len():
    assert v("CS50") == True
    assert v("C") == False
    assert v("CS50P/CS50W") == False

def test_starts_with():
    assert v("50CS") == False
    assert v("CS") == True

def test_middle_number():
    assert v("AAA222") == True
    assert v("AAA22A") == False

def test_periods():
    assert v("C.S.5.0") == False
    assert v("CS 50") == False
    assert v("CS!50") == False
    assert v("CS.50") == False

def test_starts_with_zero():
    assert v("CS05") == False

def test_alphanumeric():
    assert v("ab@%#") == False
    assert v("####") == False
    assert v(".Polti") == False
    assert v("123456") == False