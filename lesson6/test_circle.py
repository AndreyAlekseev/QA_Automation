from .Figure import Figure

PI = 3.14


class Circle(Figure):
    def __init__(self, name, radius):
        super().__init__(name, angles=0)
        self.radius = radius

    def area(self):
        s = PI*self.radius**2
        return s

    def perimeter(self):
        p = 2*PI*self.radius
        return p

    def add_area(self, obj):
        if not isinstance(obj, Circle):
            raise Exception("Argument must be instance of Circle class")
        else:
            return obj.perimeter() + self.perimeter()


""""test_circle"""

new_circle = Circle('test_circle', 10)


def test_create_circle():
    assert isinstance(new_circle, Circle)


def test_radius_of_circle():
    assert new_circle.radius == 10


def test_prop_of_circle():
    assert new_circle.name == 'test_circle' and new_circle.angles == 0


def test_area_of_circle():
    assert new_circle.area() == 314


def test_perimeter_of_circle():
    assert new_circle.perimeter() == 62.800000000000004


def test_add_area():
    circle_two = Circle('large_circle', 30)
    assert new_circle.add_area(circle_two) == 251.20000000000002
