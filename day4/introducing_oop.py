import sys
import turtle


class Rectangle:
    units = 'cm'  # all rectangles will have the same units

    def __init__(self, width, height, position=(0, 0), fill='white', stroke='black'):
        self.width = float(width)
        self.height = float(height)
        self.position = position
        self.fill = fill
        self.stroke = stroke

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def bounding_box(self):
        return (self.position[0] - self.width / 2, self.position[0] - self.width / 2,
                self.position[1] - self.height / 2, self.position[1] - self.height / 2)


class Canvas(turtle.TurtleScreen):
    units = "cm"

    def __init__(self, width, height, bg_colour="grey", canvas=turtle.getcanvas()):
        super().__init__(canvas)
        self.pen = turtle.RawTurtle(canvas)
        self.width = float(width)
        self.height = float(height)
        self.bg_colour = bg_colour

    def mystery_method(self):
        self.pen.up()
        self.pen.goto(0, self.height / 2)
        self.pen.down()
        self.pen.goto(0, -self.height / 2)
        self.pen.up()
        self.pen.goto(-self.width / 2, 0)
        self.pen.down()
        self.pen.goto(self.width / 2, 0)
        self.pen.up()
        self.pen.home()


class Square(Rectangle):
    def __init__(self, width, *args, **kwargs):
        super().__init__(width, width, *args, **kwargs)


class Text:

    def __init__(self, size=8, position=(0, 0), txt_colour="blue"):
        self.size = size
        self.position = position
        self.txt_colour = txt_colour


def main():
    rectangle = Rectangle(10, 15)
    print(rectangle.area())
    print(rectangle.bounding_box())
    print(rectangle.diagonal())
    print(rectangle.perimeter())

    square1 = Square(10)
    print(square1.area())
    print(square1.bounding_box())
    print(square1.diagonal())
    print(square1.perimeter())

    print(square1)
    print(square1.fill)

    canvas2 = Canvas(1200, 750)
    print(canvas2)
    print(canvas2.height)
    print(canvas2.mystery_method())
    turtle.done()

    return 0


if __name__ == '__main__':
    sys.exit(main())
