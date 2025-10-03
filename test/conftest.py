import pytest

@pytest.fixture #Sirve para establecer un test

def numeros(): 
    return 5,5

#Para el login
@pytest.fixture
def usuario_correcto():
    return{"nombre": "Ale" , "password": "123456"} #Diccionario clave valor




