import os


def main():
    lenguaje_favorito = os.getenv("LANGUAGE")
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, mundo desde {lenguaje} soy {nombre}!")


if __name__ == "__main__":
    main()