# función para pedir los datos necesarios al usuario por consola
def pedir_datos() -> tuple:
    url = input("Introduce la URL de YouTube: ").strip()
    
    formato = input("Indica el formato (mp3/mp4): ").strip().lower()
    
    carpeta = input("Introduce la ruta de destino: ").strip()
    
    nombre = input("Introduce el nombre del archivo resultante (sin extensión): ").strip()
    
    return url, formato, carpeta, nombre # se devuelve los datos introducidos por el usuario