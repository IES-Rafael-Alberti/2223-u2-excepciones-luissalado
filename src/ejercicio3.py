### Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás 
# desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.

## proceso 


def leernumero():
    try:
        numero = int(input("Introduzca un numero entero positivo: "))
        if numero > 0:
            return numero
        else:
            raise ValueError("Es un numero negativo.")
    except ValueError:
        print('Por favor, introduzca un número válido.')
        return leernumero()
    
numero = leernumero()

def cuantatras(numero):
    listanum = []
    for num in range(numero+1):
        listanum.append(num)
    listanum.reverse()
    return listanum

def mensaje():
    numeros = cuantatras(numero)
    for x in numeros:
        print(x, end=", ")

if __name__ == "__main__":
    
    ##salida
    mensaje()