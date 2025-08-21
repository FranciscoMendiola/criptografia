import base64

def codificar_bytes(data: bytes) -> bytes:

    return base64.b64encode(data)

def decodificar_bytes(data: bytes) -> bytes:
    return base64.b64decode(data, validate=True)
