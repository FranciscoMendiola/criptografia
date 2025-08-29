 # src/codificador/decimado.py

from typing import Iterable, Tuple

MOD = 256

def _egcd(a: int, b: int) -> Tuple[int, int, int]:
    """Extended GCD: regresa (g, x, y) tal que a*x + b*y = g = gcd(a,b)."""
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = _egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def _modinv(a: int, m: int = MOD) -> int:
    """Inverso modular de a modulo m. Lanza ValueError si no existe."""
    a = a % m
    g, x, _ = _egcd(a, m)
    if g != 1:
        raise ValueError(f"No existe inverso modular para {a} (mod {m}); gcd={g}. "
                         "Asegúrate de que la llave sea impar y coprima con 256.")
    return x % m

def _mul_mod_256_stream(data: Iterable[int], k: int) -> bytes:
    """Multiplica cada byte por k mod 256."""
    k = k % MOD
    return bytes(((b * k) % MOD for b in data))

def codificar_bytes(data: bytes, key: int) -> bytes:
    """
    Decimado binario (MOD 256) - C = a * key (mod 256)
    - data: bytes de entrada
    - key: llave multiplicativa (0..255). Para descifrar luego, key debe ser coprima con 256 (impar).
    """
    if not (0 <= key <= 255):
        raise ValueError("La llave debe estar en el rango 0..255.")
    return _mul_mod_256_stream(data, key)

def decodificar_bytes(data: bytes, key: int) -> bytes:
    """
    Descifrado Decimado (MOD 256): a = C * key^{-1} (mod 256)
    - key debe ser coprima con 256 (impar), para que exista el inverso.
    """
    if not (0 <= key <= 255):
        raise ValueError("La llave debe estar en el rango 0..255.")
    inv = _modinv(key, MOD)  # ValueError si no hay inverso
    return _mul_mod_256_stream(data, inv)

