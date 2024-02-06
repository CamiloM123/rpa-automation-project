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
        
def black_priority():
    image_path = os.path.join(os.path.dirname(__file__), 'images/priority.png')
    priority_position = find_image(image_path)

    if priority_position is not None:
        pointer_x, pointer_y = pyautogui.center(priority_position)
        pointer_x += 100
        pyautogui.moveTo(pointer_x, pointer_y)
        time.sleep(0.5)
        # pyautogui.click()
        # pyautogui.press('backspace', presses=3)
        # pyautogui.write('99');  
        
def color_params(color_name):
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
            
def black_priority_process():
    time.sleep(3)
    image_path = os.path.join(os.path.dirname(__file__), 'images/origin-1.png')
    origin_position = find_image(image_path)

    if origin_position is not None:
        pointer_x, pointer_y = pyautogui.center(origin_position)
        pointer_y += 8
        pyautogui.moveTo(pointer_x, pointer_y)
        while True: 
            color = get_color(pointer_x, pointer_y)
            if color == (0, 0, 0):
                print("Black color found.")
                black_priority()
                pyautogui.moveTo(pointer_x, pointer_y)
                # pyautogui.doubleClick(pointer_x, pointer_y)
                break
            else:
                pointer_y += 15
                pyautogui.moveTo(pointer_x, pointer_y)
                time.sleep(1)

def param_library_process(color_name):
    """
    Process the parameters library.
    """
    image_path = os.path.join(os.path.dirname(__file__), 'images/param-library.png')
    library_position = find_image(image_path)

    if library_position is not None:
        pointer_x, pointer_y = pyautogui.center(library_position)
        pyautogui.moveTo(pointer_x, pointer_y)
        color_params(color_name)
        # pyautogui.click()
        
            
def procces_2():
    time.sleep(3)
    print(pyautogui.position())  # (x, y) coordinates of the mouse

    image_path = os.path.join(os.path.dirname(__file__), 'images/origin-2.png')
    origin_position = find_image(image_path)

    if origin_position is not None:
        pointer_x, pointer_y = pyautogui.center(origin_position)
        pointer_y += 23
        # pointer_y += 35
        i = 1
        while True:
            color = get_color(pointer_x, pointer_y)
            if color == (255, 255, 255):
                print("White color found.")
                break
            else:
                color_name = color_process(color, pointer_x, pointer_y, i)
                time.sleep(0.5)
                # param_library_process(color_name)
                time.sleep(0.5)
                if color_name == "green" or color_name == "blue" or color_name == "magenta":
                    check_process()
                if color_name != "green":
                    pointer_y += 15
                else:
                    pointer_y += 20  
                i += 1
            time.sleep(1)
            
            
def main():
    """
    Main function to execute the automation script.
    """
    time.sleep(3)
    # black_priority_process()
    procces_2()
    # color_params_process("green")
    # color_params_process("blue")
    # color_params_process("magenta")
    # color_params_process("purple")
    # color_params_process("red")

if __name__ == "__main__":
    main()

