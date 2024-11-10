# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:00:31 2024

@author: JUANCHO
"""
import pandas as pd
import time
import psutil
from insertionSort import insertionShort
from BusquedaBinaria import BusquedaBinaria
#from TimSort_Personas import TimSort

# Definimos la clase Persona con los atributos correspondientes
class Persona:
    def __init__(self, numero_documento, nombre, apellido, fecha_nacimiento, edad, genero, prioridad):
        self.numero_documento = int(numero_documento)
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = edad
        self.genero = genero
        self.prioridad = prioridad

    def __repr__(self):
        return f"Persona({self.numero_documento}, {self.nombre}, {self.apellido}, {self.fecha_nacimiento}, {self.edad}, {self.genero}, {self.prioridad})"


# Función para medir el tiempo y consumo de RAM
def medir_tiempo_y_ram(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        start_ram = psutil.Process().memory_full_info().rss / 1024 / 1024  # Consumo de RAM en MB

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        end_ram = psutil.Process().memory_full_info().rss / 1024 / 1024  # Consumo de RAM en MB

        elapsed_time = end_time - start_time  # Tiempo en segundos
        ram_usage = max(end_ram - start_ram, 0)  # Evitar valores negativos de RAM

        return result, elapsed_time, ram_usage

    return wrapper

# Cargar el CSV usando pandas
df = pd.read_csv("C:/Users/User/Downloads/Proyecto de Estructura/DataSets-20241108T024642Z-001/DataSets/04-personas10k.csv")  # Reemplaza "ruta_del_archivo.csv" con la ruta de tu archivo CSV

# Convertir cada fila del DataFrame en un objeto Persona
lista_personas = [
    Persona(
        row["Número de Documento"],
        row["Nombre"],
        row["Apellido"],
        row["Fecha de Nacimiento"],
        row["Edad"],
        row["Género"],
        row["Prioridad"]
    )
    for index, row in df.iterrows()
]

# Verificación de la lista
#print("Lista de personas:", lista_personas[501].prioridad)
#print("Número total de personas:", len(lista_personas))

# Ordenar la lista de objetos Persona por número de documento
#@medir_tiempo_y_ram
# def ordenar_personas():
#     tim_sort = TimSort(lista_personas)
#     return tim_sort.tim_sort()

@medir_tiempo_y_ram
def ordenar_personas():
    lista_ordenada = insertionShort(lista_personas)
    return lista_ordenada

personas_ordenadas, tiempo_ordenacion, ram_ordenacion = ordenar_personas()
print(f"Tiempo de ordenamiento: {tiempo_ordenacion:.6f} segundos")
print(f"Consumo de RAM durante la ordenación: {ram_ordenacion:.6f} MB")

#personas_ordenadas = ordenar_personas()

# Buscar un número de documento específico
@medir_tiempo_y_ram
def buscar_persona(numero_documento, personas_ordenadas):
    #binary_search = BusquedaBinaria(personas_ordenadas)
    return BusquedaBinaria(numero_documento, personas_ordenadas)

numero_documento_a_buscar = 65889543  # Asegúrate de que el número de documento sea un entero
persona_encontrada, tiempo_busqueda, ram_busqueda = buscar_persona(numero_documento_a_buscar, personas_ordenadas)

print(f"Tiempo de búsqueda: {tiempo_busqueda:.6f} segundos")
print(f"Consumo de RAM durante la búsqueda: {ram_busqueda:.6f} MB")

if persona_encontrada:
    print("Persona encontrada:", persona_encontrada)
else:
    print("Persona no encontrada")
    
# Imprimir los resultados ordenados
#for persona in personas_ordenadas:
#    print(persona)
