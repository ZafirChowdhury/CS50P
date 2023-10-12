from twttr import shorten as s

def test():
    assert s("Twitter") == "Twttr"
    assert s("What's your name?") == "Wht's yr nm?"
    assert s("CS50") == "CS50"
    assert s("APPLE") == "PPL"