"""""PigLatin: Agregale (letra inicial + ay) al final de todas las palabras en una cadena de texto y eliminales la letra inicial """

datos = "Hola mundo"

def pig(input):
    palabra = list(input).pop(0)
    # Palabra + inicial + ay
    input = "".join(input)+palabra+"ay"
    return input.lower()  

datos = datos.split(" ")
res = list(map(pig,datos))
print(" ".join(res))