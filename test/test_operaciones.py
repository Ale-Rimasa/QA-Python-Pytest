import pytest
import Calculadora


def test_sumar():
    assert  Calculadora.sumar(4,2) == 6              # Palabra clave que indica que todo lo que viene despues debe ser verdadero, acertado.


def test_restar():
    assert Calculadora.restar(3,1) == 2

def test_division_por_cero():
    with pytest.raises(ValueError):                        #Se abre o cierra el contenido dentro de este bloque de códig
          Calculadora.dividir(10,0)                        #raises: devuelve las expresiones de errores.              


#Marcadores

@pytest.mark.parametrize("a,b,esperado",[
    (2,5,7), #numero positivo
    (-4,-2,-6), #numero negativos
    (0,0,0) #numeros ceros
  
]) #Permite pasar 2 argumentos, un string y una lista

def test_sumar_varios(a,b,esperado):
     assert Calculadora.sumar(a,b) == esperado