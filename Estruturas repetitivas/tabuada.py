i = 0
multiplicação = 0
n = int(input('Digite um número para ver a sua tabuada'))

for i in range(1, 11):
    multiplicação = n * i
    print(f'{n} x {i} = {multiplicação}.')
else:
    print('Fim do programa')