import pytest
import source.shapes as shapes

# PARAMETRIZE 
@pytest.mark.parametrize('side_length, expected_area', [(5, 25), (4, 16), (10, 100)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area

@pytest.mark.parametrize('side_length, expected_perimeter', [(3, 12), (5, 20), (4, 16)])
def test_multiple_square_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter