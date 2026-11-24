from functions.entrada import pedir_datos  # se obtiene la funcion para pedir los datos al usuario
from functions.descarga import descargar_mp3, descargar_mp4  # se obtiene las funciones para descargar el video de Youtube en MP4 y MP3

# función principal del programa
def main():
    url, formato, carpeta, nombre = pedir_datos() # obtenemos los datos necesarios del usuario
    
    # comprobamos el formato elegido por el usuario
    if formato == "mp4":
        print("\nDescargando...\n") # se muestra un mensaje indicando que se está descargando el vídeo
        
        # se descarga el video en formato MP4 y se le indica al usuario si la descarga fue existosa
        if descargar_mp4(url, carpeta, nombre): print(f"\nListo: {carpeta}\\{nombre}.mp4")
    
    else:
        print("\nDescargando...\n") # se muestra un mensaje indicando que se está descargando el vídeo
                
        # se descarga el video en formato MP3 y se le indica al usuario si la descarga fue existosa
        if descargar_mp3(url, carpeta, nombre): print(f"\nListo: {carpeta}\\{nombre}.mp3")