print('#' * 120)
print('Programa armazena nome e números em arrays e mostra o nome e a idade da pessoa mais velha.')
print('#' * 120)

numeros = int(input('Digite quantos númros que você deseja acrescentar no array.'))
array_nomes = []
array_idades = []
mais_velho = ''
maior_idade = 0

for i in range(numeros):
    print(f' Dados da {i} pessoa')
    array_nomes.append(input('Digite um nome'))
    array_idades.append(int(input('Digite a idade da pessoa')))

for i in range(numeros):
    if array_idades[i] > maior_idade:
        maior_idade = array_idades[i]
        mais_velho = array_nomes[i]

print(f'A pessoa mais velha é {mais_velho} com a idade de {maior_idade}.')

print('Fim do programa')