print('#' * 120)
print('Programa que recebe 2 vetores A e B com 5 números inteiros do usuário e soma os valores em um vetor C')
print('#' * 120)

quantidade_elementos = int(input('Digite a quantidade de elementos no vetor.'))
vetor_a = [0 for x in range(quantidade_elementos)]
vetor_b = []
vetor_soma = [0 for x in range(quantidade_elementos)]

for i in range(quantidade_elementos):
    vetor_a[i] = int(input('Digite um valor para o vetor A:'))

for i in range(quantidade_elementos):
    vetor_b.append(int(input('Digite um valor para o vetor B:')))

for i in range(quantidade_elementos):
    vetor_soma[i] = vetor_a[i] - vetor_b[i]

print(f'A subtração dos {vetor_a} com o {vetor_b} é: {vetor_soma}.')
print('Fim do programa')