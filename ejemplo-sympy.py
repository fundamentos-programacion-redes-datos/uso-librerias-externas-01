"""
    Para el funcionamiento de este ejemplo
    se debe instalar la librería sympy
    pip install symoy
"""
# Se importa el módulo y se le asigan un alias
# sp
import sympy as sp


# Definir la variable simbólica x
x = sp.Symbol('x')

# Definir la ecuación 2x + 3 = 7
ecuacion = 2*x + 3 - 7

# Resolver la ecuación
solucion = sp.solve(ecuacion, x)

print(f"La solución de la ecuación 2x + 3 = 7 es: x = {solucion[0]}")


"""

La solución de la ecuación 2x + 3 = 7 es: x = 2

"""
