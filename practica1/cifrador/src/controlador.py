import os
from src.codificador import base64 as b64
from src.buffer import leer_archivo, escribir_archivo

def procesar_base64(params):
    entrada = params["file"]
    decode = bool(params.get("decode"))
    extension = params.get("extension", "")

    # Leer archivo de entrada
    data = leer_archivo(entrada)

    # (De)codificar
    resultado = b64.decodificar_bytes(data) if decode else b64.codificar_bytes(data)

    # Guardar en la carpeta del proyecto
    salida = _ruta_salida(entrada, extension, decode)
    escribir_archivo(salida, resultado)
    return salida






def _proyecto_root() -> str:
    """
    Devuelve la ruta absoluta a la carpeta del proyecto (la que contiene 'src').
    Este archivo está en .../cifrador/src/controlador.py, así que subimos un nivel.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def _ruta_salida(path_entrada: str, extension: str, decode: bool) -> str:
    """
    Crea la ruta de salida dentro de <proyecto>/file_code o <proyecto>/file_decode.
    Nombre: <nombre_base>_code.<ext> o <nombre_base>_decode.<ext>
    """
    base_name = os.path.splitext(os.path.basename(path_entrada))[0]
    subdir = "file_decode" if decode else "file_code"

    out_dir = os.path.join(_proyecto_root(), subdir)
    os.makedirs(out_dir, exist_ok=True)

    sufijo = "decode" if decode else "code"
    ext = extension.lstrip('.')
    nombre = f"{base_name}_{sufijo}.{ext}" if ext else f"{base_name}_{sufijo}"
    return os.path.join(out_dir, nombre)