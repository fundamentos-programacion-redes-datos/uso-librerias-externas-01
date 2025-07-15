"""
    Para el funcionamiento de este ejemplo
    se debe instalar la librería pandas
    pip install pandas
"""
# Se importa el módulo y se le asigan un alias
# pd
import pandas as pd

# Crear un DataFrame con datos de estudiantes
# Se crea un diccionario de datos.
data = {
    "Nombre": ["Ana", "Juan", "Pedro"],
    "Edad": [20, 22, 21],
    "Calificacion": [90, 85, 88]
}

# Se crea la estructura DataFrame con el valor de data
df = pd.DataFrame(data)

# Mostrar el DataFrame en pantalla
print(df)

# Calcular la media de calificaciones, haciendo uso de la 
# función mean a la columna de calificaciones
#
print(f'Media de calificaciones: {df["Calificacion"].mean():.2f}')

"""
Salida:

  Nombre  Edad  Calificacion
0    Ana    20            90
1   Juan    22            85
2  Pedro    21            88
Media de calificaciones: 87.67

"""
