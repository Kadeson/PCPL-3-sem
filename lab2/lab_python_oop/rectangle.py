from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.figure_color import FigureColor

class Rectangle(GeometricFigure):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigureColor(color)

    def area(self):
        return self.width * self.height/2

    def __repr__(self):
        return "Rectangle(width={}, height={}, color={}, area={})".format(
            self.width, self.height, self.color.color, self.area()
        )