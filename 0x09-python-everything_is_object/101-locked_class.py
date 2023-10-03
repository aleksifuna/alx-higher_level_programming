#!/usr/bin/python3
"""this module contain one class ie LockedClass
"""


class LockedClass:
    """has no class or object attribute and prevents the user
    from dynamically creating new instances attributes except if 'first_name'
    """

    def __setattr__(self, name, value):
        """locks the class to only accept new attribute first name

        Raises:
            AttributeError: if the attribute is not first name
            """
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            msg = f"'LockedClass' object has no attribute '{name}'"
            raise AttributeError(msg)
