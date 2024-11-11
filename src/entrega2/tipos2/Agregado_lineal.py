'''
Created on 9 nov 2024

@author: deang
'''
from __future__ import annotations 

from abc import ABC
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