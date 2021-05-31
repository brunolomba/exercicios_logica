x = int(input('Digite um número'))
y = int(input('Digite outro número'))

if x % y == 0 or y % x == 0:
    print('São multiplos')
else:
    print('Não são multiplos')