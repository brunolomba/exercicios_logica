# Highest Rank Number in an Array

# def highest_rank(arr):
#     segundo_maior = 0
#     qtd_segundo_maior = 0
#     maior = 0
#     qtd_maior = 0
    
#     for x in arr:
#         if arr.count(x) > maior:
#             qtd_maior = arr.count(x)
#             maior = x
#         elif arr.count(x) > qtd_segundo_maior:
#             qtd_segundo_maior = arr.count(x)
#             segundo_maior = x
#     print(segundo_maior)
#     print(qtd_segundo_maior)
#     print(maior)
#     print(qtd_maior)
#     if qtd_maior >= qtd_segundo_maior:
#         return maior
#     else:
#         return segundo_maior

# print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]))

# Delete occurrences of an element if it occurs more than n times

livros_yan = [['Banco MySQL'], ['Certificação PHP', 'TDD PHP'], ['HTML5 e CSS3']]
livros_pedro = livros_yan[:]

livros_yan.append('Python game')

print(livros_yan)
print(livros_pedro)
print(id(livros_yan))
print(id(livros_pedro))

url = 'pagina?argumentos'
indice = url.find('?')
print(url[indice + 1:] )


        