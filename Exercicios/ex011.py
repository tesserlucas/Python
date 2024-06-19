produto = float(input('Valor do produto R$: '))
desco = produto - (produto*5/100)
print('O preço do produto é R$ {:.2f}, com o desconto de 5% fica R$ {:.2f}'.format(produto, desco))
print('O valor de desconto foi de R$ {:.2f}'.format(produto - desco))