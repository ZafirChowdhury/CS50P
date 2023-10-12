from um import count as c

def test_given():
    assert c("um") == 1
    assert c("um?") == 1
    assert c("um, thaks, um") == 2


def test_numbers():
    assert c("123") == 0


def test_line_of_ums():
    assert c("umumumumum") == 0


def test_case_insensitivety():
    assert c("UM") == 1