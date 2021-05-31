preco = float(input('Digite o valor do produto'))
quantidade = int(input('Digite a quantidade'))
dinheiro_recebido = float(input('Digite o valor recebido'))
valor_total = preco * quantidade

if dinheiro_recebido > valor_total:
    troco = dinheiro_recebido - valor_total
    print(f'O valor total foi de {valor_total} e seu troco é de {troco}')
else:
    resto = valor_total - dinheiro_recebido
    print(f'O valor total foi de {valor_total} e faltam {resto} reais')

print(troco)


# troco = 0
# resto = 0

# if dinheiro_recebido > preco * quantidade:
#     troco = dinheiro_recebido - preco * quantidade
#     print(f'O seu troco é de {troco} reais')
# else:
#     resto = preco * quantidade - dinheiro_recebido
#     print(f'O seu troco é de {troco} reais') 