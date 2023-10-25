#### Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)

##proceso

def leernumero():
    try:
        numero = int(input("Dame tu edad: "))
        return numero
    except ValueError:
        print('Por favor, introduzca un número válido.')
        return leernumero()

def proceso(numero):
    resultado = []
    for numeros in range(numero):
        resultado.append(f"Tienes {numeros+1} años")
    return resultado

def mensaje():
    numero = leernumero()
    resultado = proceso(numero)
    for r in resultado:
        print(r)

if __name__ == "__main__":
    
    ##salida 
    
    mensaje()
