print('Seja Bem Vindo a nossa loja Barato Mania')
print('1- Blusa \n2- Camisa Polo\n3- Calça Jeans\n4- Camisa social')
r = int(input('Qual roupa você deseja ?:'))
if r == 1:
    print('Blusa')
elif r == 2:
    print('Camisa Polo')
elif r == 3:
    print('Calça Jeans')
elif r == 4:
    print('Camisa social')
else:
    print('Opção inválida')
p = float(input('Digite o valor do produto R$: '))
d = p - (p*10/100)
a = p + (p*5/100)
print('Se comprar a {} a vista terá 10% de desconto e produto sairá por R$ {:.2f}'.format(r,d))
print('Se comprar no crédito terá um aumento de 5% e sairá por R$ {:.2f}'.format(a))
