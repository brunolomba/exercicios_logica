preco_produto = float(input('digite o valor do produto'))
quantidade_produto = int(input('digite a quantidade de produtos'))
valor_recebido = float(input('digite o valor recebido'))

valor_total = preco_produto * quantidade_produto
troco = valor_recebido - valor_total

print(f' O valor total foi de {valor_total} e o valor do troco é {troco}')