import argparse
import os
from src.controlador import procesar_base64

def main():
    tipos_de_cifrado = ['b64', 'af', 'ud', 'ce']

    parser = argparse.ArgumentParser(description="Cifrador/Descifrador de archivos")

    parser.add_argument("-t", "--type", choices=tipos_de_cifrado, required=True, help="Tipo de cifrado (b64, af, ud, ce)")
    parser.add_argument("-f", "--file", required=True, help="Ruta del archivo de entrada")
    parser.add_argument("-e", "--extension", required=True, help="Extensión para el archivo de salida (ej. txt)")
    parser.add_argument("-d", "--decode", action="store_true", help="Descifrar el archivo (si no se especifica, se codifica)")

    args = parser.parse_args()

    # Crear diccionario con parámetros
    params = {
        "type": args.type,
        "file": args.file,
        "extension": args.extension,
        "decode": args.decode
    }

    # Validar archivo de entrada
    if not os.path.exists(params["file"]):
        print(f"Error: El archivo '{params['file']}' no existe.")
        return

    # Seleccionar codificador según tipo
    try:
        if params["type"] == "b64":
            procesar_base64(params)
        elif params["type"] == "af":
            raise NotImplementedError("Error: El cifrado Afín (af) no está implementado.")
        elif params["type"] == "ud":
            raise NotImplementedError("Error: El cifrado Decimado (ud) no está implementado.")
        elif params["type"] == "ce":
            raise NotImplementedError("Error: El cifrado César (ce) no está implementado.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
