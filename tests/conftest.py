import pytest
import source.shapes as shapes


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(1,2)

@pytest.fixture
def chill_rectangle():
    return shapes.Rectangle(5,6)