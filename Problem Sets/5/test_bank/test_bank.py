from bank import value as v

def test():
    assert v("") == 100
    assert v("Hello") == 0
    assert v("Hello, Newman") == 0
    assert v("How are you doing?") == 20
    assert v("What's happening") == 100
    assert v("HELLO") == 0
    assert v("  hello ") == 0
    assert v("H....ey you!") == 20