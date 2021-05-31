x = int(input('Digite um número'))
soma = 0
i = 0

while x != 0:
    if x % 2 != 0:
      x = x + 1

    soma = 5 * x + 20
    print(f'O soma dos 5 pares consecutivos é {soma}')
    x = int(input('Digite um número'))

print('Fim do programa')