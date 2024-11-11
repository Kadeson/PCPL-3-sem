from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side, color):
        super().__init__(side, side, color)

    def __repr__(self):
        return "Square(side={}, color={}, area={})".format(
            self.width, self.color.color, self.area()
        )