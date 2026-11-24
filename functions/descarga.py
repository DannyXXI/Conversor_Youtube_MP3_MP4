import os              # librería para trabajar con rutas y archivos
import imageio_ffmpeg  # librería para trabajar con ffmpeg sin tener que instalarlo
import yt_dlp          # librería para descargar videos de YouTube


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

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl: ydl.download([url]) # se descarga el video con las opciones definidas
        
        return True # si todo ha salido bien, se devuelve True
    
    except yt_dlp.utils.DownloadError as error:
        
        print(f"\nError al descargar: {error}") # si habido un error al descargar, se muestra el error al usuario
        
        return False # si ha habido un error, se devuelve False


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

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl: ydl.download([url]) # se descarga el video con las opciones definidas
        
        return True # si todo ha salido bien, se devuelve True
    
    except yt_dlp.utils.DownloadError as error:
        
        print(f"\nError al descargar: {error}") # si habido un error al descargar, se muestra el error al usuario
        
        return False # si ha habido un error, se devuelve False

