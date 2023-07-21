#!/usr/bin/python3
""" Provides text indentation function"""


def text_indentation(text):
    """
    Print the text with 2 new lines after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If the input 'text' is not a string.

    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define the punctuation characters that indicate new lines
    punctuations = {'.', '?', ':'}

    # Initialize variables to store each line and the final output
    line = ""
    output = ""

    for char in text:
        line += char
        if char in punctuations:
            # Remove leading/trailing spaces and add the line to the output
            output += line.strip() + "\n\n"
            line = ""

    # Add the last line to the output if there is one
    if line:
        output += line.strip()

    print(output)
