"""
Module: colors.py
Author: Juan Camilo Muñoz Valencia

This module contains a function to classify a color into one of the predefined categories.
"""


def classify_color(color: tuple) -> str:
    """
    Classify a given color into one of the predefined categories.

    Parameters:
    - color (tuple): A tuple representing the color in RGB format.

    Returns:
    - str: The category to which the color belongs ('purple', 'green', 'red', 'blue', 'magenta', 'black', or 'Unclassified').
    """

    R, G, B = color

    # Define a dictionary with color tones
    color_dictionary = {
        'purple': {(127, 0, 255), (127, 102, 204), (191, 127, 255), (76, 0, 153), (153, 0, 153)},
        'green': {(0, 255, 0), (51, 204, 0), (38, 153, 0), (0, 127, 0), (38, 76, 38)},
        'red': {(255, 0, 0), (204, 0, 0), (153, 0, 0), (204, 51, 0), (255, 127, 127)},
        'blue': {(0, 0, 255)},
        'magenta': {(255, 0, 255)},
        'black': {(0, 0, 0)}
    }

    # Search for the color in the dictionary
    for category, colors in color_dictionary.items():
        if color in colors:
            return category

    # If not found in any category
    return "Unclassified"
