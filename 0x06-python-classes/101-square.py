#!/usr/bin/python3
"""this file contains our square class """


class Square:
    """A class to represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes a square instance.

        Args:
            size: the size of the square.
            position: position of the square in stdout
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Retrieves attribute size.
        Returns:
            size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """validates the value of size
        Args:
            value: the size of the square.

        Raises:
            TypeError: if size if not an integer.
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrieves the position

        Return:
            positon of square
        """
        return self._position

    @position.setter
    def position(self, value):
        """validates the value of position
        Args:
            value: tuple of 2 positive integers

        Raises:
            TypeError: if not tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculates the area of a square.

        Returns:
            area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """prints to stdout the square with #

        """
        the_size = self.__size
        pos = self.__position
        if the_size == 0:
            print()
        else:
            for j in range(pos[1]):
                print()
            for i in range(the_size):
                for k in range(pos[0]):
                    print(" ", end="")
                for i in range(the_size):
                    print("#", end="")
                print()

    def __str__(self):
        """returns a string with same output as my_print function.
        """
        string = ""
        the_size = self.__size
        pos = self.__position
        if the_size != 0:
            for i in range(pos[1]):
                string += "\n"
            for i in range(the_size):
                string += " " * pos[0] + "#" * the_size
                if i < the_size - 1:
                    string += "\n"
        return string
