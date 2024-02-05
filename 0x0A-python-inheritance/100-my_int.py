#!/usr/bin/python3
"""class MyInt that inherits from int
"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __eq__(self, value):
        "returns not equal"
        return super().__ne__(value)

    def __ne__(self, value):
        "returns equal"
        return super().__eq__(value)
