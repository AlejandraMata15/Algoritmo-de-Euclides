
def euclides_extendido(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        (d, x1, y1) = euclides_extendido(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (d, x, y)

# Ejemplo de uso
a = 117
b = 244
mcd, x, y = euclides_extendido(a, b)
print(f"MCD({a}, {b}) = {mcd}")
print(f"Coeficientes de Bezout: x = {x}, y = {y}")

