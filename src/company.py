#from core import Stand
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
    
    def add_stand(self, stand: "Stand") -> bool:
        if stand not in self.__stands:
            self.__stands.append(stand)
            stand.add_editorial(self)
            return True
        return False
    
    def get_stands(self) -> List["Stand"]:
        return self.__stands