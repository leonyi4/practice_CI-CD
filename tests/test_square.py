import pytest
import source.shapes as shapes


@pytest.mark.parametrize("side_length, expected_area",[(5,25),(2,4),(3,9),(9,81)])
def test_multiple_square_areas(side_length,expected_area):

    assert shapes.Square(side_length).area() == expected_area

@pytest.mark.parametrize("side_length, expected_perimeter",[(5,20),(3,12),(4,16),(9,36)])
def test_multiple_square_perimeter(side_length,expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter