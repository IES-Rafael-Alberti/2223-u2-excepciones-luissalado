### Escribir que solicite una contraseña, y si no coincide con la que se tiene, 
# lance la excepción NameError con el mensaje, "Incorrect Password!!"


## proceso

def verificar_contrasena(contrasena_ingresada, contrasena_correcta):
    if contrasena_ingresada != contrasena_correcta:
        raise NameError("Incorrect Password!!")

if __name__ == "__main__":
    
    ##salida
    contrasena_correcta = "contraseña"  

    try:
        contrasena_ingresada = input("ingrese la contraseña: ")
        verificar_contrasena(contrasena_ingresada, contrasena_correcta)
        print("Contraseña correcta. Acceso permitido.")
    except NameError:
        print("Acceso denegado. Vuelve a intentarlo.")