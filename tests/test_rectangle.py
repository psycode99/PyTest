import pytest
import source.shapes as shapes

# FIXTURES
@pytest.fixture
def my_rect():
    return shapes.Rectangle(20, 10)


def test_area(my_rect):
    assert my_rect.area() == 20 * 10


def test_perimeter(my_rect):
    assert my_rect.perimeter() == (20 * 2) + (10 * 2)