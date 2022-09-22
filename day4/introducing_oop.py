import sys
import os


class Rectangle:
    units = 'cm'  # all rectangles will have the same units

    def __init__(self, width, height, position=(0, 0), fill='white', stroke='black'):
        self.width = float(width)
        self.height = float(height)
        self.position = position
        self.fill = fill
        self.stroke = stroke


class Text:

    def __int__(self, size=8, position=(0, 0), txt_colour="blue"):
        self.size = size
        self.position = position
        self.txt_colour = txt_colour



    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.width + self.height)

    def diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 1/2

    def bounding_box(self):
        return (self.position[0] - self.width / 2, self.width[0] - self.width / 2,
                self.position[1] - self.width / 2, self.width[1] - self.width / 2)


class Canvas:
    units = "cm"

    def __init__(self, width, height, bg_colour="blue"):
        self.width = float(width)
        self.height = float(height)
        self.bg_colour = bg_colour

def main():
    rectangle = Rectangle(10, 15)
    print(rectangle.area())
    print(rectangle.perimeter())
    print(rectangle.diagonal())
    print(rectangle.bounding_box())

    return os.EX_OK


if __name__ == '__main__':
    sys.exit(main())
