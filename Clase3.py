#Estructura de datos

print("--------Listas------")
print("Muestro mi lista - Se muestra por posición")
mi_lista = ['Argentina', 200, True]
#como se accede
print(mi_lista[0])

print("Añade un dato a una lista: ")
mi_lista.append(5000)
mi_lista.insert(1,"Paises bajos")

print("Muestro mi lista con un dato más añadido.")
print(mi_lista)


print("--------Tuplas------")
mi_tupla = ("Celeste", 200, "Rojo")

#Como se accede, mediante la posición
print(mi_tupla[1]) 

#Error SON INMUTABLES NO SE PUEDE CAMBIAR EL VALOR
#mi_tupla[0] = "Ramiro"




print("--------Diccionario------") #Estructura tipo dato valor

persona = {
    "nombre" : "Jaime",
    "apellido" : "Desconocido",
    "edad" : 34
}
print("--------acceder al valor que tiene cada clave------")
#Como acceder al valor que tiene cada clave..
print(persona["apellido"])

print("--------acceder a los valores------")
#Como acceder a los valores (variables)
print(persona.values())

print("--------acceder a todas las claves(datos)------")
#Como acceder a todas las claves(datos) del diccionario
print(persona.keys())

print("--------acceder a los valores y clave------")
#Como acceder a los valores y clave (variables y datos)
print(persona.items())


print("--------Recorrer lista--------")

for i in mi_lista:
    print(i)





print("\n") 
print("--------Funciones--------")

def saludo():
    print('Hola')

saludo()

print("--------Funciones por Parámetros--------")

def saludo(nombre):
    return f'Hola {nombre}' # f string, permite concatenar en una sola expresión diferentes tipos de datos varios tipos de datos.

print(saludo('Alejandro'))

print("\n") 
print("--------Manejo de errores o Excepciones--------")
print("--------ZeroDivisionError--------")

try:
    resultado = 10 / 0
except ZeroDivisionError:   
    print(f'Error : No se puede dividir entre 0')

try:
    resultado = 10 / 0
except ZeroDivisionError as e:   #El "As e" permite ver el error
    print(f'Error : {e}')

print("\n")
print("--------Value Error--------")
try:
    numero = int ('abc') #Esto no es correcto, en consola te va a mostrar un error en base 10 (no es un numero)
except ValueError as e:   #El "As e" permite ver el error
    print(f'Error : {e}')


try:
    numero2 = int ('123') #Esto no es correcto, en consola te va a mostrar un error en base 10 (no es un numero)
    print(numero2)
except ValueError as e:   #El "As e" permite ver el error
    print(f'Error : {e}')

print("\n")
print("--------KeyError--------")

people = { #Diccionario
     "nombre" : "Jaime",
     "edad" : 34
}

try:
    print(people['nombre']) #Si le pongo otro dato me muestra el error.
except KeyError as e:
    print('la clave no existe')