'''
Created on 9 nov 2024

@author: deang
'''
from typing import Generic, TypeVar

E = TypeVar('E')

class Pila(AgregadoLineal[E]):
    def __init__(self):
        super().__init__()

    def of() -> 'Pila[E]':
 
        return Pila()

    def push(self, element: E):
        self._elements.append(element)

    def pop(self) -> E:
        if self.is_empty:
            raise IndexError("No se puede eliminar de una pila vacía.")
        return self._elements.pop()

    def top(self) -> E:
        if self.is_empty:
            raise IndexError("No se puede obtener el elemento de una pila vacía.")
        return self._elements[-1]
