unidade = input('Digite em qual escala vc quer transformar: "c" para Celsius ou "F" para Farenheit')

if unidade == 'f':
    f = int(input('Digite a temperatura'))
    c = 5 / 9 * (f - 32)
    print(f' {c} Graus Celsius')
else:
    c = int(input('Digite a temperatura'))
    f = 9 * c / 5 + 32
    print(f' {f} Graus Farenheit')