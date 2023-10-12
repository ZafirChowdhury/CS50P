from numb3rs import validate as v

def test_true():
    assert v("1.1.1.1") == True
    assert v("127.0.0.1") == True
    assert v("255.255.255.255") == True
    assert v("103.251.244.46") == True
    assert v("154.166.79.116") == True


def test_false():
    assert v("512.512.512.512") == False
    assert v("1.2.3.1000") == False
    assert v("cat") == False
    assert v("cat.cat.cat.cat") == False
    assert v("275.3.6.28") == False
    assert v("275.3.6.28.69") == False
    assert v("200") == False
    assert v("75.456.76.65") == False

