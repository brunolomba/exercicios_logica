def validar():
    # Título do programa.
    apresentacao()

    # Validador da quantidade de número digitado na entrada.
    cpf = validador_quantidade_numeros()

    # Conversão em lista
    cpf_lista = list(cpf)

    # Remoção do hífen
    if len(cpf_lista) == 14:
        lista_sem_pontuacao = remocao_pontuacao_14(cpf_lista)
    if len(cpf_lista) == 12:
        lista_sem_pontuacao = remocao_pontuacao_12(cpf_lista)
    lista_sem_pontuacao = cpf_lista

    # Conversão de String para Integer
    lista_convertida = [int(numero) for numero in lista_sem_pontuacao]

    # Isolando segundo digíto verificador.
    segundo_verificador = lista_convertida.pop(-1)

    # Segunda Multiplicação dos números do CPF.
    lista_multiplicada_2 = multiplicacao_sem_ultimo_digito(lista_convertida)

    # Isolando primeiro digíto verificador.
    primeiro_verificador = lista_convertida.pop(-1)
    
    # Primeria Multiplicação dos números do CPF.
    lista_multiplicada_1 = multiplicacao_sem_2_ultimos_digitos(lista_convertida)

    # Soma dos elementos multiplicados das listas.
    resultado_soma_1 = soma(lista_multiplicada_1)
    resultado_soma_2 = soma(lista_multiplicada_2)

    # Verificando calculo dos digítos.
    digito_1 = resto(resultado_soma_1)
    digito_2 = resto(resultado_soma_2)

    # Verificação e validação dos digítos.
    if digito_1 == primeiro_verificador and digito_2 == segundo_verificador:
        print(f'O CPF {cpf} é Válido')
    else:
        print(f'O CPF {cpf} é Inválido')

    print('FIM DO PROGRAMA')

# Funções
def apresentacao():
    print('########################')
    print('##  Validador de CPF  ##')
    print('########################')

def validador_quantidade_numeros():
    while True:
        cpf = input('Digite seu CPF: ')
        if len(cpf) >= 11 and len(cpf) <= 15:
            return cpf
        else:
            print('CPF inválido')

def remocao_pontuacao_14(cpf_lista):
    cpf_lista.pop(3)
    cpf_lista.pop(6)
    cpf_lista.pop(9)
    return cpf_lista

def remocao_pontuacao_12(cpf_lista):
    cpf_lista.pop(9)
    return cpf_lista

def multiplicacao_sem_ultimo_digito(lista_convertida):
    lista_multiplicada_2 = []
    multiplicação = 11
    for numero in lista_convertida:
        lista_multiplicada_2.append(numero * multiplicação)
        multiplicação -= 1
    return lista_multiplicada_2

def multiplicacao_sem_2_ultimos_digitos(lista_convertida):
    lista_multiplicada_1 = []
    multiplicação = 10
    for numero in lista_convertida:
        lista_multiplicada_1.append(numero * multiplicação)
        multiplicação -= 1
    return lista_multiplicada_1

def soma(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

def resto(valor):
    resto = valor * 10 % 11
    if resto == 10:
        resto = 0
    return resto

if __name__ == '__main__':
    validar()