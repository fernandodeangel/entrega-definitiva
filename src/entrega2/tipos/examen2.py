'''
Created on 21 nov 2024

@author: deang
'''
"""ejercicio 1"""

class Agregado_lineal:
    def __init__(self):
        self._elementos = []

    def add(self, elemento):

        self._elementos.append(elemento)

    def remove(self):
        if not self._elementos:
            raise IndexError("La estructura está vacía.")
        return self._elementos.pop(0)

    def __len__(self):
        return len(self._elementos)

class ColaConLimite(Agregado_lineal):
    def __init__(self, capacidad):

        super().__init__()
        self.capacidad = capacidad

    def add(self, elemento):

        if self.is_full():
            raise OverflowError()
        super().add(elemento)

    def is_full(self):

        return len(self) >= self.capacidad

    @classmethod
    def of(cls, capacidad):

        return cls(capacidad)

# Ejemplo de uso
def main():
    cola = ColaConLimite.of(3)
    cola.add("Tarea 1")
    cola.add("Tarea 2")
    cola.add("Tarea 3")

    try:
        cola.add("Tarea 4") 
    except OverflowError as e:
        print(e) 

    print(cola.remove()) 

if __name__ == "__main__":
    main()


"""ejercicio 2"""

from typing import Callable, TypeVar

E = TypeVar('E')  

class Agregado_lineal_mod:
 
    def __init__(self):
        self._elementos = []

    def add(self, elemento):
        self._elementos.append(elemento)

    def remove(self):
        if not self._elementos:
            raise IndexError("La estructura está vacía.")
        return self._elementos.pop(0)

    def __len__(self):
        return len(self._elementos)
    
    def __iter__(self):
        return iter(self._elementos)

    def contains(self, e: E) -> bool:

        return e in self._elementos

    def find(self, func: Callable[[E], bool]) -> E | None:

        for elemento in self._elementos:
            if func(elemento):
                return elemento
        return None

    def filter(self, func: Callable[[E], bool]) -> list[E]:

        return [elemento for elemento in self._elementos if func(elemento)]


"""ejercicio 3"""

import pytest

def test_cola_con_limite_basico():

    cola = ColaConLimite.of(3)
    
 
    cola.add("Tarea 1")
    cola.add("Tarea 2")
    cola.add("Tarea 3")
    

    assert cola.is_full() is True
    
    with pytest(OverflowError, match="La cola está llena."):
        cola.add("Tarea 4")
    

    assert cola.remove() == "Tarea 1"
    assert cola.remove() == "Tarea 2"
    assert cola.remove() == "Tarea 3"
    
    assert len(cola) == 0
    assert cola.is_full() is False

def test_cola_con_limite_vacia():
 
    cola = ColaConLimite.of(2)
    
 
    with pytest(IndexError, match="La estructura está vacía."):
        cola.remove()

    assert len(cola) == 0
    assert cola.is_full() is False

def test_cola_con_limite_una_sola_posicion():
    cola = ColaConLimite.of(1)
    
    cola.add("Tarea única")
    
    assert cola.is_full() is True
    assert len(cola) == 1
    
    assert cola.remove() == "Tarea única"
    
    assert len(cola) == 0
    assert cola.is_full() is False

def test_agregado_lineal_contains():
    agregado = Agregado_lineal()
    agregado.add(10)
    agregado.add(20)
    agregado.add(30)
    
    assert agregado.contains(10) is True
    assert agregado.contains(15) is False
    assert agregado.contains(30) is True

def test_agregado_lineal_find():
    agregado = Agregado_lineal()
    agregado.add(1)
    agregado.add(5)
    agregado.add(8)
    agregado.add(10)
    
    assert agregado.find(lambda x: x > 5) == 8  
    assert agregado.find(lambda x: x < 0) is None  

def test_agregado_lineal_filter():
  
    agregado = Agregado_lineal()
    agregado.add(3)
    agregado.add(4)
    agregado.add(6)
    agregado.add(7)
    
    pares = agregado.filter(lambda x: x % 2 == 0)
    assert pares == [4, 6]
    
    mayores_que_5 = agregado.filter(lambda x: x > 5)
    assert mayores_que_5 == [6, 7]
    
 
    vacio = agregado.filter(lambda x: x < 0)
    assert vacio == []

def test_combinaciones_agregado_y_cola():

    cola = ColaConLimite.of(5)
    
    cola.add(10)
    cola.add(15)
    cola.add(20)
    cola.add(25)
    
    assert cola.find(lambda x: x > 15) == 20  
    
    multiples_de_10 = cola.filter(lambda x: x % 10 == 0)
    assert multiples_de_10 == [10, 20]
    
    assert cola.remove() == 10
    assert cola.remove() == 15

def test_casos_extremos_y_errores():
    agregado = Agregado_lineal()
    
    assert agregado.find(lambda x: x > 0) is None
    assert agregado.filter(lambda x: x > 0) == []
    assert agregado.contains(1) is False
    
    cola = ColaConLimite.of(0)
    with pytest(OverflowError, match="La cola está llena."):
        cola.add("Cualquier elemento")
