
    
#EJERCICIO 1

class Banco: 



    def __init__(self, empleados) : 



            # Lista de empleados, cada uno representado como un diccionario u objeto 



            self.empleados = empleados  







    def empleados_mas_viejos(self, n=3): 



        '''Devuelve una lista con los n empleados de mayor edad.'''



# Ordenar la lista de empleados por edad de mayor a menor 



        empleados_ordenados = sorted(self.empleados, key=lambda x: x['edad'], reverse=True)



# Devolver los n primeros empleados de la lista ordenada



        return empleados_ordenados[:n]
    
    
#EJERCICIO 2

class Centro:

    def __init__(self, profesores):

        """

        Inicializa un centro con una lista de profesores.

        Cada profesor debe tener un nombre y una lista de alumnos.

        """

        self.profesores = profesores



    def profesor_con_mas_alumnos(self):

        """

        Devuelve el profesor con más alumnos. Si hay empate, devuelve el primero.

        """

        if not self.profesores:

            return None  # Si no hay profesores, no hay resultado.



        # Usar max() para encontrar al profesor con la lista de alumnos más larga

        profesor_mas_alumnos = max(self.profesores, key=lambda p: len(p['alumnos']))



        return profesor_mas_alumnos
    
    
#EJERCICIO 3

from datetime import date

class Usuario:
    def __init__(self, dni, nombre, fecha_nacimiento):
        self.dni = dni
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

class Relacion:
    def __init__(self, dni1, dni2):
        self.dni1 = dni1
        self.dni2 = dni2

class Red_Social:
    def __init__(self):
        self.usuarios = []  # Lista de usuarios
        self.relaciones = []  # Lista de relaciones

    def agregar_usuario(self, usuario):
        """
        Agrega un usuario a la red social.
        """
        self.usuarios.append(usuario)

    def agregar_relacion(self, relacion):
        """
        Agrega una relación entre dos usuarios a la red social.
        """
        self.relaciones.append(relacion)

    # a. Método que indique cuántos usuarios hay
    def cantidad_usuarios(self):
        """
        Devuelve la cantidad total de usuarios en la red social.
        """
        return len(self.usuarios)

    # b. Método que devuelva un conjunto con los vecinos de un usuario dado su DNI
    def vecinos(self, dni):
        """
        Devuelve un conjunto con los vecinos (usuarios conectados) del usuario dado por su DNI.
        Lanza una excepción si el usuario no existe.
        """
        # Verificar si el usuario existe
        if not any(usuario.dni == dni for usuario in self.usuarios):
            raise ValueError(f"El usuario con DNI {dni} no existe en la red social.")

        # Buscar los vecinos en las relaciones
        vecinos = set()
        for relacion in self.relaciones:
            if relacion.dni1 == dni:
                vecinos.add(relacion.dni2)
            elif relacion.dni2 == dni:
                vecinos.add(relacion.dni1)
        return vecinos

    # c. Método que devuelva una lista con los grupos de usuarios conectados entre sí
    def grupos_conectados(self):
        """
        Devuelve una lista de conjuntos, donde cada conjunto representa un grupo
        de usuarios conectados entre sí.
        """
        # Crear un diccionario para guardar las conexiones
        def dfs(dni, visitados, grupo):
            """
            Realiza una búsqueda en profundidad (DFS) para encontrar usuarios conectados.
            """
            visitados.add(dni)
            grupo.add(dni)
            for vecino in self.vecinos(dni):
                if vecino not in visitados:
                    dfs(vecino, visitados, grupo)

        visitados = set()
        grupos = []

        for usuario in self.usuarios:
            if usuario.dni not in visitados:
                grupo = set()
                dfs(usuario.dni, visitados, grupo)
                grupos.append(grupo)

        return grupos

    # d. Método que devuelva una lista ordenada con los nombres de los usuarios por fecha de nacimiento
    def usuarios_por_fecha_nacimiento(self):
        """
        Devuelve una lista con los nombres de los usuarios ordenados por fecha de nacimiento.
        """
        return [usuario.nombre for usuario in sorted(self.usuarios, key=lambda x: x.fecha_nacimiento)]
    
#EJERCICIO 4

from dataclasses import dataclass, field
from typing import List

@dataclass
class Persona:
    nombre: str
    prestamos: List[float] = field(default_factory=list)
    
    def deuda_total(self) -> float:
        return sum(self.prestamos)

@dataclass
class Banco:
    personas: List[Persona] = field(default_factory=list)

    def persona_con_mayor_deuda(self) -> Persona:
        if not self.personas:
            raise ValueError("No hay personas registradas en el banco.")
        return max(self.personas, key=lambda persona: persona.deuda_total())

# Ejemplo de uso
persona1 = Persona(nombre="Juan", prestamos=[1000, 2000, 1500])
persona2 = Persona(nombre="María", prestamos=[5000, 3000])
persona3 = Persona(nombre="Luis", prestamos=[200, 100])

banco = Banco(personas=[persona1, persona2, persona3])

mayor_deudor = banco.persona_con_mayor_deuda()
print(f"La persona con mayor deuda es {mayor_deudor.nombre}, con una deuda total de {mayor_deudor.deuda_total()} euros.")


#EJERCICIO 5

from datetime import date, datetime
from typing import NamedTuple

class Direccion(NamedTuple):
    """
    Representa la dirección de la vivienda.
    """
    calle: str
    ciudad: str
    codigo_postal: str


class Vivienda:
    """
    Representa una vivienda inmutable con validaciones.
    """
    def __init__(self, fecha_compra, fecha_construccion, valor_catastral, dni_propietario, direccion, propietario):
        """
        Constructor privado. No debe llamarse directamente.
        Use el método `of` o `parse` para crear un objeto válido.
        """
        self._fecha_compra = fecha_compra
        self._fecha_construccion = fecha_construccion
        self._valor_catastral = valor_catastral
        self._dni_propietario = dni_propietario
        self._direccion = direccion
        self._propietario = propietario

    @property
    def fecha_compra(self):
        return self._fecha_compra

    @property
    def fecha_construccion(self):
        return self._fecha_construccion

    @property
    def valor_catastral(self):
        return self._valor_catastral

    @property
    def dni_propietario(self):
        return self._dni_propietario

    @property
    def direccion(self):
        return self._direccion

    @property
    def propietario(self):
        return self._propietario

    @staticmethod
    def of(fecha_compra, fecha_construccion, valor_catastral, dni_propietario, direccion, centro):
        """
        Crea un objeto Vivienda si se cumplen las restricciones o lanza una excepción si no es válido.
        """
        # Validar que el propietario es un profesor del centro
        propietario = next((prof for prof in centro.profesores if prof["dni"] == dni_propietario), None)
        if not propietario:
            raise ValueError(f"El DNI {dni_propietario} no corresponde a ningún profesor del centro.")

        # Validar que la fecha de compra es posterior a la fecha de construcción
        if fecha_compra <= fecha_construccion:
            raise ValueError("La fecha de compra debe ser posterior a la fecha de construcción.")

        # Validar que el valor catastral es positivo
        if valor_catastral <= 0:
            raise ValueError("El valor catastral debe ser un número positivo.")

        # Validar que el propietario es mayor de edad en la fecha de compra
        edad_compra = (fecha_compra - propietario["fecha_nacimiento"]).days // 365
        if edad_compra < 18:
            raise ValueError(f"El propietario debe ser mayor de edad en la fecha de compra (edad: {edad_compra}).")

        # Crear dirección a partir del tipo Direccion
        direccion_obj = Direccion(*direccion.split(","))
        
        # Devolver una instancia válida de Vivienda
        return Vivienda(fecha_compra, fecha_construccion, valor_catastral, dni_propietario, direccion_obj, propietario)

    @staticmethod
    def parse(cadena, centro):
        """
        Crea un objeto Vivienda a partir de una cadena en formato específico.
        Lanza una excepción si no es válido.
        """
        try:
            # Dividir la cadena por comas
            partes = cadena.split(",")
            if len(partes) != 6:
                raise ValueError("El formato de la cadena no es válido.")

            # Parsear las partes
            fecha_compra = datetime.strptime(partes[0], "%d-%m-%Y").date()
            fecha_construccion = datetime.strptime(partes[1], "%d-%m-%Y").date()
            valor_catastral = float(partes[2])
            dni_propietario = partes[3]
            direccion = ",".join(partes[4:])

            # Crear y validar el objeto Vivienda
            return Vivienda.of(fecha_compra, fecha_construccion, valor_catastral, dni_propietario, direccion, centro)
        except Exception as e:
            raise ValueError(f"Error al parsear la cadena: {e}")

    def __repr__(self):
        """
        Representación personalizada del objeto Vivienda.
        """
        # Calcular la edad del propietario en el momento actual
        edad_actual = (date.today() - self.propietario["fecha_nacimiento"]).days // 365
        return (f"El propietario de la vivienda en {self.direccion.calle},{self.direccion.ciudad},"
                f"{self.direccion.codigo_postal} es {self.propietario['nombre']} de {edad_actual} años de edad.")