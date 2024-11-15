num = int(input("Introduce un número entero positivo: "))
if num % 2 == 0:
    print(num, "es par")
else:
    print(num, "es impar")
numero = int(input("Introduce un número entero: "))
mult3 = []
for i in range(numero + 1):
    if i % 3 == 0:
        mult3.append(i)
print(mult3)