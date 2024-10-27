import pytest
import class_test as shape

@pytest.fixture
def my_fixture():
    return shape.Rectangle(20, 10)

