from .Figure import Figure


class Square(Figure):
    def __init__(self, name, side):
        super().__init__(name, 4)
        self.side = side

    def area(self):
        res = self.side**2
        return res

    def perimeter(self):
        res = self.side*4
        return res

    def add_area(self, obj):
        if not isinstance(obj, Square):
            raise Exception("Argument must be instance of Square class")
        else:
            return obj.perimeter()+self.perimeter()


""""test_square"""
new_square = Square('created_triangle', 10)


def test_create_square():
    assert isinstance(new_square, Square)


def test_property_of_square():
    assert new_square.name == 'created_triangle' and new_square.side == 10 and new_square.angles == 4


def test_area_of_square():
    assert new_square.area() == 100


def test_perimeter():
    assert new_square.perimeter() == 40


def test_add_area():
    square_two = Square('square_two', 50)
    assert new_square.add_area(square_two) == 240
