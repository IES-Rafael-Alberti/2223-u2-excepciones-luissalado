from src.ejercicio5 import verificar_contrasena
import pytest


def verificar_contrasena(contrasena_ingresada, contrasena_correcta):
    if contrasena_ingresada != contrasena_correcta:
        raise NameError("Incorrect Password!!")

def test_verificar_contrasena_correcta():
    contrasena_correcta = "contrasena"
    contrasena_ingresada = "contrasena"
    try:
        verificar_contrasena(contrasena_ingresada, contrasena_correcta)
    except NameError as e:
        pytest.fail(f"Se lanzó una excepción de manera incorrecta: {e}")

def test_verificar_contrasena_incorrecta():
    contrasena_correcta = "contrasena123"
    contrasena_ingresada = "contrasena456"
    with pytest.raises(NameError, match="Incorrect Password!!"):
        verificar_contrasena(contrasena_ingresada, contrasena_correcta)