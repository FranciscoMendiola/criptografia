# src/codificador/afin.py
from . import decimado, cesar

def codificar_bytes(data: bytes, a: int, b: int) -> bytes:
    """
    Cifrado afín: aplica primero decimado (multiplicación por a mod 256)
    y luego César (suma b mod 256).
    """
    data = decimado.codificar_bytes(data, a)
    data = cesar.codificar_bytes(data, b)
    return data

def decodificar_bytes(data: bytes, a: int, b: int) -> bytes:
    """
    Descifrado afín: primero revertir César (restar b),
    después revertir decimado (multiplicar por a^{-1} mod 256).
    """
    data = cesar.decodificar_bytes(data, b)
    data = decimado.decodificar_bytes(data, a)
    return data
