# lista de errores conocidos con sus respectivos mensajes de error para el usuario
ERRORES_CONOCIDOS = [
    (("private video",),
     "El vídeo es privado y no se puede descargar."),
    (("video unavailable", "this video is no longer available", "has been removed"),
     "El vídeo no está disponible (eliminado, o la URL es incorrecta)."),
    (("sign in to confirm your age", "age-restricted", "age restricted"),
     "El vídeo tiene restricción de edad y requiere iniciar sesión."),
    (("members-only", "join this channel"),
     "El vídeo es solo para miembros del canal."),
    (("not available in your country", "blocked it in your country", "geo"),
     "El vídeo está bloqueado en tu país."),
    (("sign in to confirm you're not a bot", "sign in to confirm you’re not a bot"),
     "YouTube ha bloqueado temporalmente la petición. Prueba de nuevo más tarde."),
    (("live event", "is live", "premieres in"),
     "Es un directo o un estreno aún sin terminar. Espera a que finalice."),
    (("http error 429", "too many requests"),
     "Demasiadas peticiones seguidas. Espera unos minutos y reintenta."),
    (("unable to download webpage", "getaddrinfo failed",
      "name resolution", "timed out", "urlopen error", "connection"),
     "No hay conexión a internet o no se puede acceder a YouTube."),
    (("ffmpeg",),
     "Ha fallado la conversión (problema con ffmpeg)."),
    (("requested format is not available",),
     "No hay ningún formato descargable. Suele ocurrir con directos en curso o estrenos que aún no han terminado."),
]


# función para traducir los errores de yt-dlp a mensajes claros para el usuario
def traducir_error(error) -> str:
    texto = str(error).lower()   # se convierte el error en un texto en minúsculas para compararlo con los errores conocidos
    
    # se recorre la lista de errores conocidos
    for claves, mensaje in ERRORES_CONOCIDOS:
        # si el error conocido coincide con el error recibido, se devuelve el mensaje correspondiente
        if any(clave in texto for clave in claves): return mensaje
        
    # si el error no coincide con los errores conocidos, se devuelve un mensaje con el detalle técnico del error
    detalle = str(error).replace("ERROR: ", "").strip()
    
    return f"Error inesperado al descargar.\nDetalle técnico: {detalle}" # se devuelve el mensaje con el detalle técnico del error