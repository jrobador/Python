""" def mult_numbers (num, mult):
    return num * mult

lista_de_numeros = [1,3,9,12]
multiplier = 3


resultado = list(map(mult_numbers, lista_de_numeros,[multiplier]))


print (resultado)
 """

def suma_elementos(numero_1,numero_2, lista):
    """
    Función que suma cada elemento de la lista con el número fijo dado
    """
    return numero_1 + numero_2 + lista

# Definimos la lista con los 4 elementos enteros
lista_numeros = [1, 2, 3, 4]

# Definimos el número fijo
numero_fijo = 5
numero_2 = 3

# Usamos la función map para aplicar la función suma_elementos a cada elemento de la lista
resultado = list(map(lambda x: suma_elementos(numero_fijo,numero_2, x), lista_numeros))

# Imprimimos el resultado
print(resultado)