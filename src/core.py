from company import Editorial
from typing import List, Optional

class Megaferia:

    def __init__(self) -> None:
        self.__stands: List["Stand"] = []
        self.__editoriales: List["Editorial"] = []

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(Stands({len(self.__stands)}), Editoriales({len(self.__editoriales)}))'
    
    def add_stand(self, precio: float) -> bool:
        self.__stands.append(Stand(precio))
        return True
    
    def add_editorial(self, editorial: "Editorial") -> bool:
        if editorial not in self.__editoriales:
            self.__editoriales.append(editorial)
            return True
        return False
    
    def get_stand(self, id_stand: int) -> Optional["Stand"]:
        for stand in self.__stands:
            if stand.get_id() == id_stand:
                return stand
        return None
    

class Stand:

    __ID: int = 0

    def __init__(self, precio: float) -> None:
        self.__id = Stand.__ID
        self.__precio = precio
        self.__editoriales: List["Editorial"] = []

        Stand.__ID += 1

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.__id}, {self.__precio})'
    
    def get_id(self) -> int:
        return self.__id
    
    def add_editorial(self, editorial: "Editorial") -> bool:
        self.__editoriales.append(editorial)
        return True
    
    def get_editoriales(self) -> List["Editorial"]:
        return self.__editoriales