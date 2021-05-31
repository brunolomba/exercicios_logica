print('#' * 120)
print('Digite as idades para saber a media ou um número negativo para finalizar')
print('#' * 120)

idade = int(input('Digite um número'))
soma = 0
i = 0
media = 0

while idade > 0:
   soma = soma + idade
   i = i + 1
   idade = int(input('Digite outra idade'))

if i == 0:
   print(f'Impossível calcular.')
else:
   media = soma / i
       
print(f'A media das idade é {media} anos.')
print('Programa foi finalizado!')