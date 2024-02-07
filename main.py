"""
Author: Juan Camilo Muñoz Valencia

This module contains the main function to execute the automation script.
"""

import pyautogui
import time
from functions import get_color, color_process, move_to_center, color_params, delete_and_write


def black_priority():
    """
    Move the mouse to the center of the black priority image and adjust position.
    """
    pointer_x, pointer_y = move_to_center('images/priority.png')
    pointer_x += 100
    pyautogui.moveTo(pointer_x, pointer_y)


def change_velocity():
    """
    Change the velocity parameter.
    """
    time.sleep(0.5)
    pointer_x, pointer_y = move_to_center("images/velocity-change.png")
    pointer_x += 100
    pyautogui.moveTo(pointer_x, pointer_y)


def change_power():
    """
    Change the power parameter.
    """
    time.sleep(0.5)
    pointer_x, pointer_y = move_to_center("images/min-power-change.png")
    pointer_y += 30
    pyautogui.moveTo(pointer_x, pointer_y)

    time.sleep(0.5)
    pointer_x2, pointer_y2 = move_to_center("images/max-power-change.png")
    pointer_y2 += 30
    pyautogui.moveTo(pointer_x2, pointer_y2)


def change_interval():
    """
    Change the interval parameter.
    """
    time.sleep(0.5)
    pointer_x, pointer_y = move_to_center("images/interval-change.png")
    pointer_x += 100
    pyautogui.moveTo(pointer_x, pointer_y)


def params_change_process(color_name):
    """
    Process parameter changes based on color.
    """
    time.sleep(0.5)
    if color_name in ["green", "purple", "red"]:
        change_velocity()
        change_power()
        change_interval()
    elif color_name in ["black", "blue", "magenta"]:
        change_velocity()
        change_power()


def black_priority_process():
    """
    Process black priority.
    """
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
            break
        else:
            pointer_y += 15
            pyautogui.moveTo(pointer_x, pointer_y)
            time.sleep(1)


def param_library_process(color_name):
    """
    Process the parameters library.
    """
    pointer_x, pointer_y = move_to_center('images/param-library.png')
    pyautogui.moveTo(pointer_x, pointer_y)
    color_params(color_name)
    # pyautogui.click()


def procces_2():
    """
    Process the second stage.
    """
    # time.sleep(3)
    pointer_x, pointer_y = move_to_center('images/origin-2.png')
    pointer_y += 23
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
            if color_name in ["green", "purple", "red"]:
                x, y = move_to_center('images/check-1.png')
                x -= 60
                pyautogui.moveTo(x, y)

            if color_name != "green":
                pointer_y += 15
            else:
                pointer_y += 20
            i += 1
        time.sleep(1)


def procces_3():
    """
    Process the third stage.
    """
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
