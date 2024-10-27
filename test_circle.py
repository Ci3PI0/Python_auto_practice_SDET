import math
import pytest
import class_test as shapes


class TestCircle:

    def setup_method(self, method):
        print(f'Setting up {method}')
        print(shapes.Circle(15))
        self.circle = shapes.Circle(15)

    def teardown_method(self, method):
        print(f'Tearing down {method}')

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected

    def test_two(self):
        assert True
