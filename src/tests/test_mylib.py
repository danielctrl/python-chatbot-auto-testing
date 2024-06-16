import mylib.calc as lib

def test_sum_1():
    assert lib.sum(1, 1) == 2, "1+1 should be 2"

def test_sum_wrong():
    assert lib.sum(1, 1) != 2, "1+1 shouldn't be 1"