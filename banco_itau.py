# 341 - ITAU
# Tamanha da Agência - 4 dígitos
# Tamanha da conta - 5 dígitos

# Exemplo:
# Agência: 2545
# Conta: 023661

# Para Obter o DV, multiplica-se cada número da Agência e Conta em sua ordenação. Sequências PAR multiplica-se por 1 e ÍMPARES por 2. Se o número encontrado for maior que 9, soma-se as unidades da dezena.

# Conta: AAAACCCCCD
# Peso:  212121212

# Módulo (10) 39/10 = 9 ~ Resto = 9 ~ Dígito = 10 - 9 = 1
# OBS: se o RESTO = 0 ~ o Dígito é 0

# Entradas
agencia = input('Digite a sua Agência.')
conta = input('Digite a sua Conta.')

# Junção e conversão da conta em inteiros
conta_completa = list(agencia + conta)
conta_convertida = [int(valor) for valor in conta_completa]

# Verificação e isolamento do digíto
digito_removido = []
if len(conta_convertida) == 10:
    digito_removido = conta_convertida.pop(9)
    
# Multiplicação dos valores PARES
for i in range(len(conta_convertida)):
    if i % 2 == 0:
        conta_convertida[i] = conta_convertida[i] * 2

# Conversão dos números de 2 digítos
soma_unidade = 0
for i, numero in enumerate(conta_convertida):
    if numero > 9:
        for unidade in str(numero):
            soma_unidade += int(unidade)
            conta_convertida[i] = soma_unidade

# Cálculo do digíto
soma = sum(conta_convertida)
resto = soma % 10
digito = 10 - resto

# Verificação do digíto, se a pessoa já tiver passado ele
if digito == digito_removido:
    print('O digito da conta está correto')

print(f'Os numeros conta_convertida é: {conta_convertida}, a soma deles é: {soma} e o digíto é :{digito}.') 
print(f'O número da conta é ag / conta: {agencia} / {conta[:-1]}-{digito}')
print('FIM DO PROGRAMA')