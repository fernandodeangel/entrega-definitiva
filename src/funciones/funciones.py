#ejercicio 1
from _ast import Or
def calcular_producto(n, k):
    resultado = 1
    for i in range(k + 1):
        resultado *= (n - i + 1)
    return resultado

print(calcular_producto(4, 2))

#ejercicio 2
def producto_geometrico(a1, r, k):
    exponente_r = (k - 1) * k // 2
    producto_a1 = a1 ** k
    producto_r = r ** exponente_r
    return producto_a1 * producto_r
print(producto_geometrico(3, 5, 2))

#ejercicio 3
import math

def combinatorio(n, k):
    if k > n:
        return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
print(combinatorio(4, 2))

#ejercicio 4
def combinatorio_2(n, k):
    """Función para calcular el número combinatorio binomial."""
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def S(n, k):

    factorial_k = math.factorial(k)
    suma = 0
    for i in range(k):
        
        signo = (-1) ** i

        combinatorio_binomial = combinatorio(k + 1, i + 1)
        
        termino_potencia = (k - i) ** n
        
        suma += signo * combinatorio_binomial * termino_potencia
    
    return suma / factorial_k
print(S(4, 2))

#ejercicio 5
def newton(f, df, x0, epsilon, max_iter=1000):
    x = x0
    for _ in range(max_iter):      
        fx = f(x)
        dfx = df(x)
        
        
        if abs(fx) <= epsilon:
            return x
        
        
        if dfx == 0:
            raise ValueError("La derivada es cero, no se puede continuar el método.")
        
        
        x = x - fx / dfx
    
   
    raise ValueError("El método de Newton no ha convergido después del número máximo de iteraciones.")
def f(x):
    return 2*x**2
def df(x):
    return 4*x
print(newton(f, df, 3, 0.001))

#ejercicio 6
def contar_palabra_en_fichero(nombre_fichero, separador, palabra):
    try:

        with open(nombre_fichero, 'r', encoding='utf-8') as fichero:
 
            contenido = fichero.read()
    
            palabras = contenido.split(separador)
            
            conteo = palabras.count(palabra)
            
            return conteo
    except FileNotFoundError:
        return f"El archivo {nombre_fichero} no fue encontrado."
    
nombre_fichero = "lin_quijote.txt"
separador = " "
palabra = "QUIJOTE" 
conteo = contar_palabra_en_fichero(nombre_fichero, separador, palabra)
print(f'La palabra "{palabra}" aparece {conteo} veces en el fichero "{nombre_fichero}".')


#ejercicio 7

def buscar_lineas_con_cadena(nombre_fichero, cadena):
    lineas_con_cadena = []
    
    try:
        with open(nombre_fichero, 'r', encoding='utf-8') as fichero:
         
            for linea in fichero:
                if cadena in linea:
                    lineas_con_cadena.append(linea.strip())  
        
        return lineas_con_cadena
    except FileNotFoundError:
        return f"El archivo {nombre_fichero} no fue encontrado."


nombre_fichero = "lin_quijote.txt"
cadena = "QUIJOTE"

resultados = buscar_lineas_con_cadena(nombre_fichero, cadena)
print(f'Las líneas que contienen "{cadena}" son:')
for linea in resultados:
    print(linea)
    
#ejercicio 8

def palabras_unicas(nombre_fichero):
    try:
        
        with open(nombre_fichero, 'r', encoding='utf-8') as fichero:
           
            contenido = fichero.read()
            
            palabras = contenido.split()

            palabras_unicas = set(palabras)
            
            return list(palabras_unicas)
    except FileNotFoundError:
        return f"El archivo {nombre_fichero} no fue encontrado."

nombre_fichero = "archivo_palabras.txt"
resultado = palabras_unicas(nombre_fichero)
print(f'Palabras únicas en el archivo "{nombre_fichero}":')
print(resultado)

#ejercicio 9

from typing import Optional

def longitud_promedio_lineas(file_path: str) -> Optional[float]:
    try:    
        suma_longitudes = 0
        conteo_lineas = 0

        with open(file_path, 'r', encoding='utf-8') as fichero:
            
            for linea in fichero:
               
                linea = linea.strip()
                
                suma_longitudes += len(linea)
                
                conteo_lineas += 1
        
        if conteo_lineas == 0:
            return None
        
        promedio = suma_longitudes / conteo_lineas
        return promedio
    
    except FileNotFoundError:
     
        return None

file_path = "palabras_random.csv"
promedio = longitud_promedio_lineas(file_path)
if promedio is not None:
    print(f'La longitud promedio de las líneas es: {promedio}')
else:
    print(f'El archivo "{file_path}" no fue encontrado o está vacío.')