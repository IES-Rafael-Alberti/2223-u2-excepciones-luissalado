#### Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

## Proceso

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
    
numero =leernumero()  

def comprobarpar(numero):
    listanum = []
    for num in range(1,numero):
        if num % 2 == 0:
            pass
        else:
            listanum.append(num)
    return listanum

def mensaje():
    print(comprobarpar(numero))
    
    
if __name__ == "__main__":
    ## salida
    
    mensaje()