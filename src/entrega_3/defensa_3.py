'''
Created on 19 dic 2024

@author: deang
'''


'''Ejercicio 1: Implementación del tipo Gen'''

from dataclasses import dataclass
from typing import Dict, Set, List, Tuple, TypeVar, Generic, Optional

@dataclass(frozen=True)
class Gen:
    nombre: str
    tipo: str
    num_mutaciones: int
    loc_cromosoma: int

    @staticmethod
    def of(nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: int) -> 'Gen':
        if num_mutaciones < 0:
            raise ValueError("El número de mutaciones debe ser mayor o igual a cero.")
        return Gen(nombre, tipo, num_mutaciones, loc_cromosoma)

    @staticmethod
    def parse(cadena: str) -> 'Gen':
        partes = cadena.strip().split(",")
        if len(partes) != 4:
            raise ValueError("La cadena no tiene el formato correcto: nombre,tipo,num_mutaciones,loc_cromosoma")
        nombre, tipo, num_mutaciones, loc_cromosoma = partes
        return Gen.of(nombre, tipo, int(num_mutaciones), int(loc_cromosoma))
    
# Ejemplo de comprobación del método parse en el main
if __name__ == "__main__":
    cadena = "BRCA1,tumor_supressor,5,17"
    gen = Gen.parse(cadena)
    print(gen)   
  
  
   
'''Ejercicio 2: Implementación del tipo RelacionGenAGen''' 
   
    
@dataclass(frozen=True)
class RelacionGenAGen:
    nombre_gen1: str
    nombre_gen2: str
    conexion: float

    @staticmethod
    def of(nombre_gen1: str, nombre_gen2: str, conexion: float) -> 'RelacionGenAGen':
        if not (-1 <= conexion <= 1):
            raise ValueError("La conexión debe ser un número real entre -1 y 1.")
        return RelacionGenAGen(nombre_gen1, nombre_gen2, conexion)

    @staticmethod
    def parse(cadena: str) -> 'RelacionGenAGen':
        partes = cadena.strip().split(",")
        if len(partes) != 3:
            raise ValueError("La cadena no tiene el formato correcto: nombre_gen1,nombre_gen2,conexion")
        nombre_gen1, nombre_gen2, conexion = partes
        return RelacionGenAGen.of(nombre_gen1, nombre_gen2, float(conexion))

    @property
    def coexpresados(self) -> bool:
        return self.conexion > 0.75

    @property
    def anticorrelados(self) -> bool:
        return self.conexion < -0.75


# Ejemplo de comprobación del método parse en el main
if __name__ == "__main__":
    cadena_relacion = "BRCA1,BRCA2,0.8"
    relacion = RelacionGenAGen.parse(cadena_relacion)
    print(relacion)
    print(f"Coexpresados: {relacion.coexpresados}")
    print(f"Anticorrelados: {relacion.anticorrelados}")
    
    
               
''' Ejercicio 3: Implementación del tipo RedGenica'''

#Implementación básica de Grafo

T = TypeVar('T')  # Tipo genérico para los vértices
E = TypeVar('E')  # Tipo genérico para las aristas

class Grafo(Generic[T, E]):
    def __init__(self, es_dirigido: bool = False) -> None:
        self.es_dirigido = es_dirigido
        self.vertices: List[T] = []
        self.aristas: List[Tuple[E, T, T]] = []

    def agregar_vertice(self, vertice: T) -> None:
        self.vertices.append(vertice)

    def agregar_arista(self, arista: E, origen: T, destino: T) -> None:
        self.aristas.append((arista, origen, destino))
        if not self.es_dirigido:
            self.aristas.append((arista, destino, origen))
            
class RedGenica(Grafo[Gen, RelacionGenAGen]):
    '''
    def __init__(self, es_dirigido: bool = False) -> None:
        super().__init__(es_dirigido)
        self.genes_por_nombre: Dict[str, Gen] = {}

    @staticmethod
    def of(es_dirigido: bool = False) -> 'RedGenica':
      
        return RedGenica(es_dirigido)

    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False) -> 'RedGenica':
      
        red = RedGenica(es_dirigido)

        # Primero, leer y agregar genes
        with open(f1, "r") as archivo_genes:
            for linea in archivo_genes:
                gen = Gen.parse(linea)
                red.genes_por_nombre[gen.nombre] = gen
                red.agregar_vertice(gen)

        # Segundo, leer y agregar relaciones entre genes
        with open(f2, "r") as archivo_relaciones:
            for linea in archivo_relaciones:
                relacion = RelacionGenAGen.parse(linea)
                gen1 = red.genes_por_nombre[relacion.nombre_gen1]
                gen2 = red.genes_por_nombre[relacion.nombre_gen2]
                red.agregar_arista(relacion, gen1, gen2)

        return red
    
#test    

with open('genes.txt', 'r') as f:
        genes = [linea.strip() for linea in f]
    
    # Leer conexiones
with open('red_genes.txt', 'r') as f:
        conexiones = [tuple(linea.strip().split(',')) for linea in f]
def test_red_genetica():
    print("\n=== TEST RED GENÉTICA ===\n")
  
    # 1. Crear red genética no dirigida
from enum import Enum
class TipoGrafo(Enum):
    DIRIGIDO = "DIRIGIDO"
    NO_DIRIGIDO = "NO_DIRIGIDO"
   
red = Grafo(TipoGrafo.NO_DIRIGIDO)
    
try:
        # Leer genes.txt
        with open('genes.txt', 'r') as f:
            for linea in f:
                gen = linea.strip()
                red.add_vertex(gen)
                
        # Leer red_genes.txt y crear conexiones
        with open('red_genes.txt', 'r') as f:
            for linea in f:
                gen1, gen2 = linea.strip().split(',')
                red.add_edge(gen1, gen2)
                
        # 2. Realizar recorrido en profundidad desde KRAS hasta PI3K3CA
        inicio = "KRAS"
        fin = "PI3K3CA"
        camino = encontrar_camino(red, inicio, fin)
        
        # 3. Crear y mostrar subgrafo
        print("Camino encontrado entre KRAS y PI3K3CA:")
        for i in range(len(camino)-1):
            print(f"{camino[i]} -> {camino[i+1]}")
            
except FileNotFoundError:
        print("Error: No se encontraron los archivos necesarios")
        return

def encontrar_camino(grafo: Grafo, inicio: str, fin: str, 
                    visitados: Optional[Set] = None, 
                    camino: Optional[List] = None) -> Optional[List[str]]:
    # Inicializar visitados y camino en la primera llamada
    if visitados is None:
        visitados = set()
    if camino is None:
        camino = []
    
    # Agregar el vértice actual al camino y a visitados
    visitados.add(inicio)
    camino.append(inicio)
    
    # Si llegamos al destino, retornar el camino
    if inicio == fin:
        return camino
    
    # Explorar vecinos no visitados
    for vecino in grafo.sucessors(inicio):
        if vecino not in visitados:
            nuevo_camino = encontrar_camino(grafo, vecino, fin, visitados, camino)
            if nuevo_camino:
                return nuevo_camino
    
    # Si no se encuentra camino, retroceder
    camino.pop()
    return None

if __name__ == '__main__':
    test_red_genetica()
   ''' 





class E_grafo:
    def __init__(self):
        self.vertices = set()
        self.aristas = {}

    def add_vertex(self, vertice):
        if vertice not in self.vertices:
            self.vertices.add(vertice)
            self.aristas[vertice] = set()
            return True
        return False

    def add_edge(self, origen, destino):
        if origen in self.vertices and destino in self.vertices:
            self.aristas[origen].add(destino)
            self.aristas[destino].add(origen)
            return True
        return False

    def get_neighbors(self, vertice):
        return self.aristas.get(vertice, set())

def buscar_camino(grafo: E_grafo, inicio: str, fin: str, 
                 visitados: Optional[set] = None, 
                 camino: Optional[List[str]] = None) -> Optional[List[str]]:
    # Inicializar visitados y camino en la primera llamada
    if visitados is None:
        visitados = set()
    if camino is None:
        camino = []
    
    # Agregar el vértice actual
    visitados.add(inicio)
    camino.append(inicio)
    
    # Si llegamos al destino
    if inicio == fin:
        return camino
    
    # Explorar vecinos
    for vecino in grafo.get_neighbors(inicio):
        if vecino not in visitados:
            resultado = buscar_camino(grafo, vecino, fin, visitados, camino)
            if resultado:
                return resultado
    
    # Retroceder si no hay camino
    camino.pop()
    return None

def main():
    print("\n=== TEST RED GENÉTICA ===\n")
    
    # Crear grafo
    red = E_grafo()
    
    # Agregar vértices
    genes = ["KRAS", "TP53", "PI3K3CA"]
    for gen in genes:
        red.add_vertex(gen)
    
    # Agregar aristas
    red.add_edge("KRAS", "TP53")
    red.add_edge("TP53", "PI3K3CA")
    
    # Buscar camino
    camino = buscar_camino(red, "KRAS", "PI3K3CA")
    
    # Mostrar resultado
    if camino:
        print("Camino encontrado:")
        for i in range(len(camino)-1):
            print(f"{camino[i]} -> {camino[i+1]}")
    else:
        print("No se encontró camino")

    # Visualización opcional
    try:
        import networkx as nx
        import matplotlib.pyplot as plt
        
        G = nx.Graph()
        G.add_edge("KRAS", "TP53")
        G.add_edge("TP53", "PI3K3CA")
        
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', 
                node_size=1500, font_size=10, font_weight='bold')
        plt.savefig('red_genetica.png')
        plt.close()
        print("\nSe ha generado la visualización en 'red_genetica.png'")
    except ImportError:
        print("\nPara visualizar, instala: pip install networkx matplotlib")

if __name__ == '__main__':
    main()