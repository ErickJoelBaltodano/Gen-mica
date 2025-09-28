import random
import math

'''Algoritmo misterio misterioso.'''

#Inicializamos las variables
m = int (input('Ingrese un numero de iteraciones M: '))
d_mayuscula = 0

# Iteramos un número de m veces
for i in range(1, m + 1):
    # Calculamos dos números al azar entre -1 y 1
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    # Calculamos una especie de hipotenusa
    d = math.sqrt((x**2)+(y**2))

    # Contamos cuantas veces ocurrió el evento de que 1 fuera menor o igual a 1
    if (d <= 1):
        d_mayuscula += 1

# Terminamos de iterar y relizamos ciertas operaciones.        
x = (4 * (d_mayuscula))/i

print ('El resultado obtenido de nuestro algoritmo misterio misterioso fue: {}'.format(x))