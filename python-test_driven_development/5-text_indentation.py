#!/usr/bin/python3
""" Module that print a text with 2 new lines"""


def text_indentation(text):
    """function that that print a text with 2 new lines
    Args:
    text to print
    Return:
    New text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    specialchar = ('.', '?', ':')
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in specialchar:
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
    print("\n".join([line.strip() for line in result.split("\n")]))
