import sys
import os


class Rectangle:
    units = 'cm'  # all rectangles will have the same units

    def __init__(self, width, height, position=(0, 0)):
        self.width = float(width)
        self.height = float(height)
        self.position = position


    def __str__(self):  # Python special methods
        return f"I am a circle of size {self.area()}{self.units} located at {self.position}."


    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.width + self.height)

    def diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 1/2

    def bounding_box(self):
        coords =(self.position[0] - self.width / 2, self.width[0] - self.width / 2,
                 self.position[1] - self.width / 2, self.width[1] - self.width / 2)
        return coords


def main():
    rectangle = Rectangle(10, 15)
    print(rectangle.area())
    print(rectangle.perimeter())
    print(rectangle.diagonal())
    print(rectangle.coords())

    return os.EX_OK


if __name__ == '__main__':
    sys.exit(main())
