'''
Created on 16 dic 2024

@author: deang
'''
from enum import Enum
from typing import Dict, Set, Any

class TipoGrafo(Enum):
    DIRIGIDO = "DIRIGIDO"
    NO_DIRIGIDO = "NO_DIRIGIDO"

class TipoRecorrido(Enum):
    FORWARD = "FORWARD"
    BACK = "BACK"

class E_grafo:
    def __init__(self, tipo_grafo: TipoGrafo = TipoGrafo.NO_DIRIGIDO, 
                 tipo_recorrido: TipoRecorrido = TipoRecorrido.BACK):
        self.__vertices: Set = set()
        self.__neighbors: Dict = {}  # vecinos
        self.__predecessors: Dict = {}  # predecesores
        self.__edges: Set = set()  # aristas
        self.__tipo_grafo = tipo_grafo
        self.__tipo_recorrido = tipo_recorrido
        
    def __add_neighbors(self, source: Any, target: Any) -> None:
        if source not in self.__neighbors:
            self.__neighbors[source] = set()
        self.__neighbors[source].add(target)
        
    def __add_predecessors(self, source: Any, target: Any) -> None:
        if target not in self.__predecessors:
            self.__predecessors[target] = set()
        self.__predecessors[target].add(source)
        
    def add_edge(self, source: Any, target: Any) -> bool:
        # Verificar condiciones
        if source not in self.__vertices or target not in self.__vertices:
            return False
        if source == target:  # No permitir bucles
            return False
        if (source, target) in self.__edges:  # No permitir aristas duplicadas
            return False
            
        # Agregar la arista
        self.__edges.add((source, target))
        self.__add_neighbors(source, target)
        
        if self.__tipo_grafo == TipoGrafo.DIRIGIDO:
            self.__add_predecessors(source, target)
        else:
            # Para grafos no dirigidos, agregar en ambas direcciones
            self.__edges.add((target, source))
            self.__add_neighbors(target, source)
            
        return True
        
    def edge_weight(self, source: Any, target: Any) -> float:
        if (source, target) in self.__edges:
            return 1.0  # Peso por defecto, se puede modificar según necesidades
        return float('inf')
        
    def add_vertex(self, vertex: Any) -> bool:
        if vertex in self.__vertices:
            return False
        self.__vertices.add(vertex)
        self.__neighbors[vertex] = set()
        self.__predecessors[vertex] = set()
        return True
        
    def edge_source(self, edge: tuple) -> Any:
        return edge[0]
        
    def edge_target(self, edge: tuple) -> Any:
        return edge[1]
        
    def vertex_set(self) -> Set:
        return self.__vertices.copy()
        
    def contains_edge(self, source: Any, target: Any) -> bool:
        return (source, target) in self.__edges
        
    def predecessors(self, vertex: Any) -> Set:
        if self.__tipo_grafo == TipoGrafo.DIRIGIDO:
            return self.__predecessors.get(vertex, set()).copy()
        return self.__neighbors.get(vertex, set()).copy()
        
    def sucessors(self, vertex: Any) -> Set:
        if self.__tipo_recorrido == TipoRecorrido.FORWARD:
            return self.__neighbors.get(vertex, set()).copy()
        return self.predecessors(vertex)
        
    def inverse_graph(self) -> 'E_grafo':
        if self.__tipo_grafo == TipoGrafo.NO_DIRIGIDO:
            return self
            
        inverse = E_grafo(self.__tipo_grafo, self.__tipo_recorrido)
        # Copiar vértices
        for vertex in self.__vertices:
            inverse.add_vertex(vertex)
            
        # Invertir aristas
        for source, target in self.__edges:
            inverse.add_edge(target, source)
            
        return inverse
