def area_cuadrado(lado):
    "Esta función recibe la longitud de un lado del cuadrado y devuelve su área"
    area = lado ** 2
    return area
longitud = float(input("Introduce el lado del cuadrado: \n"))
print("El área del cuadrado es de", area_cuadrado(longitud),"centímetros cuadrados")
def mayor_de_tres(a, b ,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
x = int(input("Introduce el primer número: "))
y = int(input("Introduce el segundo número: "))
z = int(input("Introduce el tercer número: "))
print("El mayor número entre esos tres es", mayor_de_tres(x, y, z))
