def test_area(my_fixture):
    assert my_fixture.area() == 20 * 10


def test_perimeter(my_fixture):
    assert my_fixture.perimeter() == (10 * 2) + (20 * 2)
