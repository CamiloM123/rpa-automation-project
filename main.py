import pyautogui
import time
from colors import clasificar_color

""" Mouse functions """

time.sleep(3)
# *** Information about the mouse ***
print(pyautogui.position())  # (x, y) coordinates of the mouse
# print(pyautogui.size()) # (width, height) of the screen
# print(pyautogui.onScreen(-1, 0)) # True if (x, y) is within the screen.

# *** Move the mouse ***
# pyautogui.moveTo(1000, 100, duration=3)  # move mouse to (x, y) coordinates
# pyautogui.moveRel(100, 200, duration=3)  # move mouse relative to its current position

# *** Click the mouse ***
# pyautogui.click(1000, 300, 4, 1, button="left")  # click the mouse at (x, y) coordinates
# pyautogui.doubleClick(1000, 300)

# *** Drag the mouse ***
# pyautogui.dragTo(1000, 500, duration=3)  # drag mouse to XY
# pyautogui.dragRel(100, 100, duration=3)  # drag mouse relative to its current position

# # *** Scroll the mouse ***
# pyautogui.scroll(100)  # scroll up 100 "clicks"
# pyautogui.scroll(-100)  # scroll down 100 "clicks"

""" Spiral drawing using pyautogui """

# time.sleep(1)
# distance = 300
# while distance > 0:
#     pyautogui.dragRel(distance, 0, 0.2, button="left")  # move right
#     distance = distance - 20
#     pyautogui.dragRel(0, distance, 0.2, button="left")  # move down
#     pyautogui.dragRel(-distance, 0, 0.2, button="left")  # move left
#     distance = distance - 20
#     pyautogui.dragRel(0, -distance, 0.2, button="left")  # move up

# time.sleep(2)

""" Keyboard functions """

# *** Information about the keyboard ***
# print(pyautogui.KEYBOARD_KEYS)  # list of all keyboard keys
# print(pyautogui.KEYBOARD_KEYS[0])  # first keyboard key

# *** Press and write***
# pyautogui.press("enter")  # press and release the enter key
# pyautogui.write("Hello world!", interval=0.2)  # write "Hello world!" with a quarter second delay after each character
# pyautogui.screenshot("screenshot.png")  # take a screenshot


""" Image """

import os

image = os.path.join(os.path.dirname(__file__), 'origin.png')

position = pyautogui.locateOnScreen(image)

if position is not None:
    # Imprime las coordenadas de la esquina superior izquierda y la esquina inferior derecha
    print(f"La imagen fue encontrada en la posición: {position}")
else:
    print("La imagen no fue encontrada en la pantalla.")

""" Colors """

def get_color(x, y):
    return pyautogui.pixel(x, y)

pointer_x, pointer_y = pyautogui.center(position)
pointer_y += 40
i = 1

while True:
    color = get_color(pointer_x, pointer_y)
    if color == (255, 255, 255):
        print("Color blanco encontrado.")
        break
    else:
        color_name = clasificar_color(color)
        print(f"color {i}: {color} -> {color_name}")
        pyautogui.moveTo(pointer_x, pointer_y)  # move mouse to (x, y) coordinates
        i += 1
        if i != 10:
            pointer_y += 20
        else:
            pointer_y += 15
    time.sleep(0.5)

#Error 10-11