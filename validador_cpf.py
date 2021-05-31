print('#' * 120)
print('Validador de CPF')
print('#' * 120)

# Validação de quantidade de números
while True:
    cpf = input('Digite seu CPF')
    if len(cpf) >= 11 and len(cpf) <= 15:
        break
    else:
        print('CPF inválido')

# Conversão em lista
cpf_lista = list(cpf)

# Remoção do hífen
if len(cpf_lista) == 14:
    cpf_lista.pop(3)
    cpf_lista.pop(6)
    cpf_lista.pop(9)

if len(cpf_lista) == 12:
    cpf_lista.pop(9)

# Conversão para inteiros
convertido = []
for numero in cpf_lista:
    convertido.append(int(numero))

# Separação segundo digíto verificador
segundo_verificador = convertido[-1]
convertido.pop(-1)

# Segunda Multiplicação dos números do CPF
lista_multiplicada_2 = []
multiplicação = 11
for numero in convertido:
    lista_multiplicada_2.append(numero * multiplicação)
    multiplicação -= 1

# Separação primeiro digíto verificador
primeiro_verificador = convertido[-1]
convertido.pop(-1)

# Primeria Multiplicação dos números do CPF
lista_multiplicada_1 = []
multiplicação = 10
for numero in convertido:
    lista_multiplicada_1.append(numero * multiplicação)
    multiplicação -= 1

# Função de soma dos números multiplicados
def soma(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

resultado_soma_1 = soma(lista_multiplicada_1)
resultado_soma_2 = soma(lista_multiplicada_2)

# Função para achar o resto
def resto(valor):
    resto = valor * 10 % 11
    if resto == 10:
        resto = 0
    return resto

digito_1 = resto(resultado_soma_1)
digito_2 = resto(resultado_soma_2)

if digito_1 == primeiro_verificador and digito_2 == segundo_verificador:
    print(f'O CPF de número {cpf} é Válido')

print('FIM DO PROGRAMA')