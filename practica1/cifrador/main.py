import argparse
import os
from src.controlador import procesar_base64, procesar_cesar, procesar_decimado, procesar_afin

def main():
    tipos_de_cifrado = ['b64', 'af', 'ud', 'ce']

    parser = argparse.ArgumentParser(description="Cifrador/Descifrador de archivos")
    parser.add_argument("-t", "--type", choices=tipos_de_cifrado, required=True, help="Tipo de cifrado (b64, af, ud, ce)")
    parser.add_argument("-f", "--file", required=True, help="Ruta del archivo de entrada")
    parser.add_argument("-e", "--extension", required=True, help="Extensión para el archivo de salida (ej. txt, png)")
    parser.add_argument("-d", "--decode", action="store_true", help="Descifrar el archivo (si no se especifica, se codifica)")

    parser.add_argument("--shift", type=int, default=3, help="Desplazamiento para César (0..255; por defecto 3)")
    parser.add_argument("--key", type=int,
                        help="Llave multiplicativa para Decimado (0..255; debe ser IMPAR para poder descifrar)")

    args = parser.parse_args()
    
    params = {
        "type": args.type,
        "file": args.file,
        "extension": args.extension,
        "decode": args.decode,
        "shift": args.shift, 
        "key": args.key, 
    }

    if not os.path.exists(params["file"]):
        print(f"Error: El archivo '{params['file']}' no existe.")
        return

    try:
        if params["type"] == "b64":
            procesar_base64(params)
        elif params["type"] == "af":
            procesar_afin(params)
        elif params["type"] == "ud":
            if params["key"] is None:
                raise ValueError("Para decimado debes proporcionar --key (0..255, impar para descifrar).")
            procesar_decimado(params)
        elif params["type"] == "ce":
            procesar_cesar(params)   
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
