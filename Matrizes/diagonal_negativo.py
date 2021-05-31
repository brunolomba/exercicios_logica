print('#' * 120)
print('Programa que pergunta cria uma matriz quadrada.')
print('#' * 120)

while True:
    matriz_quadrada = int(input('Digite a quantidade de linhas e colunas (máximo 10).'))
    if matriz_quadrada > 0 and matriz_quadrada <= 10:
        break

matriz = [[0 for x in range(matriz_quadrada)] for x in range(matriz_quadrada)]
diagonal = []
negativos = []
contador_negativos = 0

for i in range(matriz_quadrada):
    for j in range(matriz_quadrada):
        matriz[i][j] = int(input(f'Digite um número para a posição [{i}, {j}].'))

# EXEMPLO DE COMO EXIBIR A LISTA (INTERNET)
for lista in matriz:
    for elemento in lista:
        print(elemento, end=' ')
    print()

# print_comprehension = [print(elemento, end=' ') for lista in matriz for elemento in lista]

# diagonal_comprehension = [
#     diagonal.append(matriz[linha][coluna]) for coluna in range(matriz_quadrada) for linha in range(matriz_quadrada) if linha == coluna
# ]

# Diagonal principal.
# for linha in range(matriz_quadrada):
#     for coluna in range(matriz_quadrada):
#         if linha == coluna:
#             diagonal.append(matriz[linha][coluna])

# for i in range(matriz_quadrada):
#     diagonal.append(matriz[i][i])

for lista in matriz:
    for elemento in lista:
        if elemento < 0:
            negativos.append(elemento)
            contador_negativos += 1

print(f'A diagonal da matriz é {diagonal}. e a quantidade de negativos são {contador_negativos} : {negativos}')
print(diagonal_comprehension)
print(matriz)
        
print('Fim do programa')