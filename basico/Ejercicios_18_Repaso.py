# EJERCICIO 1

"""
    Definir una función max()
    que tome como argumento dos números y devuelva el mayor de ellos. 
    (Es cierto que python tiene una función max() incorporada,
    pero hacerla nosotros mismos es un muy buen ejercicio).
"""


def maximo(n1, n2):
    if n1 < n2:
        print(f"El valor máximo es {n2}")
        return n2
    elif n2 < n1:
        print(f"El valor máximo es {n1}")
        return n1
    else:
        return "son iguales"

print(maximo(8, 5))

# EJERCICIO 2


"""
    Definir una función max_de_tres(), 
    que tome tres números como argumentos y 
    devuelva el mayor de ellos.
"""


def max_de_tres():
    pass

print(max_de_tres())

# EJERCICIO 3

"""
    Definir una función que calcule la longitud de una lista 
    o una cadena dada. 
    (Es cierto que python tiene la función len() incorporada, 
    pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""

def longitud():
    pass

print("Enhorabuena acabaste los ejercicios")