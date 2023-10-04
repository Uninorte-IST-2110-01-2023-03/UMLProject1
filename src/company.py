from typing import List

class Editorial:

    def __init__(self, nit: str, nombre: str, direccion: str) -> None:
        self.__nit = nit
        self.__nombre = nombre
        self.__direccion = direccion
        self.__gerente: "Gerente" = None
        self.__libros: List["Libro"] = []
        self.__stands: List["Stand"] = []

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.__nit!r}, {self.__nombre!r})'