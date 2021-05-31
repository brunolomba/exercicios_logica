print('#' * 120)
print('Programa que cria 1 matriz e soma os elementos acima da diagonal.')
print('#' * 120)

# Validação da quantidade de linhas e colunas e criação da matriz
while True:
    matriz_quadrada = int(input('Digite a quantidade de linhas da primeira matriz.'))
    if matriz_quadrada > 0 and matriz_quadrada <= 10:
        matriz = [[0 for x in range(matriz_quadrada)] for x in range(matriz_quadrada)]
        break

# Adicionando os valores dos elementos das matrizes.
for linhas in range(matriz_quadrada):
    for elemento in range(matriz_quadrada):
        print(f'Digite o valor de elemento da primeira matriz {linhas} / {elemento}.')
        matriz[linhas][elemento] = int(input())

soma_acima_diagonal = 0
# Soma acima diagonal
for linhas in range(matriz_quadrada):
    for elemento in range(linhas + 1, matriz_quadrada):
        soma_acima_diagonal += matriz[linhas][elemento]

# Exibição da matriz organizada.
for linhas in matriz:
    for elemento in linhas:
        print(elemento, end=' ')

    else:
        print()

print(f'A soma acima da diagonal é {soma_acima_diagonal}.')
print('Fim do programa')