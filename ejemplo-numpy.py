"""
    Para el funcionamiento de este ejemplo
    se debe instalar la librería numpy
    pip install numpy
"""

# Se importa el módulo y se usa por intermedio de as
# un alias para ser usado en el script, en este caso np
import numpy as np

# Crear un array de 2x2
matriz = np.array([[1, 2], [3, 4]])

# Calcular la media de la matriz
media = np.mean(matriz)

print("Matriz:\n", matriz)
print("Media de la matriz:", media)

"""
La salida es:

Matriz:
 [[1 2]
 [3 4]]
Media de la matriz: 2.5

"""
