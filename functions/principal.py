from functions.entrada import pedir_datos  # se obtiene la funcion para pedir los datos al usuario

# función principal del programa
def main():
    url, formato, carpeta, nombre = pedir_datos() # obtenemos los datos necesarios del usuario

    print("\nDatos recibidos:")
    print(f"  URL:     {url}")
    print(f"  Formato: {formato}")
    print(f"  Carpeta: {carpeta}")
    print(f"  Nombre:  {nombre}")