#Escribe un pequeño script que utilice un bucle para mostrar los primeros 10 números pares.
#Usa condicionales para validar y mostrar sólo los números pares.

print("Los primeros 10 números pares mostrados con un FOR son: ")

for i in range(0, 20, 2):
    print(i)

print("-----------------------------------------------------------")
#Mostrando con condicionales.
print("Los primeros 10 números pares mostrados con CONDICIONALES son: ")

contadorIndex = 0
num = 0

while contadorIndex < 10:
    if num % 2 == 0:
        print(num)
        contadorIndex += 1
    num += 1
