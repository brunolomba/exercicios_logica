print('#' * 120)
print('Programa escolha quantas divisões você pretende fazer, para dividir o número "X" por "Y".')
print('#' * 120)

vezes = int(input('Digite a quantidade de vezes você deseja dividir.'))

for numero in range(vezes):
    numerador = int(input('Digite o valor do numerador.'))
    denominador = int(input('Digite o valor do denominador.'))

    if denominador == 0:
        print('Impossível dividir')
    else:
        divisao = numerador / denominador
        print(f'A divisão do denominador {numerador} pelo divisor {denominador} é: {divisao}.')

print('Fim do programa')