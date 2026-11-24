import os    # libreria para trabajar con rutas y archivos
from functions.validaciones import validar_url, validar_formato, validar_carpeta, validar_nombre  # se importan las funciones de validación


# funcion para pedir un dato al usuario y validarlo
def pedir(mensaje, validar, limpiar=None) -> str:
    # se repite la pregunta hasta que pase que la validación
    while True:
        valor = input(mensaje).strip()     # se obtiene el valor introducido por el usuario (sin espacios al incio ni al final)
        
        if limpiar: valor = limpiar(valor) # si se ha definido una función de limpieza, se aplica al valor introducido
        
        error = validar(valor)          # se valida el valor introducido
        
        if error is None: return valor  # si cumple la validación, se sale del bucle y se devuelve el valor introducido
        
        print(f"Error: {error}\n")      # si no cumple la validación, se muestra el mensaje de error y se repite la pregunta
    

# función para limpiar la ruta introducida por el usuario
def limpiar_ruta(ruta) -> str:
    return os.path.expanduser(ruta.strip("\"'")) # devuelve la ruta sin comillas y si tiene ~ hace que sea leible (MacOs y Linux)


# función para pedir y validarlos datos necesarios al usuario por consola
def pedir_datos() -> tuple:
    
    url = pedir("Introduce la URL de YouTube: ", validar_url) # se pide la URL y se valida
    
    formato = pedir("Indica el formato (mp3/mp4): ", validar_formato, limpiar=str.lower) # se pide el formato y se valida
    
    carpeta = pedir("Introduce la ruta de destino: ", validar_carpeta, limpiar=limpiar_ruta) # se pide la ruta y se valida
    
    nombre = pedir("Introduce el nombre del archivo resultante (sin extensión): ", validar_nombre) # se pide el nombre y se valida
    
    return url, formato, carpeta, nombre # se devuelve los datos introducidos por el usuario