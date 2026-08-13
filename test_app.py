from app import add, multiply


def test_add():
    assert add(10, 20) == 40


def test_multiply():
    assert multiply(10, 20) == 200
