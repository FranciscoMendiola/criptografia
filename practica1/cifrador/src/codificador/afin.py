 # src/codificador/afin.py
MOD = 256

def _egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = _egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def _modinv(a, m=MOD):
    a = a % m
    g, x, _ = _egcd(a, m)
    if g != 1:
        raise ValueError(f"No existe inverso modular para {a} mod {m}.")
    return x % m

def decodificar_bytes(data: bytes, a: int, b: int) -> bytes:
    if not (0 <= a < MOD and 0 <= b < MOD):
        raise ValueError("a y b deben estar en el rango 0..255.")
    return bytes(((a * x + b) % MOD for x in data))

def codificar_bytes(data: bytes, a: int, b: int) -> bytes:
    if not (0 <= a < MOD and 0 <= b < MOD):
        raise ValueError("a y b deben estar en el rango 0..255.")
    inv = _modinv(a, MOD)
    return bytes(((inv * ((x - b) % MOD)) % MOD for x in data))
