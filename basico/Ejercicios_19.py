# Ejercicio 1

"""
    Definir una función inversa() que calcule la inversion de una cadena. 
    Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse".
"""

def inversa (cadena):
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida

print(inversa("Hola mundo"))

# Otra opción..

def inversa2(cadena):
    return cadena[::-1]

resultado = inversa2("Hola mundo2")
print(resultado)



# Ejercicio 2

"""
    Definir una funcion es_palindromo() que reconoce palindromo 
    palabras  que tiene el mismo aspecto escritas invertidas), ejemplo: es_palindromo("radar")
    tendría que devolver True.
"""

def palindromo(cadena):
    inicio = 0
    fin = len(cadena) - 1
    while cadena[inicio] == cadena[fin]:
        if inicio >= fin:
            return True
        inicio += 1
        fin -= 1
    return False

cadena = input("introduce una letra por favor: ")

print(palindromo(cadena))

# otra opción...
def es_palindromo(cadena):
    palabra_invertida = inversa(cadena)
    indice = 0
    cont = 0
    for i in range (len(cadena)):
        if palabra_invertida[indice] == cadena[indice]:
            indice += 1
            cont += 1
        else:
            print("No es palindromo")
            break
    if cont == len(cadena): #Si el contador = a la cantidad de letras de la cadena
        print("Es palindromo") # es porque recorrió todo el ciclo for y todas las
                                            # letras son iguales

es_palindromo("radar")

# Ejercicio 3

"""
    Definir una funcion superposicion() que tome dos listas y devuelva True si tiene al
    menos 1 elemento en común o devuelva False en caso contrario. Escribe la función usando el bucle for 
    aninado.
"""

def superposicion():
    pass