#Esto es un comentario

"""
Esto es una 2da forma de comentario.
"""

'''
Esta es una 3er forma de comentario
'''

#Variables:

edad = 45 #(variable edad la asigno con el número 45)
nombre = "Luis"
altura = 1.60
esMayorDeEdad = True

#Tipos de Datos Primitivos:

#str => String => cadena texto
#int => Enteros
#float => Decimales
#bool => True o False

#Entrada y salida de datos

print(nombre) #Muestra en consola los datos.

input("Ingresa tu fruta favorita: ")

#Almacenamos la función input en una variable y luego la mostramos.

AnioDeNacimiento = int (input("Ingresa tu año de nacimiento: ")) # Convertimos el tipo de dato a entero con "INT" 
print(AnioDeNacimiento)

#Función que permite ver el tipo de dato "TYPE"
print(type(AnioDeNacimiento))


#Operaciones matemáticas
print("-----Operaciones matemáticas--------")
resultado = 3 + 2
print("Resultado de la suma")

potencia = 2**2
print("Resultado de la potencia")
print(potencia)

division = 10 / 5
print("Resultado de la división")
print(division)

divisionEntera = 10 // 5
print("Resultado de la división entera")
print(divisionEntera)

resto = 4 % 2
print("Resultado del resto")
print(resto)


#Operaciones relacionales

result = 5 == 2  #Evalua si son 2 iguales

#Operadores lógicos
#para que se cumpla el "AND" se evaluan 2 expresiones
#(edad01 => 18) and (licencia == True) => True

print ("-----Condicionales-----")

puntuacion = int(input("Ingrese una nota: - (0 - 10)"))

if puntuacion >= 9:
    print("Excelente")
elif puntuacion >= 8:
    print("bien")
else:
    print('desaprobado')


for i in range(0, 11, 2):
    print(i)
    
print("-------While------")


i = 1 #Variable iteradora

while i  <= 5: #me imprima las variables que me recorra
    print(i)
    i = i + 1 # o se puede usar "i += 1"