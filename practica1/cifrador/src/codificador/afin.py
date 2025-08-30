from src.codificador import cesar
from src.codificador import decimado 

def codificar_bytes(data: bytes, a: int, b: int) -> bytes:

    multiplied = decimado.codificar_bytes(data, a)
    shifted = cesar.codificar_bytes(multiplied, b)
    return shifted

def decodificar_bytes(data: bytes, a: int, b: int) -> bytes:
    
    shifted = cesar.decodificar_bytes(data, b)
    multiplied = decimado.decodificar_bytes(shifted, a)
    return multiplied