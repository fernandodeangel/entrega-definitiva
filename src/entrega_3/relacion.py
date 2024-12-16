'''
Created on 16 dic 2024

@author: deang
'''
class Relacion:
    # Contador interno para generar ID únicos
    xx_num = 0

    def __init__(self, interacciones: int, dias_activa: int):
        # Incrementar el contador y asignar un ID único
        Relacion.xx_num += 1
        self.id = Relacion.xx_num
        self.interacciones = interacciones
        self.dias_activa = dias_activa

    @staticmethod
    def of(interacciones: int, dias_activa: int) -> 'Relacion':
        """Método de factoría que crea e inicializa una nueva instancia de Relación."""
        return Relacion(interacciones, dias_activa)
    
    def __repr__(self) -> str:
        """Representación detallada de la relación como cadena."""
        return f"({self.id} - días activa: {self.dias_activa} - num interacciones {self.interacciones})"
    