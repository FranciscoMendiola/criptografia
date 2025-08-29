# src/codificador/cesar.py

def codificar_bytes(data: bytes, shift: int = 3) -> bytes:
    """César binario: desplaza cada byte (mod 256)."""
    s = shift % 256
    return bytes(((b + s) % 256 for b in data))

def decodificar_bytes(data: bytes, shift: int = 3) -> bytes:
    """Revierte el cifrado César binario."""
    s = shift % 256
    return bytes(((b - s) % 256 for b in data))
