print('#' * 120)
print('Escolha uma quantidade de números pra digitar e descobrir quantos estão dentro do intervalo [10, 20]')
print('#' * 120)

n = int(input('Digite quantos números você deseja digitar"'))
dentro = 0
fora = 0

for numero in range(n):
    x = int(input('Digite um número'))
    if x >= 10 and x <= 20:
        dentro += 1
    else:
        fora += 1
else:
    print(f'Você digitou {n} números e dentre eles, {dentro} estão dentro do intervalo e {fora} estão fora.')

print('Fim do programa')