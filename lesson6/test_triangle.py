from .Figure import Figure


class Triangle(Figure):
    def __init__(self, name, side_a, side_b, side_c):
        super().__init__(name, 3)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        s_area = (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5
        return s_area

    def perimeter(self):
        res = self.side_a + self.side_b + self.side_c
        return res

    def add_area(self, obj):
        if not isinstance(obj, Triangle):
            raise Exception("Argument must be instance of Triangle class")
        else:
            return obj.perimeter()+self.perimeter()


""""test_triangle"""

new_triangle = Triangle('created_triangle', 10, 10, 10)


def test_create_triangle():
    assert isinstance(new_triangle, Triangle)


def test_sides_of_triangle():
    assert new_triangle.side_a == 10 and new_triangle.side_b == 10 and new_triangle.side_c == 10


def test_prop_of_triangle():
    assert new_triangle.name == 'created_triangle' and new_triangle.angles == 3


def test_area_of_triangle():
    assert new_triangle.area() == 43.30127018922193


def test_perimeter_of_triangle():
    assert new_triangle.perimeter() == 30


def test_add_area():
    triangle_two = Triangle('large_triangle', 20, 20, 20)
    assert new_triangle.add_area(triangle_two) == 90
