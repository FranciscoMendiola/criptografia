 # src/codificador/decimado.py

from typing import Iterable, Tuple

MOD = 256

"""Algoritmo de Euclides extendido. Retorna (gcd, x, y) tal que a*x + b*y = gcd."""
def _egcd(a: int, b: int) -> Tuple[int, int, int]:
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = _egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

"""Inverso modular de a modulo m. Lanza ValueError si no existe."""
def _modinv(a: int, m: int = MOD) -> int:
    a = a % m
    g, x, _ = _egcd(a, m)
    if g != 1:
        raise ValueError(f"No existe inverso modular para {a} (mod {m}); gcd={g}. "
                         "Asegúrate de que la llave sea impar y coprima con 256.")
    return x % m

"""Multiplica cada byte por k mod 256."""
def _mul_mod_256_stream(data: Iterable[int], k: int) -> bytes:
    k = k % MOD
    return bytes(((b * k) % MOD for b in data))

""" 
Decimado binario (MOD 256) - C = a * key (mod 256)
- data: bytes de entrada
- key: llave multiplicativa (0..255). Para descifrar luego, key debe ser coprima con 256 (impar).
"""
def codificar_bytes(data: bytes, key: int) -> bytes:
    if not (0 <= key <= 255):
        raise ValueError("La llave debe estar en el rango 0..255.")
    return _mul_mod_256_stream(data, key)

"""
Descifrado Decimado (MOD 256): a = C * key^{-1} (mod 256)
- key debe ser coprima con 256 (impar), para que exista el inverso.
"""
def decodificar_bytes(data: bytes, key: int) -> bytes:
    if not (0 <= key <= 255):
        raise ValueError("La llave debe estar en el rango 0..255.")
    inv = _modinv(key, MOD)  # ValueError si no hay inverso
    return _mul_mod_256_stream(data, inv)

