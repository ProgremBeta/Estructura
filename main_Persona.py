# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:00:31 2024

@author: JUANCHO
"""
import pandas as pd
import time
from memory_profiler import profile
from insertionSort import insertionShort
from BusquedaBinaria import BusquedaBinaria
from BusquedaInterpolacion import BusquedaInterpolacion
from couting_sort import counting_sort

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

print("Iniciando procesos\n")

# Cargar el CSV usando pandas
df = pd.read_csv("/home/ignacio/Documentos/RepositoriosGit/Estructura/DataSets-20241108T024642Z-001/DataSets/01-personas100.csv")

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

@profile
def ordenar_personas():
    inicio = time.time()r

    personas_ordenadas = insertionShort(lista_personas)

    fin = time.time()
    tiempo_total = fin - inicio 

    print(f"Tiempo de ordenamiento: {tiempo_total:.6f} segundos")
    return personas_ordenadas

# Ordenar la lista y medir el tiempo y consumo de RAM
personas_ordenadas = ordenar_personas()

@profile
def buscar_persona(numero_documento, personas_ordenadas):
    inicio = time.time()

    persona_encontrada = BusquedaBinaria(numero_documento, personas_ordenadas)  # Cambia a BusquedaInterpolacion si lo deseas

    fin = time.time()
    tiempo_total = fin - inicio

    print(f"Tiempo de búsqueda: {tiempo_total:.6f} segundos")
    return persona_encontrada

# Buscar un número de documento específico
numero_documento_a_buscar = 18297912  # Número de documento a buscar
persona_encontrada = buscar_persona(numero_documento_a_buscar, personas_ordenadas)

if persona_encontrada:
    print("Persona encontrada:", persona_encontrada)
else:
    print("Persona no encontrada")
