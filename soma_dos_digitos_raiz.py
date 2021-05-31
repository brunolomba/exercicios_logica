digitos = '235423427'
def soma_dos_digitos_raiz():
    # Conversão em lista.
    lista = list(digitos)
    # Conversão de String para Integer.
    lista_convertida = conversao_para_inteiros(lista)
    # Soma dos elementos da lista.
    resultado = soma(lista_convertida)
    # Lopping para separação  e soma dos elementos de 2 digítos.
    numero_final = looping_para_somar_numeros_2_digitos(resultado)
    # Exibição do resultado.
    exibicao(numero_final)
    
#Funções
def conversao_para_inteiros(lista):
    for i, numero in enumerate(lista):
        lista[i] = int(numero)
    return lista

def soma(lista_convertida):
    soma = sum(lista_convertida)
    return soma

def looping_para_somar_numeros_2_digitos(resultado):
        while resultado > 9:
            conversao_para_string = str(resultado)

            soma_2 = 0
            for numero in conversao_para_string:
                soma_2 += int(numero)

            resultado = soma_2
            soma_2 = 0
        else:
            return resultado

def exibicao(numero_final):
    print(f'O número final é {numero_final}.')

if __name__ == '__main__':
    soma_dos_digitos_raiz()