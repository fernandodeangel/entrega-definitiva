'''
Created on 9 nov 2024

@author: deang
'''


#A
from __future__ import annotations 

from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

E = TypeVar('E')

class AgregadoLineal(ABC, Generic[E]):
    def __init__(self):
        self._elements: List[E] = []

    def size(self) -> int:
        return len(self._elements)

    def is_empty(self) -> bool:
        return len(self._elements) == 0

    def elements(self) -> List[E]:
        return self._elements

    def add(self, element: E):
        pass

    def remove(self) -> E:
        pass
    


#B
from typing import Callable, Generic, List, TypeVar


E = TypeVar('E')
R = TypeVar('R')

class ListaOrdenada(AgregadoLineal[E]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order

    def of(self, order: Callable[[E], R]) -> 'ListaOrdenada[E]':
        
        return ListaOrdenada(order)

    def add(self, element: E):
        
        self._elements.append(element)
        self._elements.sort(key=self._order)

    def remove(self) -> E:
        
        if self.is_empty:
            raise IndexError("No se puede eliminar de una lista vacía.")
        return self._elements.pop(0)



#C
from typing import Callable, Generic, List, TypeVar

E = TypeVar('E')
R = TypeVar('R')

class ListaOrdenadaSinRepeticion(AgregadoLineal[E]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order

    def of(self, order: Callable[[E], R]) -> 'ListaOrdenadaSinRepeticion[E]':
        return ListaOrdenadaSinRepeticion(order)

    def add(self, element: E):
        if element not in self._elements:  
            self._elements.append(element)
            self._elements.sort(key=self._order)

    def remove(self) -> E:
        if self.is_empty:
            raise IndexError("No se puede eliminar de una lista vacía.")
        return self._elements.pop(0)


#D
from typing import Generic, TypeVar


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
    
    

#E
from typing import Generic, List, TypeVar, Tuple


E = TypeVar('E')
P = TypeVar('P')

class ColaPrioridad(AgregadoLineal[E]):
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
  

    
#F
from typing import Generic, TypeVar

E = TypeVar('E')

class Pila(AgregadoLineal[E]):
    def __init__(self):
        super().__init__()

    def of(self) -> 'Pila[E]':
 
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
