from book import LibroImpreso, LibroDigital, Audiolibro
from company import Editorial
from core import Megaferia
from person import Autor

def main() -> None:
    
    """
    libro_1 = LibroImpreso(
        titulo = 'Cien años de soledad',
        isbn = '848559455',
        genero = 'Novela',
        formato = 'Tapa dura',
        valor = 85000.0,
        paginas = 496,
        num_ejemplares = 5
    )

    libro_2 = LibroDigital(
        titulo = 'El aliento de los dioses',
        isbn = '5848485984',
        genero = 'Novela',
        formato = 'pdf',
        valor = 60000.0,
        has_hipervinculo = True
    )

    libro_3 = Audiolibro(
        titulo = 'Harry Potter',
        isbn = '1896455814',
        genero = 'Novela',
        formato = 'mp4',
        valor = 50000.0,
        duracion = 330
    )

    print(libro_1)
    print(libro_2)
    print(libro_3)
    """

    megaferia = Megaferia()
    editorial_1 = Editorial('865-894846613-1', 'Editorial 1', 'Calle 1 # 1 - 1')
    editorial_2 = Editorial('865-894846613-2', 'Editorial 2', 'Calle 2 # 2 - 2')

    megaferia.add_stand(50000.0)
    megaferia.add_stand(100000.0)
    megaferia.add_stand(75000.0)

    megaferia.add_editorial(editorial_1)
    megaferia.add_editorial(editorial_2)

    print(megaferia)

    editorial_1.add_stand(megaferia.get_stand(0))
    editorial_1.add_stand(megaferia.get_stand(1))

    editorial_2.add_stand(megaferia.get_stand(0))
    editorial_2.add_stand(megaferia.get_stand(2))

    print(editorial_1, editorial_1.get_stands())
    print(editorial_2, editorial_2.get_stands())

    print(megaferia.get_stand(0), megaferia.get_stand(0).get_editoriales())
    print(megaferia.get_stand(1), megaferia.get_stand(1).get_editoriales())
    print(megaferia.get_stand(2), megaferia.get_stand(2).get_editoriales())


if __name__ == '__main__':
    main()