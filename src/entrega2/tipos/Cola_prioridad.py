'''
Created on 9 nov 2024

@author: deang
'''
from typing import List, TypeVar
from src.entrega2.tipos.Agregado_lineal import *


E = TypeVar('E')
P = TypeVar('P')

class ColaPrioridad(Agregado_lineal[E]):
    def __init__(self):
        super().__init__()
        self._priorities: List[P] = []  

    def priorities(self) -> List[P]:
        return self._priorities

    def add(self, element: E, priority: P):

        self._elements.append(element)
        self._priorities.append(priority)

        combined = sorted(zip(self._priorities, self._elements), key=lambda x: x[0], reverse=True)
        self._priorities, self._elements = zip(*combined) if combined else ([], [])
        self._priorities, self._elements = list(self._priorities), list(self._elements)

    def remove(self) -> E:

        if self.is_empty:
            raise IndexError("No se puede eliminar de una cola de prioridad vacía.")
        
        self._priorities.pop(0)
        return self._elements.pop(0)