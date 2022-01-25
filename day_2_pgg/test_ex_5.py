from day_2_pgg.ex_5 import more_than

def test_empty_string():
    assert more_than('', 0) == set()

def test_small_caps_string():
    assert more_than('ala ma kota a kot ma ale', 3) == {'a', ' '}

def test_mixed_case_string():
    assert more_than('BBbbBBaac') == {'a', 'b'}
