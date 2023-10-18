from abc import ABC
from company import Editorial
from person import Narrador
from typing import Any, List

class Libro(ABC):

    def __init__(self, titulo: str, isbn: str, genero: str, formato: str, valor: float, editorial: "Editorial", **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._titulo = titulo
        self._autores: List["Autor"] = []
        self._isbn = isbn
        self._genero = genero
        self._formato = formato
        self._valor = valor
        self._editorial: "Editorial" = editorial
        self._editorial.add_libro(self)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._titulo!r}, {self._isbn!r})'
    
    def add_autor(self, autor: "Autor") -> bool:
        if autor not in self._autores:
            self._autores.append(autor)
            return True
        return False

    def get_autores(self) -> List["Autor"]:
        return self._autores

    def get_editorial(self) -> "Editorial":
        return self._editorial


class LibroImpreso(Libro):

    def __init__(self, paginas: int, num_ejemplares: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.__paginas = paginas
        self.__num_ejemplares = num_ejemplares


class LibroDigital(Libro):

    def __init__(self, has_hipervinculo: bool, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.__has_hipervinculo = has_hipervinculo
        self.__hipervinculo: List[str] = []


class Audiolibro(Libro):

    def __init__(self, duracion: int, narrador: "Narrador", **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.__duracion = duracion
        self.__narrador: "Narrador" = narrador
        self.__narrador.add_libro(self)

    def get_narrador(self) -> "Narrador":
        return self.__narrador