import pytest
import time
import source.my_functions as my_functions

def test_add():
    results = my_functions.add_numbers(1, 2)
    assert results == 3 

def test_subtract():
    results = my_functions.subtract_numbers(1, 2)
    assert results == -1

def test_multiply():
    results = my_functions.multiply_numbers(1, 2)
    assert results == 2

def test_divide():
    results = my_functions.divide_numbers(1, 2)
    assert results == 0.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide_numbers(1, 0)

@pytest.mark.slow   
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide_numbers(10,5)
    assert result == 2

@pytest.mark.skip(reason="Not implemented yet")
def test_add():
    assert my_functions.add_numbers(1,3)==4

@pytest.mark.xfail(reason= "Can't divide by zero :)")
def test_divide_by_zero_broken():
    my_functions.divide_numbers(1,0)==0      

def test_strings():
    results = my_functions.add_numbers("Hello", "World")
    assert results == 'HelloWorld'