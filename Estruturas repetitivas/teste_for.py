i = 0
soma = 0
x = 0
n = int(input('Digite a quantidade de números'))

for i in range(0, n):
    x = int(input('Digite um número para somar'))
    soma = soma + x
else: 
    print(f'A soma dos números digitados é {soma}.')