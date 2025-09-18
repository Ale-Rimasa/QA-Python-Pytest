def sumar( a , b):
    return a + b

def restar (a , b):
    return a + b

def dividir (a, b):
    return a // b #Con 2 comillas de vuelve el número entero

def multiplicar (a , b):
    return a * b


def calculadora_simple(operacion , a , b):

    try:

        a = int(a) #Parseo para convertir en número
        b = int(b)

        if operacion == 'sumar':
            return sumar(a,b)
        elif operacion == 'restar':
             return restar(a,b)
        elif operacion == 'dividir':
            return dividir(a,b)
        elif operacion == 'multiplicar':
            return multiplicar(a,b)
        else:
            return KeyError('Opración no válida')
    except ZeroDivisionError:
            return 'Error: No se puede dividir por cero'
    except ValueError:
        return 'Error: Ingrese un valor numérico'
    

print(calculadora_simple("dividir",7,7)) #1
print(calculadora_simple("sumar",7,3)) #10
print(calculadora_simple("multiplicar",7,3)) #21
print(calculadora_simple("restar",7,3))  # 4
print(calculadora_simple("dividir",7,0)) #Error Zero
print(calculadora_simple("dividir","A",3)) #Error Value
print(calculadora_simple("dividirr",7,3)) #Error Keyeerror


print("\n")
print("--------2do Ejemplo--------")

usuario ={
    "ana": {"edad": 56},
    "jose": {"edad": 66}
}

def pedirNombre():
    try:
        nombre = input('Ingrese el nombre: ')
        edad = usuario[nombre]["edad"] #Almaceno la edad que me ingresa el nombre del usuario
        print(f'{nombre} tiene {edad} años')
    except KeyError:
        print("Error : No se encontro la edad de ese nombre")

pedirNombre()