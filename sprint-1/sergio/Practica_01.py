# ==========================================================
# Desarrollo Web - Entorno Servidor
# Ciclo Superior Desarrollo Web
# Curso 2020-21
# Primera práctica
# ===========================================================

#   APELLIDOS, NOMBRE: AVILA CHACON, SERGIO
#   DNI: 29498790W

import math

# Práctica 1: Introducción a Python
# =================================

# En esta práctica veremos algunos ejercicios de Python, para ir
# familiarizándonos con el lenguaje.

# -----------
# EJERCICIO 1
# -----------
#
# Escribir una funcion cuadrados(l) que recibiendo una secuencia l de números,
# devuelve la lista de los cuadrados de esos números, en el mismo orden.

# Por ejemplo:
#
# >>> cuadrados([4,1,5.2,3,8])
# [16, 1, 27.040000000000003, 9, 64]

# Hacer dos versiones: una usando un bucle explícito, y la otra mediante
# definición de listas por comprensión.
# ---------------------------------------------------------------------------

def cuadradosComprensionLista (l):
    
    l = [x*x for x in l]
    return print(l)


def cuadradoBucle (l):
    for x in range(0,len(l)):
        l[x] = l[x]**2

    return print(l)


# -----------
# EJERCICIO 2
# -----------
# Definir una funcion vocales_consonantes(s), que reciba una cadena de
# caracteres s (de letras mayúsculas) y escribe por pantalla, una a una, si
# sus letras son vocales o  consonantes.
# Ejemplo:
# >>> vocales_consonantes("INTELIGENCIA")
# I es vocal
# N es consonante
# T es consonante
# E es vocal
# L es consonante
# I es vocal
# G es consonante
# E es vocal
# N es consonante
# C es consonante
# I es vocal
# A es vocal
# ---------------------------------------------------------------------------

def vocalesConsonantes (palabra):
    palabra_mayuscula = palabra.upper()

    vocales = ['A','E','I','O','U']
    
    for x in palabra_mayuscula:
        if x in vocales:
            print(x,' Es vocal')
        else:
            print(x,' Es consonante')


# -----------
# EJERCICIO 3
# -----------

# Usando como técnica principal la definición de secuancias por comprensión,
# definir las siguientes funciones:

# a) Dada una lista de números naturales, la suma de los cuadrados de los
#    números pares de la lista.

# Ejemplo:
# >>> suma_cuadrados([9,4,2,6,8,1])
# 120

def sumCuadrados(numeros):
    
    numeros = sum([x*x for x in numeros if x%2 == 0])
    
    return print('resultado', numeros)


# b) Dada una lista de números l=[a(1),...,a(n)], calcular el sumatorio de i=1
#    hasta n de i*a(i).

# Ejemplo:

# >>> suma_fórmula([2,4,6,8,10])
# 110

def sumFormula(numeros):
 
    numeros = sum([(x+1) *numeros[x] for x in range(len(numeros))])

    return print('resultado', numeros)


# c) Dados dos listas numéricas de la misma longitud, representado dos puntos
#    n-dimensionales, calcular la distancia euclídea entre ellos.

# Ejemplo:

# >>> distancia([3,1,2],[1,2,1])
# 2.449489742783178

def distancia(lista1,lista2):
    import math
    if len(lista1) == len(lista2):
        solucion = math.sqrt(sum([(lista1[x] - lista2[x]) for x in range(len(lista1)) for x in range(len(lista2))]))
        return print(solucion)         
    else:
        return print('ERROR:Se necesitan listas de la misma longitud')


# d) Dada una lista y una funcion de un argumento, devolver la lista de los
#    resultados de aplicar la funcion a cada elelmento de la lista.

# Ejemplo:

# >>> map_mio(abs,[-2,-3,-4,-1])
# [2, 3, 4, 1]

def map_mio(funcion, lista):
    
    lista = [funcion(x) for x in lista]

    return print (lista)

#EJERCICIO UTILIZANDO ZIP
# e) Dada un par de listas (de la misma longitud) y una funcion de dos
#    argumentos, devolver la lista de los resultados de aplicar la funcion a
#    cada par de elementos que ocupan la misma posición en las listas de
#    entrada.

# Ejemplo:
# >>> map2_mio((lambda x,y: x+y) ,[1,2,3,4],[5,2,7,9])
# [6, 4, 10, 13]

def map_mio2(funcion, lista1, lista2):
    
    solucion = [funcion(x,y) for x,y in zip(lista1,lista2)  ]
    return print (solucion)

# f) Dada una lista de números, contar el número de elementos que sean múltiplos
#    de tres y distintos de cero.

# Ejemplo:

# >>> m3_no_nulos([4,0,6,7,0,9,18])
# 3

def map_no_nulos(lista):
    
    solucion = sum([lista.count(x) for x in lista if x%3==0 and x !=0])
    return print(solucion)



# f) Dadas dos listas de la misma longitud, contar el número de posiciones en
#    las que coinciden los elementos de ambas listas.

# Ejemplo:

# >>> cuenta_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6])
# 3

def cuenta_coincidentes(lista1,lista2):
    solucion = len([x for x in range(len(lista1)) if lista1[x] == lista2[x]])
    return print(solucion)

# g) Dadas dos listas de la misma longitud, devolver un diccionario que tiene
# como claves las posiciones  en las que coinciden los elementos de ambas
# listas, y como valor de esas claves, el elemento coincidente.

# Ejemplos:

# >>> dic_posiciones_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6])
# {1: 2, 3: 8, 4: 9}
# >>> dic_posiciones_coincidentes([2,8,1,2,1,3],[1,8,1,2,1,6])
# {1: 8, 2: 1, 3: 2, 4: 1}

def dic_posiciones_coincidentes(lista1,lista2):
    solucion = dict([[x,lista1[x]] for x in range(len(lista1)) if lista1[x] == lista2[x]])
    return print (solucion)


# -----------
# EJERCICIO 4
# -----------
# Un número es perfecto si es la suma de todos sus divisores (excepto él
# mismo). Definir una función filtra_perfectos(n,m,p) que imprime por pantalla
# todos los números perfectos entre n y m que cumplen la condición p. Se pide
# también que se indiquen los divisores de cada número perfecto que se
# imprima.

# Ejemplo:

# >>> filtra_perfectos(3,500, lambda x: True)
# El 6 es perfecto y sus divisores son [1, 2, 3]
# El 28 es perfecto y sus divisores son [1, 2, 4, 7, 14]
# El 496 es perfecto y sus divisores son [1, 2, 4, 8, 16, 31, 62, 124, 248]

# >>> filtra_perfectos(3,500, lambda x: (x%7==0))
# El 28 es perfecto y sus divisores son [1, 2, 4, 7, 14]
# ------------------------------------------------------------------------

def divisores(x):
    return [i for i in range(1, x) if x % i == 0]


def filtra_perfectos(numeroInicial,numeroFinal,funcion):
    for x in range(numeroInicial, numeroFinal+1):
        if (x == sum(divisores(x)) and funcion(x)):
            print("El " , x , " es perfecto y sus divisores son " , divisores(x))


##    for x in range(a,b+1):
##        if sum(multiplos(x)) == x:
##            if f(x):
##                print ( "El " , x , " es perfecto y sus divisores son " , multiplos(x))
# -----------
# EJERCICIO 5
# -----------
#
# Supongamos que recibimos un diccionario cuyas claves son cadenas de
# caracteres de longitud uno y los valores asociados son números enteros
# entre 0 y 50.
# Definir una funcion histograma_horizontal(d), que recibiendo un diccionario
# de ese tipo, escribe un histograma de barras horizontales asociado,
# como se ilustra en el siguiente ejemplo:

# >>> d1={"a":5,"b":10,"c":12,"d":11,"e":15,"f":20,
#         "g":15,"h":9,"i":7,"j":2}
# >>> histograma_horizontal(d1)
# a: *****
# b: **********
# c: ************
# d: ***********
# e: ***************
# f: ********************
# g: ***************
# h: *********
# i: *******
# j: **
#
# Nota: imprimir las barras, de arriba a abajo, en el orden que determina la
#         función "sorted" sobre las claves
# ---------------------------------------------------------------------------

d1={"a":5,"b":10,"c":12,"d":11,"e":15,"f":20,"g":15,"h":9,"i":7,"j":2}

def histograma_horizontal(d1):


##    for x,y in sorted(d1.items()):
##        print( x , ": ", y * '*')

# -----------
# EJERCICIO 6
# -----------
# Con la misma entrada que el ejercicio anterior, definir una funcion
# histograma_vertical(d) que imprime el mismo histograma pero con las barras
# en vertical.

# Ejemplo:

# >>> d2={"a":5,"b":7,"c":9,"d":12,"e":15,"f":20,
#         "g":15,"h":9,"i":7,"j":2}
# >>> histograma_vertical(d2)
#           *
#           *
#           *
#           *
#           *
#         * * *
#         * * *
#         * * *
#       * * * *
#       * * * *
#       * * * *
#     * * * * * *
#     * * * * * *
#   * * * * * * * *
#   * * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# a b c d e f g h i j

# Nota: imprimir las barras, de izquierda a derecha, en el orden que determina la
#         función "sorted" sobre las claves
# ---------------------------------------------------------------------------

d2={"a":5,"b":7,"c":9,"d":12,"e":15,"f":20,"g":15,"h":9,"i":7,"j":2}

#Buscamos el máximo de todos para saber por cual empezar.

def histograma_vertical(d2):
