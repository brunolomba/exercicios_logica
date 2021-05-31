print('#' * 120)
print('Programa que adicionar números reais em um array, mostra os números e depois soma.')
print('#' * 120)

quantidade_pessoas = int(input('Digite a quantidade de pessoas que você deseja acrescentar no array.'))
array_pessoas = []
array_idades = []
array_alturas = []
soma_alturas = 0
contador_16anos = 0
porcentagem_16anos = 0

for i in range(quantidade_pessoas):
    array_pessoas.append(input('Digite o nome da pessoa.'))
    array_idades.append(int(input('Digite a idade da pessoa.')))
    array_alturas.append(float(input('Digite a altura da pessoa.')))

for i in range(quantidade_pessoas):
    print(f'Dados da {i + 1} pessoa')
    print(f'Nome: {array_pessoas[i]}')
    print(f'Idade: {array_idades[i]}')
    print(f'Altura: {array_alturas[i]}')

# Menores de 16 anos
for i in range(quantidade_pessoas):
    if array_idades[i] < 16:
        print('Menor de 16 anos')
        print(array_pessoas[i])

# Contador 16 anos
for i in array_idades:
    if i < 16:
        contador_16anos += 1

# Porcentagem 16 anos
porcentagem_16anos = contador_16anos * 100 / quantidade_pessoas

# Soma das alturas
for i in array_alturas:
    soma_alturas += i

# Media das alturas
media_alturas = soma_alturas / quantidade_pessoas

print(f'A media de alturas é de: {media_alturas}. E a porcetagem de menores de 16 anos é de: {porcentagem_16anos}')
print('Fim do programa')