# Soma da linha escolhida n:
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29

def row_sum_odd_numbers(n):
    lista = []
    linha = 1
    contador_impar = 1
    
    while linha <= n:
        
        for i in range(1, linha + 1):
            if linha == n:
                lista.append(contador_impar)
            contador_impar += 2
        linha += 1
        
    return sum(lista)

print(row_sum_odd_numbers(3))

