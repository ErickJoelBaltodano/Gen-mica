import random
'''Definimos la clase Funciones, desde la cual realizaremos la implementación de dichas funciones que ocuparemos en Expansion.py'''
class Funcion:
    
    ''' Funcion que recibe como parametro una cadena semilla y que con probabilidad p
    mute alguna posición elegida con probabilidad uniforme de la cadena original y con 1-p
    la concatene con ella misma.'''
    @staticmethod
    def una_funcion(cadena: str, p: float) -> str:
        if random.random() < p:
            return Funcion.muta(cadena)
        else:
            return cadena + cadena
        

    
    @staticmethod
    def otra_funcion(iteraciones: int, probabilidad: float, cadena: str):
        resultado = cadena
        for _ in range(iteraciones):
            resultado = Funcion.una_funcion(resultado,probabilidad)
        return resultado


    # Método donde cambiamos un caracter elegido al azar.
    @staticmethod
    def muta(cadena: str) -> str:
        # Caso de la cadena vacía
        if not cadena:  
            return cadena
        # Generamos un indice al azar        
        i = random.randrange(len(cadena))  
        nuevo_bit = '1' if cadena[i] == '0' else '0'
        return cadena[:i] + nuevo_bit + cadena[i+1:]