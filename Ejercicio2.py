nombre = input("Introduce tu nombre en formato Nombre Apellido \n")
primernom = nombre.split(" ")
print(primernom[0])
palabra = input("Introduce una palabra:")
vocal = input("Introduce una vocal:")
palabramayus = []
for i in palabra:
    if i == vocal:
        palabramayus.append(i.upper())
    else:
        palabramayus.append(i)
for j in range(len(palabramayus)):
    print(palabramayus[j], end="")