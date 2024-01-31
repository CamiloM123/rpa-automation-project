def clasificar_color(color):
    R, G, B = color

    # # Tonos de Morado
    morado_1 = (127, 0, 255)
    morado_2 = (127, 102, 204)
    morado_3 = (191, 127, 255)
    morado_4 = (76, 0, 153)
    morado_5 = (153, 0, 153) 

    # Tonos de Verde
    verde_1 = (0, 255, 0)
    verde_2 = (51, 204, 0)
    verde_3 = (38, 153, 0)
    verde_4 = (0, 127, 0)
    verde_5 = (38, 76, 38)

    # Tonos de Rojo
    rojo_1 = (255, 0, 0)
    rojo_2 = (204, 0, 0)
    rojo_3 = (153, 0, 0)
    rojo_4 = (204, 51, 0)
    rojo_5 = (255, 127, 127)

    # Color Azul
    azul = (0, 0, 255)

    # Color Magenta
    magenta = (255, 0, 255)

    # Color Negro
    negro = (0, 0, 0)
    # Funciones de comparación
    
    diccionario = {
        'morado' : {morado_1, morado_2, morado_3, morado_4, morado_5},
        'verde' : {verde_1, verde_2, verde_3, verde_4, verde_5},
        'rojo' : {rojo_1, rojo_2, rojo_3, rojo_4, rojo_5},
        'azul' : {azul},
        'magenta' : {magenta},
        'negro' : {negro}
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
