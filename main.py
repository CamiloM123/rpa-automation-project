"""Laser Machine Automation Script"""

import pyautogui
import time
import os
from colors import classify_color

def get_color(x, y):
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

def find_image(image_path):
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

def color_process(color, pointer_x, pointer_y, i):
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

def check_process():
    """
    Check the specified image on the screen and move the mouse to its center.
    """
    image_path = os.path.join(os.path.dirname(__file__), 'images/check-1.png')
    check_position = find_image(image_path)

    if check_position is not None:
        pointer_x, pointer_y = pyautogui.center(check_position)
        pyautogui.moveTo(pointer_x, pointer_y)

def main():
    """
    Main function to execute the automation script.
    """
    time.sleep(3)
    print(pyautogui.position())  # (x, y) coordinates of the mouse

    image_path = os.path.join(os.path.dirname(__file__), 'images/origin-2.png')
    origin_position = find_image(image_path)

    if origin_position is not None:
        pointer_x, pointer_y = pyautogui.center(origin_position)
        # pointer_y += 25
        pointer_y += 35
        i = 1
        while True:
            color = get_color(pointer_x, pointer_y)
            if color == (255, 255, 255):
                print("White color found.")
                break
            else:
                color_name = color_process(color, pointer_x, pointer_y, i)
                time.sleep(1)
                check_process()
                if color_name != "green":
                    pointer_y += 17
                else:
                    pointer_y += 22
                i += 1
            time.sleep(1)

if __name__ == "__main__":
    main()

