from Funcion import *

#Recopilamos los parametros
cadena_inicial = input('Ingrese una cadena inicial con el alfabeto sigma igual a {0, 1}: ')
probabilidad = float(input('Ingrese una probabilidad: '))
iteraciones = int (input('Ingrese el numero de iteraciones: '))

#Aplicamos las funciones
cadena_final = Funcion.otra_funcion(10,probabilidad,cadena_inicial)

# Regresamos el resultado final
print(cadena_final)
