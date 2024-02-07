"""
Module: functions.py
Author: Juan Camilo Muñoz Valencia

This module contains the functions for the RPA (Robotic Process Automation) project.
"""

import pyautogui
import os
import time
from colors import classify_color


def get_color(x: int, y: int) -> tuple:
    """
    Get the color of the screen at the given coordinates.

    This function retrieves the color of the screen at the specified coordinates (x, y).
    It returns a tuple representing the color in RGB format.

    Parameters:
    - x (int): X-coordinate.
    - y (int): Y-coordinate.

    Returns:
    - tuple: A tuple representing the color in RGB format.
    """
    x, y = int(x), int(y)
    return pyautogui.pixel(x, y)


def find_image(image_path: str) -> tuple or None:
    """
    Find the specified image on the screen.

    This function searches for the specified image on the screen using its file path.
    If the image is found, it returns the position (x, y, width, height) of the image.
    If the image is not found, it returns None.

    Parameters:
    - image_path (str): Path to the image file.

    Returns:
    - tuple: Position of the found image (x, y, width, height) or None if not found.
    """
    try:
        position = pyautogui.locateOnScreen(image_path)
        # print(f"Image found at {position}")
        return position
    except pyautogui.ImageNotFoundException:
        print("The image was not found on the screen.")
        return None


def color_process(color: tuple, pointer_x: int, pointer_y: int, i: int) -> str:
    """
    Process the color at the given coordinates.

    This function processes the color represented by the RGB tuple at the specified coordinates.
    It assigns a name to the color using the `classify_color` function.
    Additionally, it moves the mouse pointer to the given coordinates.

    Parameters:
    - color (tuple): RGB color tuple.
    - pointer_x (int): X-coordinate of the pointer.
    - pointer_y (int): Y-coordinate of the pointer.
    - i (int): Index for color processing.

    Returns:
    - str: Name of the color.
    """
    color_name = classify_color(color)
    print(f"Color {i}: {color} -> {color_name}")
    # move the mouse to (x, y) coordinates
    pyautogui.moveTo(pointer_x, pointer_y)
    return color_name


def move_to_center(image_path: str) -> tuple or None:
    """
    Move the mouse to the center of the specified image.

    This function locates the specified image on the screen and moves the mouse pointer to its center.
    If the image is found, it returns the coordinates (x, y) of the center of the image.
    If the image is not found, it returns None.

    Parameters:
    - image_path (str): Path to the image file.

    Returns:
    - tuple: Coordinates (x, y) of the center of the image, or None if the image is not found.
    """
    position = find_image(image_path)
    if position is not None:
        pointer_x, pointer_y = pyautogui.center(position)
        pyautogui.moveTo(pointer_x, pointer_y)
        return pointer_x, pointer_y


def color_params(color_name: str):
    """
    Process color parameters.

    This function searches for the specified color in a predefined dictionary of color names and corresponding image paths.
    If the color is found, it moves the mouse pointer to the center of the image representing the color parameters.
    Optionally, it waits for a specified time before and after moving the mouse.

    Parameters:
    - color_name (str): Name of the color to process.

    Notes:
    - The function assumes the existence of image files corresponding to each color parameter.
    - Adjust the sleep time as needed for proper synchronization with screen changes.
    """
    dict_color = {
        "green": 'images/param-green.png',
        "blue": 'images/param-blue.png',
        "magenta": 'images/param-magenta.png',
        "red": 'images/param-red.png',
        "purple": 'images/param-purple.png'
    }

    for key, value in dict_color.items():
        if key == color_name:
            image_params_path = value
            image_path = os.path.join(
                os.path.dirname(__file__), image_params_path)
            position = find_image(image_path)
            if position is not None:
                pointer_x, pointer_y = pyautogui.center(position)
                pyautogui.moveTo(pointer_x, pointer_y)
                # pyautogui.click() # Uncomment to click on the image
                time.sleep(3)  # Adjust sleep time as needed
                image_path = os.path.join(os.path.dirname(
                    __file__), "images/param-load.png")
                load_position = find_image(image_path)
                if load_position is not None:
                    pointer_x, pointer_y = pyautogui.center(load_position)
                    pyautogui.moveTo(pointer_x, pointer_y)
                    # pyautogui.click() # Uncomment to click on the image
                break


def delete_and_write(value: str) -> None:
    """
    Delete the content of the input field and write a new value.

    Parameters:
    - value (str): The new value to be written into the input field.
    """
    pyautogui.click()  # Click to focus on the input field
    pyautogui.press('backspace', presses=3)  # Delete existing content
    pyautogui.write(f'{value}')  # Write the new value into the input field
