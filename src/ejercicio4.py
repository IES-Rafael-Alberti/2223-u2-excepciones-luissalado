#### Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, 
# mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.


##proceso
def pedir_numero_entero():
    try:
        numero = int(input("ingrese un numero entero: "))
        return numero
    except ValueError:
        print("La entrada no es correcta.")
        raise

if __name__ == "__main__":
    
    #salida
    try:
        resultado = pedir_numero_entero()
        print("El numero es:", resultado)
    except ValueError:
        print("Ha ocurrido un error ")