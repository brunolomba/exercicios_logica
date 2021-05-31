print('#' * 120)
print('Programa que pergunta cria uma matriz e mostra o maior número de cada linha.')
print('#' * 120)

# Validação da quantidade de linhas e colunas e criação da matriz
while True:
    matriz_quadrada = int(input('Digite o número de linhas'))
    if matriz_quadrada > 0 and matriz_quadrada <= 10:
        matriz = [[0 for x in range(matriz_quadrada)] for x in range(matriz_quadrada)]
        break

# Inserção dos valores dos elementos.
for linhas in range(matriz_quadrada):
    for colunas in range(matriz_quadrada):
        matriz[linhas][colunas] = int(input(f'Digite o valor do elemento {linhas} / {colunas}.'))

maior = 0

for linhas in matriz:
    for elemento in linhas:
        if maior < elemento:
            maior = elemento
    else:
        print(maior)

print(matriz)

print('Fim do programa')