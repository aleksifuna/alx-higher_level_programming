#!/usr/bin/python3
""" This module supplies a class Rectangle"""
from .base import Base


class Rectangle(Base):
    """ Inherits from Base with some private instance """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes an instance of class Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """
        retrieves the private instance attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Validates and sets the attribute height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        retrieves the private instance attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        validates and sets the attribute height
        """
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def x(self):
        """
        retrieves the private instance attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        validates and sets the attribute height
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
         retrieves the private instance attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        validates and sets the attribute height
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calculates and returns the area value of rectangle instance

        Return: (int) area of rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        prints to stdout the instance with characer '#'
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
                if j == self.__width - 1:
                    print()

    def __str__(self):
        """
        Returns a str representation of rectangle instance
        """
        a = self.id
        b = self.__x
        c = self.__y
        d = self.__width
        e = self.__height

        return "[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, d, e)

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "width":
                        self.__width = value
                    elif key == "height":
                        self.__height = value
                    elif key == "x":
                        self.__x = value
                    elif key == "y":
                        self.__y = value
