import os                           # libreria para trabajar con rutas y archivos
from urllib.parse import urlparse   # libreria para analizar URLs


DOMINIOS_YOUTUBE = {"youtube.com", "www.youtube.com", "m.youtube.com", "music.youtube.com", "youtu.be",} # dominios válidos
FORMATOS_VALIDOS = {"mp3", "mp4"}      # formatos válidos
MAX_NOMBRE = 20                        # longitud máxima del nombre del archivo resultante
CARACTERES_PROHIBIDOS = '\\/:*?"<>|'   # caracteres prohibidos en los nombres de archivo


# función para validar la URL de YouTube
def validar_url(url) -> str | None:
    if not url: return "La URL no puede estar vacía." # detecta si la URL está vacía
    
    partes = urlparse(url) # divide la URL en partes (protocolo, dominio, ruta, etc)
    
    # si el protocolo no es HTTP o HTTPS, o el dominio no es uno de los válidos de Youtube, se muestra un mensaje de error
    if partes.scheme not in ("http", "https") or partes.hostname not in DOMINIOS_YOUTUBE: return "Debe ser una URL de YouTube."

    return None # si la URL es válida, devuelve None


# función para validar el formato escogido para el archivo resultante
def validar_formato(formato) -> str | None:
    # si el formato no es uno de los válidos, se muestra un mensaje de error
    if formato not in FORMATOS_VALIDOS: return "El formato debe ser exactamente mp3 o mp4."
    
    return None # si el formato es válido, devuelve None


# función para validar la ruta de la carpeta donde se guardará el archivo resultante
def validar_carpeta(carpeta) -> str | None:
    if not carpeta: return "La ruta no puede estar vacía." # detecta si la ruta está vacía
    
    if not os.path.isdir(carpeta): return "La carpeta no existe." # detecta si la ruta no es una carpeta válida
    
    # detecta si el usuario tiene permisos de escritura en la carpeta
    if not os.access(carpeta, os.W_OK): return "No tienes permiso de escritura en esa carpeta."
    
    return None # si la ruta es válida, devuelve None


# función para validar el nombre del archivo resultante
def validar_nombre(nombre) -> str | None:
    if not nombre: return "El nombre no puede estar vacío." # detecta si el nombre del archivo está vacío
    
    # detecta si el nombre del archivo supera la longitud máxima permitida
    if len(nombre) > MAX_NOMBRE: return f"Máximo {MAX_NOMBRE} caracteres (has escrito {len(nombre)})."
    
    # detecta si el nombre del archivo contiene puntos y comas
    if "." in nombre or "," in nombre: return "No puede contener puntos ni comas." 
    
    if " " in nombre: return "No puede contener espacios." # detecta si el nombre del archivo contiene espacios
    
    # detecta si el nombre del archivo contiene alguno de los caracteres definidos como prohibidos
    if any(c in CARACTERES_PROHIBIDOS for c in nombre): return f"No puede contener estos caracteres: {CARACTERES_PROHIBIDOS}"
    
    return None # si el nombre es válido, devuelve None