print('#' * 120)
print('Escolha um número do fatorial que deseja saber')
print('#' * 120)

n = int(input('Digite o número do fatorial que vc deseja, no máximo até 15.'))
fatorial = 1

if n <= 15:
    for numero in range(1, n + 1):
        fatorial *= numero
else:
    print('Não é permitido fatorial maior do que 15')

print(fatorial)

print('Fim do programa')