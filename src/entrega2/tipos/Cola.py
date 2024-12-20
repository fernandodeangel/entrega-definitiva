'''
Created on 9 nov 2024

@author: deang
'''
from typing import Generic, TypeVar
from src.entrega2.tipos.Agregado_lineal import *


E = TypeVar('E')

class Cola(AgregadoLineal[E]):
    def __init__(self):
        super().__init__()

    def of(self) -> 'Cola[E]':
        return Cola()

    def add(self, element: E):
        self._elements.append(element)

    def remove(self) -> E:
        if self.is_empty:
            raise IndexError("No se puede eliminar de una cola vacía.")
        return self._elements.pop(0)
