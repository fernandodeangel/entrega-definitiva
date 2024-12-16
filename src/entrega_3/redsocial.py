'''
Created on 16 dic 2024

@author: deang
'''
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Set
import csv

class TipoGrafo(Enum):
    DIRIGIDO = "DIRIGIDO"
    NO_DIRIGIDO = "NO_DIRIGIDO"

class TipoRecorrido(Enum):
    FORWARD = "FORWARD"
    BACK = "BACK"

class E_grafo:
    def __init__(self):
        self.__vertices: Set = set()
        self.__aristas: Dict = {}
        
    def agregar_vertice(self, v):
        self.__vertices.add(v)
        if v not in self.__aristas:
            self.__aristas[v] = set()
    
    def agregar_arista(self, v1, v2):
        if v1 in self.__vertices and v2 in self.__vertices:
            self.__aristas[v1].add(v2)
            self.__aristas[v2].add(v1)  # Para grafo no dirigido

@dataclass
class Usuario:
    id: str
    dias_activa: int
    interacciones: int
    
    def __str__(self):
        return f"({self.id} - días activa: {self.dias_activa} - num interacciones {self.interacciones})"

class Red_social(E_grafo):
    def __init__(self):
        super().__init__()
        self.__usuarios_dni: Dict[str, Usuario] = {}
    
    @classmethod
    def of(cls, tipo_grafo: TipoGrafo = TipoGrafo.NO_DIRIGIDO, 
           tipo_recorrido: TipoRecorrido = TipoRecorrido.BACK) -> 'Red_social':
        red = cls()
        return red
    
    @classmethod
    def parse(cls, archivo_usuarios: str, archivo_relaciones: str) -> 'Red_social':
        red = cls.of()
        
        # Leer usuarios
        with open(archivo_usuarios, 'r') as f:
            lector = csv.reader(f)
            next(lector)  # Saltar encabezados si existen
            for fila in lector:
                id, dias_activa, interacciones = fila
                usuario = Usuario(id, int(dias_activa), int(interacciones))
                red.__usuarios_dni[id] = usuario
                red.agregar_vertice(usuario)
        
        # Leer relaciones
        with open(archivo_relaciones, 'r') as f:
            lector = csv.reader(f)
            next(lector)  # Saltar encabezados si existen
            for fila in lector:
                id1, id2 = fila
                usuario1 = red.__usuarios_dni[id1]
                usuario2 = red.__usuarios_dni[id2]
                red.agregar_arista(usuario1, usuario2)
        
        return red
    
