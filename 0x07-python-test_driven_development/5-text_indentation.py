#!/usr/bin/python3
"""function that prints a text with 2 new lines after
    each of these characters: ., ? and :"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each
    occurrence of '.', '?', and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_chars = ['.', '?', ':']
    output = ""
    current_line = ""
    for char in text:
        current_line += char
        if char in punctuation_chars:
            output += current_line.strip() + '\n\n'
            current_line = ""
    output += current_line.strip()
    print(output)
