print('#' * 120)
print('Soma dos números ímpares entra os valor x e y')
print('#' * 120)
i = 0
soma = 0
troca = 0
x = int(input('Digite um número "X"'))
y = int(input('Digite outro número "Y"'))

if x > y:
    troca = x
    x = y
    y = troca

for i in range(x + 1, y - 1):
    if i % 2 != 0:
        soma = soma + i

print(f'A soma dos números ímpares é {soma}')

print('Fim do programa')