def func(x):
    return x + 1


def test_case1():
    assert func(4) == 5

def test_case2():
    assert func(6) == 7

def test_case3():
    assert func(10) != 25

def test_case4():
    assert func(20) != 25
