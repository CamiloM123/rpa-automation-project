import pyautogui
import time
import os
from colors import clasificar_color

def get_color(x, y):
    """
    Obtiene el color de la pantalla en las coordenadas dadas.

    Parameters:
    - x (int): Coordenada x.
    - y (int): Coordenada y.

    Returns:
    - tuple: Una tupla que representa el color en formato RGB.
    """
    return pyautogui.pixel(x, y)

def find_image(image_path):
    """
    Busca una imagen en la pantalla y devuelve su posición si es encontrada.

    Parameters:
    - image_path (str): La ruta de la imagen a buscar.

    Returns:
    - tuple or None: La posición de la esquina superior izquierda y la esquina inferior derecha de la imagen si es encontrada,
    o None si no se encuentra.
    """
    position = pyautogui.locateOnScreen(image_path)
    return position

def main():
    time.sleep(3)
    print(pyautogui.position())  # (x, y) coordinates of the mouse

    image_path = os.path.join(os.path.dirname(__file__), 'origin.png')
    position = find_image(image_path)

    if position is not None:
        # Imprime las coordenadas de la esquina superior izquierda y la esquina inferior derecha
        print(f"La imagen fue encontrada en la posición: {position}")
    else:
        print("La imagen no fue encontrada en la pantalla.")

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
            pyautogui.moveTo(pointer_x, pointer_y)  # mueve el mouse a las coordenadas (x, y)
            i += 1
            if i != 10:
                pointer_y += 20
            else:
                pointer_y += 15
        time.sleep(0.5)

if __name__ == "__main__":
    main()