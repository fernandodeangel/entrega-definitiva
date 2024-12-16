'''
Created on 16 dic 2024

@author: deang
'''
import unittest
from grafo import E_grafo, TipoGrafo, TipoRecorrido  # Asumiendo que el código está en grafo.py

class TestEGrafo(unittest.TestCase):
    
    def setUp(self):
        # Se ejecuta antes de cada test
        self.grafo_dirigido = E_grafo(TipoGrafo.DIRIGIDO)
        self.grafo_no_dirigido = E_grafo(TipoGrafo.NO_DIRIGIDO)
        
    def test_add_vertex(self):
        # Probar añadir vértices
        self.assertTrue(self.grafo_dirigido.add_vertex("A"))
        self.assertTrue(self.grafo_dirigido.add_vertex("B"))
        # Probar añadir vértice duplicado
        self.assertFalse(self.grafo_dirigido.add_vertex("A"))
        
    def test_add_edge(self):
        # Preparar grafo
        self.grafo_dirigido.add_vertex("A")
        self.grafo_dirigido.add_vertex("B")
        
        # Probar añadir arista válida
        self.assertTrue(self.grafo_dirigido.add_edge("A", "B"))
        
        # Probar añadir arista duplicada
        self.assertFalse(self.grafo_dirigido.add_edge("A", "B"))
        
        # Probar añadir bucle
        self.assertFalse(self.grafo_dirigido.add_edge("A", "A"))
        
        # Probar añadir arista con vértice inexistente
        self.assertFalse(self.grafo_dirigido.add_edge("A", "C"))
        
    def test_contains_edge(self):
        # Preparar grafo
        self.grafo_dirigido.add_vertex("A")
        self.grafo_dirigido.add_vertex("B")
        self.grafo_dirigido.add_edge("A", "B")
        
        # Verificar arista existente
        self.assertTrue(self.grafo_dirigido.contains_edge("A", "B"))
        # Verificar arista no existente
        self.assertFalse(self.grafo_dirigido.contains_edge("B", "A"))
        
    def test_grafo_no_dirigido(self):
        # Preparar grafo no dirigido
        self.grafo_no_dirigido.add_vertex("A")
        self.grafo_no_dirigido.add_vertex("B")
        self.grafo_no_dirigido.add_edge("A", "B")
        
        # Verificar que la arista existe en ambas direcciones
        self.assertTrue(self.grafo_no_dirigido.contains_edge("A", "B"))
        self.assertTrue(self.grafo_no_dirigido.contains_edge("B", "A"))
        
    def test_predecessors(self):
        # Preparar grafo dirigido
        self.grafo_dirigido.add_vertex("A")
        self.grafo_dirigido.add_vertex("B")
        self.grafo_dirigido.add_vertex("C")
        self.grafo_dirigido.add_edge("A", "B")
        self.grafo_dirigido.add_edge("C", "B")
        
        # Verificar predecesores
        predecesores_B = self.grafo_dirigido.predecessors("B")
        self.assertEqual(predecesores_B, {"A", "C"})
        
    def test_sucessors(self):
        # Preparar grafo
        self.grafo_dirigido.add_vertex("A")
        self.grafo_dirigido.add_vertex("B")
        self.grafo_dirigido.add_vertex("C")
        self.grafo_dirigido.add_edge("A", "B")
        self.grafo_dirigido.add_edge("A", "C")
        
        # Verificar sucesores con recorrido FORWARD
        grafo_forward = E_grafo(TipoGrafo.DIRIGIDO, TipoRecorrido.FORWARD)
        grafo_forward.add_vertex("A")
        grafo_forward.add_vertex("B")
        grafo_forward.add_vertex("C")
        grafo_forward.add_edge("A", "B")
        grafo_forward.add_edge("A", "C")
        
        sucesores = grafo_forward.sucessors("A")
        self.assertEqual(sucesores, {"B", "C"})
        
    def test_inverse_graph(self):
        # Preparar grafo original
        self.grafo_dirigido.add_vertex("A")
        self.grafo_dirigido.add_vertex("B")
        self.grafo_dirigido.add_edge("A", "B")
        
        # Obtener grafo inverso
        grafo_inverso = self.grafo_dirigido.inverse_graph()
        
        # Verificar que la arista está invertida
        self.assertTrue(grafo_inverso.contains_edge("B", "A"))
        self.assertFalse(grafo_inverso.contains_edge("A", "B"))
        
    def test_vertex_set(self):
        # Añadir vértices
        self.grafo_dirigido.add_vertex("A")
        self.grafo_dirigido.add_vertex("B")
        self.grafo_dirigido.add_vertex("C")
        
        # Verificar conjunto de vértices
        vertices = self.grafo_dirigido.vertex_set()
        self.assertEqual(vertices, {"A", "B", "C"})
        
if __name__ == '__main__':
    unittest.main()
