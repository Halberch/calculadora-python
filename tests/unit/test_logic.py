from logic import add, subtract

def test_add():
    assert add(2, 2) == 4
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5