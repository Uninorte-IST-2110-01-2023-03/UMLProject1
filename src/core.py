from typing import List

class Megaferia:

    def __init__(self) -> None:
        self.__stands: List["Stand"] = []
        self.__editoriales: List["Editorial"] = []

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.__stands})'
    
    def add_stand(self, precio: float) -> bool:
        self.__stands.append(Stand(precio))
        return True
    

class Stand:

    __ID: int = 0

    def __init__(self, precio: float) -> None:
        self.__id = Stand.__ID
        self.__precio = precio
        self.__editoriales: List["Editorial"] = []

        Stand.__ID += 1

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.__id}, {self.__precio})'