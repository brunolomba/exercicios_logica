print('#' * 120)
print('Programa experiências.')
print('#' * 120)

quantidade_testes = int(input('Digite a quantidade de testes que vc deseja analisar.'))
total_cobaias = 0
coelhos = 0
ratos = 0
sapos = 0

for numero in range(quantidade_testes):
    quantidade_cobaias = int(input('Digite a quantidade de cobaias.'))
    total_cobaias += quantidade_cobaias
    tipo_cobaia = input('Digite C = Coelho, R = Ratos ou S = Sapos.')

    while tipo_cobaia != 'c' and tipo_cobaia != 'r' and tipo_cobaia != 's':
        print('Valor não permitido')
        tipo_cobaia = input('Digite C = Coelho, R = Ratos ou S = Sapos')

    if tipo_cobaia == 'c':
        coelhos += quantidade_cobaias
    elif tipo_cobaia == 'r':
        ratos += quantidade_cobaias
    elif tipo_cobaia == 's':
        sapos += quantidade_cobaias

def porcentagem(valor):
    calculo = valor / total_cobaias * 100
    return calculo

print(f'A quantidade de teste é de {quantidade_testes} com {total_cobaias} cobaias, sendo uma porcentagem de {porcentagem(coelhos)}% Coelhos, {porcentagem(ratos)}% ratos e {porcentagem(sapos)}% sapos.')

print('Fim do programa')