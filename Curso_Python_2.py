"""
Funciones:
Para definir una función en Python, utilizamos la palabra clave def seguida del nombre de la 
función y paréntesis. Opcionalmente, podemos especificar parámetros dentro de los paréntesis. 
El bloque de código de la función se indenta después de los dos puntos.

"""


def saludo(nombre):
    print(f"Hola {nombre}")
    
    
saludo('miguel')

def suma(a, b):
    return a + b




print('Suma: ', suma(2,2))


#Funciones con numero variable de argumentos

def suma_vari(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total
    
print("Result de suma_vari", suma_vari(5,5,5))