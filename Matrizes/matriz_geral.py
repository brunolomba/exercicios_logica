print('#' * 120)
print('Programa que cria 1 matriz e soma os elementos acima da diagonal.')
print('#' * 120)

# Validação da quantidade de linhas e colunas e criação da matriz
while True:
    matriz_quadrada = int(input('Qual a ordem da matriz?'))
    if matriz_quadrada > 0 and matriz_quadrada <= 10:
        matriz = [[0 for x in range(matriz_quadrada)] for x in range(matriz_quadrada)]
        break

# Adicionando os valores dos elementos das matrizes.
for linhas in range(matriz_quadrada):
    for elemento in range(matriz_quadrada):
        matriz[linhas][elemento] = int(input(f'Elemento {linhas} / {elemento}:'))

# calcular e imprimar todos elementos positivos da matriz.
soma_positivo = 0
for linhas in matriz:
    for elemento in linhas:
        if elemento > 0:
            soma_positivo += elemento
print(f'A soma dos positivos é {soma_positivo}.')

# Escolhendo uma linha e imprimindo apenas essa linhas
linha_escolhida = 0
linha_escolhida_print = []

while True:
    linha_escolhida = int(input('Digite a linha que vc deseja imprimir.'))
    if linha_escolhida > 0 and linha_escolhida <= matriz_quadrada:
        linha_escolhida -= 1
        break
    
for colunas in matriz:
    linha_escolhida_print = matriz[linha_escolhida]
print(f'A linhas escolhida é {linha_escolhida + 1} com o resultado de {linha_escolhida_print}.')

# Escolhendo uma coluna e imprimindo apenas essa coluna.
coluna_escolhida = 0
coluna_escolhida_print = []

while True:
    coluna_escolhida = int(input('Digite a coluna que vc deseja imprimir.'))
    if coluna_escolhida > 0 and coluna_escolhida <= matriz_quadrada:
        coluna_escolhida -= 1
        break
for linhas in range(matriz_quadrada):
    for colunas in range(matriz_quadrada):
        if colunas == (coluna_escolhida):
            coluna_escolhida_print.append(matriz[linhas][coluna_escolhida])

print(f'A coluna escolhida é {coluna_escolhida + 1} com o resultado de {coluna_escolhida_print}.')

# Diagonal principal
diagonal_principal_print = []

for linhas in range(matriz_quadrada):
    for elemento in range(matriz_quadrada):
        if linhas == elemento:
            diagonal_principal_print.append(matriz[linhas][elemento])
print(f'A diagonal principal é: {diagonal_principal_print}.')

# Matriz com negativos elevados ao quadrado.
for linhas in range(matriz_quadrada):
    for elemento in range(matriz_quadrada):
        if matriz[linhas][elemento] < 0:
            matriz[linhas][elemento] = (matriz[linhas][elemento]) ** 2

# Exibição da matriz organizada matriz com negativos ao quadrado.
for linhas in matriz:
    for elemento in linhas:
        print(elemento, end=' ')
    print()

print('Fim do programa')