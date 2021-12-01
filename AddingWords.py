"""Concatenar palabras con (-)"""
def concatenate(*words):
    lista = list(words)
    return "-".join(lista)

print(concatenate("I", "love", "Python", "!"))