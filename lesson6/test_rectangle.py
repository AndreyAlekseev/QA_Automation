from .Figure import Figure


class Rectangle(Figure):
    def __init__(self, name, side_a, side_b):
        super().__init__(name, angles=4)
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        res = self.side_a * self.side_b
        return res

    def perimeter(self):
        res = 2*(self.side_a + self.side_b)
        return res

    def add_area(self, obj):
        if not isinstance(obj, Rectangle):
            raise Exception("Argument must be instance of Rectangle class")
        else:
            return obj.perimeter() + self.perimeter()


""""test_triangle"""

new_rectangle = Rectangle('test_rectangle', 10, 20)


def test_create_rectangle():
    assert isinstance(new_rectangle, Rectangle)


def test_sides_of_rectangle():
    assert new_rectangle.side_a == 10 and new_rectangle.side_b == 20


def test_prop_of_rectangle():
    assert new_rectangle.name == 'test_rectangle' and new_rectangle.angles == 4


def test_area_of_rectangle():
    assert new_rectangle.area() == 200


def test_perimeter_of_rectangle():
    assert new_rectangle.perimeter() == 60


def test_add_area():
    triangle_two = Rectangle('large_rectangle', 30, 20,)
    assert new_rectangle.add_area(triangle_two) == 160
