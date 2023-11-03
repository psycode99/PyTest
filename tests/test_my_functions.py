import pytest
import time
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(x=3, y=6)
    assert result == 9

def test_add_strings():
    result = my_functions.add('hello ', 'world')
    assert result == 'hello world'

def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2

def test_divide_by_zero():
    my_functions.divide_zero(2, 'kk')

def test_divide_by_zero_2():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(2, 0)
    with pytest.raises(TypeError):
        my_functions.divide(2, 'kk')


# MARKING
@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(2, 2)
    assert result == 1

@pytest.mark.skip(reason='feature is in alpha')
def test_add2():
    assert my_functions.add(1,2) == 3

@pytest.mark.xfail(reason='we cannot divide by zero')
def test_zero_division_fail():
    my_functions.divide(1, 0)
