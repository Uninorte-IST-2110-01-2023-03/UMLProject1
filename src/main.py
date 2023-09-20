from book import LibroImpreso, LibroDigital, Audiolibro
from person import Autor

def main() -> None:
    nombre = input('Digite el nombre: ')
    cedula = int(input('Digite la cedula: '))

    autor = Autor(nombre, cedula)

    print(autor)


if __name__ == '__main__':
    main()