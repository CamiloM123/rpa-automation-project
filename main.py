"""
Author: Juan Camilo Muñoz Valencia

This module contains the main function to execute the automation script.
"""

import pyautogui
import time
import os
from functions import get_color, find_image, color_process, move_to_center, color_params, delete_and_write

def black_priority():
    pointer_x, pointer_y = move_to_center('images/priority.png')
    pointer_x += 100
    pyautogui.moveTo(pointer_x, pointer_y)
    # time.sleep(0.5)
    # delete_and_write('99')
    
def change_velocity():
    time.sleep(0.5)
    pointer_x, pointer_y = move_to_center("images/velocity-change.png")
    pointer_x += 100
    pyautogui.moveTo(pointer_x, pointer_y)
    # time.sleep(0.5)
    # delete_and_write('99');
        
def change_power():
    time.sleep(0.5)
    pointer_x, pointer_y = move_to_center("images/min-power-change.png")
    pointer_y += 30
    pyautogui.moveTo(pointer_x, pointer_y)
    # delete_and_write('99')
    time.sleep(0.5)
    pointer_x2, pointer_y2 = move_to_center("images/max-power-change.png")
    pointer_y2 += 30
    pyautogui.moveTo(pointer_x2, pointer_y2)
    # delete_and_write('99')

def change_interval():
    time.sleep(0.5)
    pointer_x, pointer_y = move_to_center("images/interval-change.png")
    pointer_x += 100
    pyautogui.moveTo(pointer_x, pointer_y)
    # time.sleep(0.5)
    # delete_and_write('99')

def params_change_process(color_name):
    time.sleep(0.5)
    if color_name == "green" or color_name == "purple" or color_name == "red":
        change_velocity()
        change_power()
        change_interval()
    elif color_name == "black" or color_name == "blue" or color_name == "magenta":
        change_velocity()
        change_power()

def black_priority_process():
    time.sleep(3)
    pointer_x, pointer_y = move_to_center("images/origin-1.png")
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
    # time.sleep(3)
    pointer_x, pointer_y = move_to_center('images/origin-2.png')
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
            # time.sleep(0.5)
            params_change_process(color_name)
            time.sleep(0.5)
            if color_name == "green" or color_name == "purple" or color_name == "red":
                x,y = move_to_center('images/check-1.png')
                x -= 60
                pyautogui.moveTo(x, y)
                
            if color_name != "green":
                pointer_y += 15
            else:
                pointer_y += 20  
            i += 1
        time.sleep(1)

def procces_3():
    pointer_x, pointer_y = move_to_center('images/btn-ok.png')
    pyautogui.click(pointer_x, pointer_y)
    time.sleep(3)
    pointer_x, pointer_y = move_to_center('images/btn-download.png')
    pyautogui.click(pointer_x, pointer_y)
            
def main():
    """
    Main function to execute the automation script.
    """
    time.sleep(3)
    # black_priority_process()
    procces_2()
    # procces_3()

if __name__ == "__main__":
    main()

