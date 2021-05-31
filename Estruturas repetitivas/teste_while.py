x = int(input('Digite um número para somar'))
soma = 0

while x != 0:
    soma = soma + x
    x = int(input('Digite outro número para somar ou digite zero para finalizar a soma'))

print(f'A soma dos números digitados é: {soma}.')