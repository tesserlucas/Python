produto = ('Lápis', 2.52,
           'Borracha', 3.50,
           'Caneta', 8.00,
           'Caderno', 22.50,
           'Livro', 55.20,
           'Estojo', 11.00,
           'Calculadora', 82.50)
print('-'*35)
print('LISTAGEM DE PREÇO')
print('-'*35)
for pos in range(0, len(produto)):
    if pos % 2 == 0:
        print(f'{produto[pos]:.<20}', end='')
    else:
        print(f'R${produto[pos]:>5}')
print('-'*35)