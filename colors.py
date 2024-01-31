def clasificar_color(color: any) -> str:
    """
    Clasifica un color dado en una de las categorías predefinidas.

    Parameters:
    - color (tuple): Una tupla que representa el color en formato RGB.

    Returns:
    - str: La categoría a la que pertenece el color ('morado', 'verde', 'rojo', 'azul', 'magenta', 'negro' o 'No clasificado').

    Example:
    >>> color_ejemplo = (127, 0, 255)
    >>> categoria = clasificar_color(color_ejemplo)
    >>> print(f"El color se clasifica como: {categoria}")
    El color se clasifica como: morado
    """
    R, G, B = color

    # Definir un diccionario con los tonos de colores
    diccionario = {
        'morado': {(127, 0, 255), (127, 102, 204), (191, 127, 255), (76, 0, 153), (153, 0, 153)},
        'verde': {(0, 255, 0), (51, 204, 0), (38, 153, 0), (0, 127, 0), (38, 76, 38)},
        'rojo': {(255, 0, 0), (204, 0, 0), (153, 0, 0), (204, 51, 0), (255, 127, 127)},
        'azul': {(0, 0, 255)},
        'magenta': {(255, 0, 255)},
        'negro': {(0, 0, 0)}
    }

    # Buscar el color en el diccionario
    for categoria, colores in diccionario.items():
        if color in colores:
            return categoria

    # Si no se encuentra en ninguna categoría
    return "No clasificado"

# Ejemplo de uso
color_ejemplo = (127, 0, 255)
categoria = clasificar_color(color_ejemplo)
print(f"El color se clasifica como: {categoria}")

