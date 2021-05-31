print('#' * 120)
print('vetores teste.')
print('#' * 120)

n = int(input('Digite a quantidade de elementos que você deseja acrescentar no array.'))

if n > 10 or n < 0:
    print('Esse número não é permitido')

array = [float(input('Digite um valor para adicionar no array')) for i in range(n)]
# for i in range(n):
#     valor = float(input('Digite um valor para adicionar no array'))
#     array.append(valor)

for i in range(n):
    print(array[i])

print(f'Números ordenados de forma crescente {sorted(array)}.')
print(f'Números ordenados de forma decrescente {sorted(array, reverse=True)}.')
print(f'Números ordenados de forma digitada {array}.')

# EXEMPLO DE QUANDO OS VALORES ESTÃO EM FORMATO DE STRINGS / ORDENANDO VALORES SEM ALTERAR O TIPO STRING

# for i in range(n):
#     valor = input('Digite um valor para adicionar no array')
#     array.append(valor)

# print(f'Números ordenados de forma crescente {sorted(array, key=int)}.')
# print(f'Números ordenados de forma crescente {sorted(array, key=int, reverse=True)}.')
# print(f'Números ordenados de forma digitada {array}.')

print('Fim do programa')