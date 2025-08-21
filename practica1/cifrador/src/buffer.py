def leer_archivo(ruta: str) -> bytes:
    """
    Lee un archivo en modo binario y devuelve sus bytes.
    """
    with open(ruta, "rb") as f:
        return f.read()

def escribir_archivo(ruta: str, data: bytes):
    """
    Escribe bytes en un archivo en modo binario.
    """
    with open(ruta, "wb") as f:
        f.write(data)
