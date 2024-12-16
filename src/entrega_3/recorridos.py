'''
Created on 16 dic 2024

@author: deang
'''
from typing import Dict, Tuple, Optional, List

V = str  # Tipo de vértices (puedes cambiarlo por cualquier tipo)
E = Tuple[V, V]  # Tipo de aristas (en este caso, una tupla de vértices)

class GrafoRecorrido:
    def __init__(self, grafo: Dict[V, List[V]]):
        self.tree: Dict[V, Tuple[Optional[V], float]] = {}
        self.path: List[V] = []
        self.grafo = grafo
    
    def path_to_origin(self, vertex: V) -> List[V]:
        path = []
        while vertex is not None:
            path.append(vertex)
            vertex = self.tree[vertex][0]  # El predecesor
        path.reverse()  # Para devolverlo desde el origen
        return path
    
    def origin(self, vertex: V) -> V:
        while self.tree[vertex][0] is not None:
            vertex = self.tree[vertex][0]
        return vertex
    
    def groups(self) -> Dict[V, set[V]]:
        groups = {}
        for vertex, (predecessor, _) in self.tree.items():
            if predecessor is not None:  # No incluir el nodo raíz
                if predecessor not in groups:
                    groups[predecessor] = set()
                groups[predecessor].add(vertex)
        return groups