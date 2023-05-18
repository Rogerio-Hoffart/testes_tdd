lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range((len(lista) - 1) // 2):
    lista[i], lista[-1 -i] = lista[-1 -i], lista[i]

print(lista)

lista.sort(reverse=True)
print(lista)