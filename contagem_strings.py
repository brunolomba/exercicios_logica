print('#' * 120)
print('Programa que conta quantas letras tem até 1000')
print('#' * 120)

zero = 'zero'
vetor_1 = ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
vetor_2 = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quize', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
vetor_3 = ['trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
vetor_4 = ['cem', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seissentos', 'setecentos', 'oitocentos', 'novecentos']

soma = zero + ''
soma_total = 0
for i in vetor_1:
    soma += i * 10

for i in vetor_2:
    soma += i * 10

for i in vetor_3:
    soma += i * 10

for i in vetor_3:
    soma += i

soma_total += len(soma)

print(soma)
print(soma_total)