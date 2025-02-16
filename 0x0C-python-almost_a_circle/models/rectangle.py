#!/usr/bin/python3
"""
This module contains the Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
    Define Rectangle class.

    Private instance attributes, each with its own public getter and setter:
    - __width -> width
    - __height -> height
    - __x -> x
    - __y -> y

    Class constructor:
    def __init__(self, width, height, x=0, y=0, id=None):
        Call the super class with id - this super call with use the
        logic of the __init__ of the Base class
        Assign each argument width, height, x, and y to the right attribute
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the rectangle.
        """
        super().__init__(id)  # Call the _init_ method of Base class with id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Defines getter for the y of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the rectanle
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the rectangle using the '#' character,
        taking x and y coordinates into account
        """
        # Print y offset
        for i in range(self.y):
            print()

        # Print each row with x offset
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
         Updates the Rectangle attributes.
        Args:
            *args: Variable length argument list.
                1st argument represents id
                2nd argument represents width
                3rd argument represents height
                4th argument represents x
                5th argument represents y
            **kwargs: Double pointer to a dictionary: key/value pairs
                Each key represents an attribute to the Rectangle
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
