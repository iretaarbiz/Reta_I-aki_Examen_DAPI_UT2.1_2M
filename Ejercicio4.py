paises = []
for i in range(2):
    if i == 0:
        paises.append(input("Introduce el primer pais que te gustaría visitar: "))
    if i == 1:
        paises.append(input("Introduce el segundo pais que te gustaría visitar: "))
    else:
        paises.append(input("Introduce el tercer pais que te gustaría visitar: "))
for j in range(len(paises)):
    print("Me gustaría visitar",paises[j])
listaenteros = []
nums = input("Ingresa una lista de números separados por comas: \n")
listanums = list(nums.split(","))
for k in range(len(listanums)):
    listaenteros.append(int(listanums[k]))
print("El número mas alto es:", max(listaenteros))
print("El número mas bajo es:", min(listaenteros))