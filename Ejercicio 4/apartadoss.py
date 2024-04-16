import math

# Definir la ecuación
def ecuacion(x):
    return x**3 - 2*x - 5

# Método de bisección
def biseccion(a, b, tolerancia):
    iteraciones = 0
    while (b - a) / 2 > tolerancia:
        c = (a + b) / 2
        if ecuacion(c) == 0:
            break
        if ecuacion(a) * ecuacion(c) < 0:
            b = c
        else:
            a = c
        iteraciones += 1
    return c, iteraciones

# Método de secante
def secante(x0, x1, tolerancia):
    iteraciones = 0
    while True:
        x2 = x1 - (ecuacion(x1) * (x1 - x0)) / (ecuacion(x1) - ecuacion(x0))
        if abs(x2 - x1) < tolerancia:
            break
        x0 = x1
        x1 = x2
        iteraciones += 1
    return x2, iteraciones

# Método de Newton-Raphson
def newton_raphson(x0, tolerancia):
    iteraciones = 0
    while True:
        x1 = x0 - ecuacion(x0) / derivada_ecuacion(x0)
        if abs(x1 - x0) < tolerancia:
            break
        x0 = x1
        iteraciones += 1
    return x1, iteraciones

# Derivada de la ecuación
def derivada_ecuacion(x):
    return 3*x**2 - 2

# Valores iniciales
a, b = 2, 3
x0, x1 = 2, 3
tolerancia = 1e-6

# Aplicar cada método
raiz_biseccion, iteraciones_biseccion = biseccion(a, b, tolerancia)
raiz_secante, iteraciones_secante = secante(x0, x1, tolerancia)
raiz_newton, iteraciones_newton = newton_raphson(x0, tolerancia)

# Imprimir resultados
print("Método de bisección:")
print("Raíz:", raiz_biseccion)
print("Iteraciones:", iteraciones_biseccion)

print("\nMétodo de secante:")
print("Raíz:", raiz_secante)
print("Iteraciones:", iteraciones_secante)

print("\nMétodo de Newton-Raphson:")
print("Raíz:", raiz_newton)
print("Iteraciones:", iteraciones_newton)
