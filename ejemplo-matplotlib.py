"""
    Para el funcionamiento de este ejemplo
    se debe instalar la librería matplotlib
    pip install matplotlib
"""
# Se importa el módulo y se le asigan un alias
# plt

import matplotlib

matplotlib.use("TkAgg")  # Forzar el uso de un backend interactivo

import matplotlib.pyplot as plt

# Datos
x = ["A", "B", "C", "D"]
y = [5, 8, 3, 6]

# Crear gráfico de barras
plt.bar(x, y, color='blue')

# Etiquetas

plt.xlabel("Categorías")
plt.ylabel("Valores")
plt.title("Ejemplo de Gráfico de Barras")

# Mostrar el gráfico
# plt.show()

plt.show(block=True)  # Bloquea la ejecución hasta que cierres la ventana


"""

"""
