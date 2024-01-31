#!/usr/bin/python3
"""The module contains a function prints a text with \
2 new lines after each of these characters: ., ? and :
raises TypeError if the text is not a string
"""
encountered_letter = False


def text_indentation(text):
    """The text_indentation prints a text with 2 new lines after each\
of these characters: ., ? and :
    Arg: text(string) The text to indent
    Return: The indented string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    global encountered_letter
    for letter in text:
        if encountered_letter:
            encountered_letter = False
            continue
        if letter == '.' or letter == '?' or letter == ":":
            print(letter)
            print()
            encountered_letter = True
        else:
            print(letter, end="")
