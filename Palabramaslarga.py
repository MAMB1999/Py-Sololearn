"""Toma una cadena, calcula la longitud promedio de todas las palabras y devuelve la que tiene mas caracteres"""
def palabra_larga(var):
    var = var.split(" ")
    res = sorted(var,key=len)
    return res[len(var)-1]

print(palabra_larga("this is an awesome text"))
    
