import os              # librería para trabajar con rutas y archivos
import imageio_ffmpeg  # librería para trabajar con ffmpeg sin tener que instalarlo
import yt_dlp          # librería para descargar videos de YouTube
from functions.errores import traducir_error  # función para traducir los errores de yt-dlp a mensajes para el usuario


# función para descargar un video de YouTube en formato MP4
def descargar_mp4(url, carpeta, nombre) -> bool:
    nombre_seguro = nombre.replace("%", "%%") # se reemplaza el simbolo % por %% para evitar que yt-dlp lo malinterprete
    
    # se definen las opciones para descargar el video
    opciones = {
        # formato de descarga (mejor calidad de video y audio, sino mejor calidad de video y si no lo mejor que haya)
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "merge_output_format": "mp4",  # formato de salida del video (MP4)
        "outtmpl": os.path.join(carpeta, nombre_seguro + ".%(ext)s"), # ruta y nombre del archivo de salida
        "ffmpeg_location": imageio_ffmpeg.get_ffmpeg_exe(),           # ruta del ejecutable del ffmpeg (para unir video y audio)
        "noplaylist": True,  # indica que no se descargue la playlist completa (solo el vídeo)
    }

    return descargar(opciones, url) # se descarga el video con las opciones definidas


# función para descargar un video de YouTube en formato MP3
def descargar_mp3(url, carpeta, nombre) -> bool:
    nombre_seguro = nombre.replace("%", "%%") # se reemplaza el simbolo % por %% para evitar que yt-dlp lo malinterprete
    
    # se definen las opciones para descargar el video
    opciones = {
        "format": "bestaudio/best", # formato de descarga (mejor calidad de audio)
        "merge_output_format": "mp3",  # formato de salida del audio (MP3)
        "outtmpl": os.path.join(carpeta, nombre_seguro + ".%(ext)s"), # ruta y nombre del archivo de salida
        "ffmpeg_location": imageio_ffmpeg.get_ffmpeg_exe(),           # ruta del ejecutable del ffmpeg (para unir video y audio)
        "noplaylist": True,  # indica que no se descargue la playlist completa (solo el vídeo)
        "postprocessors": [  # indica que se realizará postprocesamiento del archivo descargado
            {
                "key": "FFmpegExtractAudio", # indica que se va extraer el audio del video descargado
                "preferredcodec": "mp3",     # indica el formato de salida del audio (MP3)
                "preferredquality": "320",   # indica la calidad del audio (320 kbps)
            }
        ],
        
    }

    return descargar(opciones, url) # se descarga el video con las opciones definidas


# función para descargar un video de Youtube con las opciones definidas
def descargar(opciones, url) -> bool:
    try:
        with yt_dlp.YoutubeDL(opciones) as ydl: ydl.download([url]) # se descarga el video con las opciones definidas
            
        return True # si todo ha salido bien, se devuelve True
        
    except yt_dlp.utils.DownloadError as error:
        
        print(f"\nError: {traducir_error(error)}") # mensaje de error de yt-dlp traducido a un mensaje claro para el usuario
        
    except OSError as error:
        
        print(f"\nError al guardar el archivo: {error}") # mensaje de error si hay un problema al guardar el archivo
        
    except KeyboardInterrupt:
        
        print("\nDescarga cancelada.") # mensaje de error si el usuario cancela la descarga con Ctrl+C

    return False # si ha habido un error, se devuelve False