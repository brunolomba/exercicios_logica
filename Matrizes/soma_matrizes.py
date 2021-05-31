print('#' * 120)
print('Programa que cria 2 matrizes e soma os elementos delas.')
print('#' * 120)

# Validação da quantidade de linhas e colunas e criação da matriz
while True:
    numero_linhas = int(input('Digite a quantidade de linhas da primeira matriz.'))
    numero_colunas = int(input('Digite a quantidade de colunas da primeira matriz.'))
    if numero_linhas > 0 and numero_linhas <= 10 and numero_colunas > 0 and numero_colunas <= 10:
        matriz_a = [[0 for x in range(numero_colunas)] for x in range(numero_linhas)]
        matriz_b = [[0 for x in range(numero_colunas)] for x in range(numero_linhas)]
        matriz_soma_ab = [[0 for x in range(numero_colunas)] for x in range(numero_linhas)]
        break

# Adicionando os valores dos elementos das matrizes.
for linhas in range(numero_linhas):
    for elemento in range(numero_colunas):
        matriz_a[linhas][elemento] = int(input(f'Digite o valor de elemento da primeira matriz {linhas} / {elemento}.'))

for linhas in range(numero_linhas):
    for elemento in range(numero_colunas):
        matriz_b[linhas][elemento] = int(input(f'Digite o valor de elemento da segunda matriz {linhas} / {elemento}.'))

soma = 0
# Soma dos elementos das matrizes
for linha in range(numero_linhas):
    for elemento in range(numero_colunas):
        matriz_soma_ab[linha][elemento] = matriz_a[linha][elemento] + matriz_b[linha][elemento]

# Exibição da matriz organizada.
print('A soma das matrizes A e B é:')
for linhas in matriz_soma_ab:
    for elemento in linhas:
        print(elemento, end=' ')

    else:
        print()

print(matriz_a)
print(matriz_b)
print(matriz_soma_ab)

print('Fim do programa')