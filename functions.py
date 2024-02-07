"""
Module: functions.py
Author: Juan Camilo Muñoz Valencia

This module contains the functions for the RPA project.
"""

import pyautogui
import os
import time
from colors import classify_color

def get_color(x: int, y: int) -> tuple:
    """
    Get the color of the screen at the given coordinates.

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

    Parameters:
    - image_path (str): Path to the image file.

    Returns:
    - tuple: Position of the found image or None if not found.
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
    pyautogui.moveTo(pointer_x, pointer_y)  # move the mouse to (x, y) coordinates
    return color_name

def move_to_center(image_path: str) -> tuple or None:
    """
    Move the mouse to the center of the specified image and click.

    Parameters:
    - image_path (str): Path to the image file.

    Returns:
    - tuple: Coordinates (x, y) of the center of the image.
    """
    position = find_image(image_path)
    if position is not None:
        pointer_x, pointer_y = pyautogui.center(position)
        pyautogui.moveTo(pointer_x, pointer_y)
        return pointer_x, pointer_y

def color_params(color_name: str) :
    """
    Process color parameters.

    Parameters:
    - color_name (str): Name of the color.
    """
    # time.sleep(3)
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
            image_path = os.path.join(os.path.dirname(__file__), image_params_path)
            position = find_image(image_path)
            if position is not None:
                pointer_x, pointer_y = pyautogui.center(position)
                pyautogui.moveTo(pointer_x, pointer_y)
                # pyautogui.click()
                time.sleep(3)
                image_path = os.path.join(os.path.dirname(__file__), "images/param-load.png")
                load_position = find_image(image_path)
                if load_position is not None:
                    pointer_x, pointer_y = pyautogui.center(load_position)
                    pyautogui.moveTo(pointer_x, pointer_y)
                    # pyautogui.click()
                break
    
def delete_and_write(value):
    """
    Delete the content of the input field and write a new value.
    """
    pyautogui.click()
    pyautogui.press('backspace' , presses=3)
    pyautogui.write('{value}')