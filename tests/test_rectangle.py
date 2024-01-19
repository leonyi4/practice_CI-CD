import pytest

import source.shapes as shapes


def test_area(my_rectangle):

    assert my_rectangle.area() == 1*2

def test_perimeter(my_rectangle):  

    assert my_rectangle.perimeter() == (1*2) + (2*2)

def test_not_equal(my_rectangle,chill_rectangle):

    assert my_rectangle != chill_rectangle