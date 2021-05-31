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

def calcular_digito_correto():
    # Entradas
    agencia = input('Digite a sua Agência.')
    conta = input('Digite a sua Conta.')

    # Junção e conversão da conta em inteiros.
    conta_completa = list(agencia + conta)
    conta_convertida = [int(valor) for valor in conta_completa]

    # Isolamento do digíto.
    digito_removido = remocao_digito(conta_convertida)

    # Atualização da conta.
    conta_convertida_sem_digito = conta_convertida

    # Multiplicação por 2 dos valores PARES.
    conta_multiplicada = multiplicao_valores(conta_convertida_sem_digito)

    # Conversão dos números de 2 digítos.
    conta_multiplicada_sem_2_digitos = conversao_numero_2_digitos(conta_multiplicada)

    # Cálculo do digíto.
    digito = calculo_digito(conta_multiplicada_sem_2_digitos)

    # Verificação do digíto.
    if digito == digito_removido:
        print(f'O digito da conta está correto, é: {digito}')

    #Exibição da verificação do digíto e da conta completa.
    exibicao(agencia, conta, digito)

# Funções
def remocao_digito(conta_convertida):
    digito_removido = []
    if len(conta_convertida) == 10:
        digito_removido = conta_convertida.pop(9)
    return digito_removido

def multiplicao_valores(conta_convertida_sem_digito):
    for i in range(len(conta_convertida_sem_digito)):
        if i % 2 == 0:
            conta_convertida_sem_digito[i] = conta_convertida_sem_digito[i] * 2
    return conta_convertida_sem_digito

def conversao_numero_2_digitos(conta_multiplicada):
    soma_unidade = 0
    for i, numero in enumerate(conta_multiplicada):
        if numero > 9:
            for unidade in str(numero):
                soma_unidade += int(unidade)
                conta_multiplicada[i] = soma_unidade
    return conta_multiplicada

def calculo_digito(conta_multiplicada_sem_2_digitos):
    soma = sum(conta_multiplicada_sem_2_digitos)
    resto = soma % 10
    digito = 10 - resto
    return digito

def exibicao(agencia, conta, digito):
    print(f'O número da conta é ag {agencia} / conta: {conta[:-1]}-{digito}')
    print('FIM DO PROGRAMA')

if __name__ == '__main__':
    calcular_digito_correto()