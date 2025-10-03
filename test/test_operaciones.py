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


def test_restar_con_fixture(numeros):
     a,b = numeros
     assert Calculadora.restar(a,b) == 0


def test_sumar_con_fixture(numeros):
     a,b = numeros
     assert Calculadora.sumar(a,b) == 10



#Sistema de login
     #Para el login se necesita usuario y password
#Aparte del sistema de login hay credenciales = correctas
def login(usuario,password, usuario_correcto):
     return usuario == usuario_correcto["nombre"] and password == usuario_correcto["password"]

@pytest.mark.parametrize(       #para pasar más de un dato de prueba y poder evaluarlos con el parametrize
     "usuario, password, esperado", [
          ("pepito", "123", False),
          ("Ale", "123456", True),
          ("","123", False)
     ]
)

def test_login(usuario, password, esperado, usuario_correcto):
     resultado = login(usuario, password, usuario_correcto)
     assert resultado == esperado





#Sistema de envío de email, que se necesita ?? ==
     #Destinatario  alerimasa92@gmail.com

def enviar_email(destinatario):
     if '@' not in destinatario:
          return False
     return True


@pytest.fixture
def email_send():
     return enviar_email


#Casos de prueba

@pytest.mark.parametrize(
     "correo, esperado" ,[
          ("usuario@gmail.com", True),
          ("empresa@empresa.com", True),
          ("correo_invalido", False)
     ] 
)

def test_envio_de_email(correo, esperado, email_send):
     resultado = email_send(correo)
     assert resultado == esperado