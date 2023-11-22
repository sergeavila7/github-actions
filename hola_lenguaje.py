import os


def main():
    lenguaje_favorito = os.getenv("LANGUAGE")
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, mundo desde {lenguaje_favorito} soy {nombre}!")


if __name__ == "__main__":
    main()