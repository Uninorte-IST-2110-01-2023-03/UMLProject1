from abc import ABC
#from book import Libro
#from company import Editorial
from typing import List

class Persona(ABC):

    def __init__(self, nombre: str, cedula: int) -> None:
        self._nombre = nombre
        self._cedula = cedula

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._cedula}, {self._nombre!r})'
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def get_cedula(self) -> int:
        return self._cedula
    

class Autor(Persona):

    def __init__(self, nombre: str, cedula: int) -> None:
        super().__init__(nombre, cedula)
        self.__libros: List["Libro"] = []

    def add_libro(self, libro: "Libro") -> bool:
        if libro not in self.__libros:
            self.__libros.append(libro)
            libro.add_autor(self)
            return True
        return False
    
    def get_libros(self) -> List["Libro"]:
        return self.__libros


class Gerente(Persona):

    def __init__(self, nombre: str, cedula: int) -> None:
        super().__init__(nombre, cedula)
        self.__editorial: "Editorial" = None

    def get_editorial(self) -> int:
        return self.__editorial

    def set_editorial(self, editorial: "Editorial") -> bool:
        self.__editorial = editorial
        return True


class Narrador(Persona):

    def __init__(self, nombre: str, cedula: int) -> None:
        super().__init__(nombre, cedula)
        self.__libros: List["Audiolibro"] = []

    def add_libro(self, libro: "Audiolibro") -> bool:
        if libro not in self.__libros:
            self.__libros.append(libro)
            return True
        return False
    
    def get_libros(self) -> List["Audiolibro"]:
        return self.__libros