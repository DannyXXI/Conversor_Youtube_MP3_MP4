# Conversor de YouTube a MP3/MP4

Aplicación de consola en **Python** para descargar vídeos de YouTube y convertirlos a **MP3** o **MP4**.

## 📌 Descripción

Este proyecto permite:

- 🔗 Indicar la URL de un vídeo de YouTube.
- 🎞️ Elegir el formato de salida: MP3 (audio) o MP4 (vídeo).
- 📂 Escoger la carpeta de destino y el nombre del archivo resultante.
- ✅ Validar cada dato introducido y volver a pedirlo si no es correcto.
- 💬 Mostrar mensajes de error claros en español (vídeo privado, sin conexión, directo en curso...).

Este proyecto está pensado como una herramienta de aprendizaje sobre el uso de librerías externas, validación de datos y gestión de errores en Python.

## 🛠️ Tecnologías utilizadas

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/yt--dlp-FF0000?style=for-the-badge&logo=youtube&logoColor=white" />
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white" />
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Deno-000000?style=for-the-badge&logo=deno&logoColor=white" />
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
</p>

## 🎯 Objetivo

El objetivo principal de este proyecto es aprender a:

- Usar librerías externas como `yt-dlp` desde Python.
- Validar los datos introducidos por el usuario.
- Gestionar errores y mostrar mensajes personalizados.
- Organizar un proyecto en módulos y trabajar con ramas en Git.

## ⚙️ Requisitos

Antes de ejecutar el proyecto necesitas:

- Python **3.10 o superior**.
- Las dependencias del proyecto, que se instalarán dentro del entorno virtual.

No necesitas instalar **ffmpeg** ni **Deno** en el sistema ya que ambos se instalan dentro del entorno virtual.

## 📦 Instalación

1. Clona el repositorio.

2. Crea y activa un entorno virtual:
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## ▶️ Ejecución

Utiliza este comando desde la raíz del proyecto, con el entorno virtual activado:
```bash
python main.py
```

El programa te pedirá, en este orden:

```
Introduce la URL de YouTube: https://youtu.be/xxxxxxxxxxx
Indica el formato (mp3/mp4): mp3
Introduce la ruta de destino: C:\Descargas
Introduce el nombre del archivo resultante (sin extensión): cancion01

Descargando...

Listo: C:\Descargas\cancion01.mp3
```
## ✅ Validaciones

Si algún dato no cumple los requisitos, se muestra un mensaje de error y se vuelve a pedir **solo ese dato**.

| Dato | Requisito |
|------|-----------|
| **URL** | Debe ser de YouTube (`youtube.com`, `youtu.be`, `music.youtube.com`, etc). |
| **Formato** | Exactamente `mp3` o `mp4`. |
| **Carpeta** | Debe existir y tener permisos de escritura. |
| **Nombre** | Sin extensión, sin puntos ni espacios, sin caracteres especiales (`\ / : * ? " < > \|`) y con un máximo de 12 caracteres. |

## 📁 Estructura del proyecto

```
.
├── functions/
│   ├── __init__.py
│   ├── descarga.py          # descarga y conversión a MP4 y MP3
│   ├── entrada.py           # petición de datos por consola
│   ├── errores.py           # mensajes de error personalizados
│   ├── principal.py         # flujo principal del programa
│   └── validaciones.py      # reglas de validación de los datos
├── main.py                  # punto de entrada de la aplicación
├── requirements.txt         # dependencias del proyecto
├── LICENSE                  # licencia de uso
├── README.md                # este archivo
└── .gitignore               # archivos ignorados por Git
```


## 🚀 Próximas mejoras

- Avisar si ya existe un archivo con el mismo nombre antes de sobrescribirlo.
- Detectar los directos en curso antes de intentar descargarlos.
- Interfaz gráfica.

## 📄 Licencia

Este proyecto es de uso **exclusivamente educativo** y no se permite su modificación. Para cualquier otro uso, es necesario contactar con el autor.

## 👨‍💻 Autor

Proyecto desarrollado por **Daniel Requejo Expósito** ([@DannyXXI](https://github.com/DannyXXI)).