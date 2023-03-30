import random
import string

def generar_contrasena(longitud):
    # Selecciona una combinación aleatoria de letras minúsculas, mayúsculas y números
    caracteres = string.ascii_letters + string.digits
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

def guardar_contrasena(nombre_contrasena, contrasena):
    with open("contraseñas.txt", "a") as archivo:
        archivo.write(f"{nombre_contrasena}: {contrasena}\n")
    print("Contraseña guardada exitosamente.")

def buscar_contrasena(nombre_contrasena):
    with open("contraseñas.txt", "r") as archivo:
        for linea in archivo:
            if linea.startswith(nombre_contrasena + ":"):
                return linea.strip().split(": ")[1]
    return None

# Pedir al usuario que ingrese un comando
comando = input("Ingresa un comando (o presiona Enter para salir): ")

# Generar y guardar una contraseña
if comando == "/gen":
    longitud_contrasena = 12
    contrasena = generar_contrasena(longitud_contrasena)
    print(f"Tu nueva contraseña es: {contrasena}")

    # Preguntar si se desea guardar la contraseña
    respuesta = input("¿Deseas guardar esta contraseña? (s/n): ")
    if respuesta.lower() == "s":
        nombre_contrasena = input("Ingresa un nombre para la contraseña: ")
        guardar_contrasena(nombre_contrasena, contrasena)
    else:
        print("Contraseña no guardada.")

# Buscar una contraseña guardada
elif comando == "/search":
    nombre_contrasena = input("Ingresa el nombre de la contraseña que deseas buscar: ")
    contrasena = buscar_contrasena(nombre_contrasena)
    if contrasena is not None:
        print(f"La contraseña para {nombre_contrasena} es: {contrasena}")
    else:
        print(f"No se encontró una contraseña con el nombre {nombre_contrasena}.")

# Salir
else:
    print("Saliendo...")
