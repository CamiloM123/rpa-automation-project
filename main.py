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
    return pyautogui.pixel(x, y)

def find_image(image_path):
    """
    Search for an image on the screen and return its position if found.

    Parameters:
    - image_path (str): The path of the image to search for.

    Returns:
    - tuple or None: The position of the top-left and bottom-right corners of the image if found,
    or None if not found.
    """
    position = pyautogui.locateOnScreen(image_path)
    return position

def main():
    time.sleep(3)
    print(pyautogui.position())  # (x, y) coordinates of the mouse

    image_path = os.path.join(os.path.dirname(__file__), 'images/origin.png')
    position = find_image(image_path)

    if position is not None:
        # Print the coordinates of the top-left and bottom-right corners
        print(f"The image was found at the position: {position}")
    else:
        print("The image was not found on the screen.")

    pointer_x, pointer_y = pyautogui.center(position)
    pointer_y += 40
    i = 1

    while True:
        color = get_color(pointer_x, pointer_y)
        if color == (255, 255, 255):
            print("White color found.")
            break
        else:
            color_name = classify_color(color)
            print(f"Color {i}: {color} -> {color_name}")
            pyautogui.moveTo(pointer_x, pointer_y)  # move the mouse to (x, y) coordinates
            i += 1
            if i != 10:
                pointer_y += 20
            else:
                pointer_y += 15
        time.sleep(0.5)

if __name__ == "__main__":
    main()
