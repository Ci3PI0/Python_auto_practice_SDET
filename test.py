import pytest


def add(firts_num, second_num):
    if int == type(firts_num) and type(second_num) == int:
        if firts_num == 0 or second_num == 0:
            raise ValueError
        else:
            return firts_num + second_num
    else:
        return firts_num + second_num


def test_add():
    with pytest.raises(ValueError):
        add(3, 0)
    # result = add(5, 1)
    # assert 1 + 5 == result
    # # pass


def test_add2():
    result = add(3, 1)
    assert result == 4

def test_string_add():
    result = add('Hello ', 'world')
    assert result == 'Hello world'
