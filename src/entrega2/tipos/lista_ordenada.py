'''
Created on 9 nov 2024

@author: deang
'''
from typing import Callable, Generic, List, TypeVar


E = TypeVar('E')
R = TypeVar('R')

class ListaOrdenada(AgregadoLineal[E]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order
        
    @staticmethod
    def of(order: Callable[[E], R]) -> 'ListaOrdenada[E]':
        
        return ListaOrdenada(order)

    def add(self, element: E):
        
        self._elements.append(element)
        self._elements.sort(key=self._order)

    def remove(self) -> E:
        
        if self.is_empty:
            raise IndexError("No se puede eliminar de una lista vacía.")
        return self._elements.pop(0)