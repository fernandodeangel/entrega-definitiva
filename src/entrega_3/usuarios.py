'''
Created on 16 dic 2024

@author: deang
'''
from datetime import date
from typing import Optional

class Usuario:
    def __init__(self, dni: str, nombre: str, apellidos: str, fecha_nacimiento: date):
        # Comprobaciones para asegurarse de que el DNI sigue el formato esperado y la fecha de nacimiento es válida.
        if not self.validar_dni(dni):
            raise ValueError(f"El DNI {dni} no tiene el formato correcto.")
        if fecha_nacimiento >= date.today():
            raise ValueError("La fecha de nacimiento debe ser anterior a la fecha actual.")
        
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
    
    @staticmethod
    def of(dni: str, nombre: str, apellidos: str, fecha_nacimiento: date) -> 'Usuario':
        """Método de factoría que crea e inicializa una nueva instancia de Usuario."""
        return Usuario(dni, nombre, apellidos, fecha_nacimiento)
    
    @staticmethod
    def parse(data: str) -> 'Usuario':
        """Método de factoría que convierte una cadena de texto en una instancia de Usuario."""
        # Suponemos que la cadena está en el formato "45718832U,Carlos,Lopez,1984-01-14"
        dni, nombre, apellidos, fecha_nacimiento_str = data.split(',')
        fecha_nacimiento = date.fromisoformat(fecha_nacimiento_str)
        return Usuario(dni, nombre, apellidos, fecha_nacimiento)
    
    @staticmethod
    def validar_dni(dni: str) -> bool:
        """Valida que el DNI siga el formato de 8 dígitos seguidos de una letra."""
        return len(dni) == 9 and dni[:8].isdigit() and dni[8].isalpha()
    
    def __repr__(self) -> str:
        """Representación en cadena del objeto."""
        return f"{self.dni} - {self.nombre}"