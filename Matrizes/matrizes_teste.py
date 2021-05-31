print('#' * 120)
print('Programa que pergunta quantos linhas e quantas colunas na matriz.')
print('#' * 120)

numero_linhas = int(input('Digite a quantidade de linhas.'))
numero_colunas = int(input('Digite a quantidade de colunas.'))
matriz = [[0 for x in range(numero_colunas)] for x in range(numero_linhas)]

for i in range(numero_linhas):
    for j in range(numero_colunas):
        print(f'Elemento {i} e {j} :')
        matriz[i][j] = int(input('Digite um elemento'))

# EXEMPLO DE COMO EXIBIR A LISTA (INTERNET)

for lista in matriz:
    for elemento in lista:
        print(elemento, end=' ')
    print()

print(matriz)
        
print('Fim do programa')