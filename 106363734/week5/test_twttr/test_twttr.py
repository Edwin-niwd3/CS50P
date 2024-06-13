from twttr import shorten

def test_shorten():
    assert shorten("Hello") == "Hll"
    assert shorten("Hi There") == "H Thr"
    assert shorten("What's 1?") == "Wht's 1?"
    assert shorten("WHAT IS HAPPENING") == "WHT S HPPNNG"
