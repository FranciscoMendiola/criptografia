# brute_force_cesar_png.py
import os, sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # .../practica1/cifrador
sys.path.insert(0, BASE_DIR)                            # para que 'src' sea visible

from src.buffer import leer_archivo, escribir_archivo
from src.codificador import cesar

PNG_MAGIC = b"\x89PNG\r\n\x1a\x0a"  # firma PNG

IN_PATH  = os.path.join(BASE_DIR, "file2.lol")          # tus .lol están aquí
OUT_DIR  = os.path.join(BASE_DIR, "file_decode")
os.makedirs(OUT_DIR, exist_ok=True)

data = leer_archivo(IN_PATH)

cands_minus = []   # asumiendo cifrado: b + shift  -> descifrar: b - shift
cands_plus  = []   # asumiendo cifrado: b - shift  -> descifrar: b + shift

for s in range(256):
    # Dirección 1: descifrar con (b - shift)
    probe_minus = cesar.decodificar_bytes(data[:16], s)
    if probe_minus.startswith(PNG_MAGIC):
        cands_minus.append(s)

    # Dirección 2: descifrar con (b + shift)
    probe_plus = cesar.codificar_bytes(data[:16], s)
    if probe_plus.startswith(PNG_MAGIC):
        cands_plus.append(s)

print("Candidatos (descifrar = b - shift):", cands_minus)
print("Candidatos (descifrar = b + shift):", cands_plus)

# Guarda archivos para los primeros candidatos de cada lista
if cands_minus:
    s = cands_minus[0]
    dec = cesar.decodificar_bytes(data, s)
    out_path = os.path.join(OUT_DIR, f"file2_decode_minus_{s}.png")
    escribir_archivo(out_path, dec)
    print("-> minus:", out_path, "OK" if dec.startswith(PNG_MAGIC) else "firma NO PNG")

if cands_plus:
    s = cands_plus[0]
    dec = cesar.codificar_bytes(data, s)
    out_path = os.path.join(OUT_DIR, f"file2_decode_plus_{s}.png")
    escribir_archivo(out_path, dec)
    print("-> plus :", out_path, "OK" if dec.startswith(PNG_MAGIC) else "firma NO PNG")
