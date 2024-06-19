print('\033[36m ========== LOJA TESSER ==========\033[m')
preco = float(input('Preço das compras: R$ '))
vista = preco - (preco*10/100)
debito = preco - (preco*5/100)
credito2x = preco
credito3x = preco + (preco*20/100)
print('[1] à vista dinheiro/cheque')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
op = int(input('Sua opção: '))
if op == 1:
    print('Sua compra de R$ {} vai custar R$ {:.2f} no final'.format(preco, vista))
elif op == 2:
    print('Sua compra de R$ {} vai custar R$ {:.2f} no final'.format(preco, debito))
elif op == 3:
    p1 = int(input('Deseja fazer em 1x ou 2x ? '))
    if p1 == 1:
        print('Sua compra custara {:.2f}'.format(preco))
    elif p1 == 2:
        print('Parcelando em 2x você vai pagar a 1ºparcela de R$ {:.2f} e a 2º de R$ {:.2f}'.format(preco/2,preco/2))
    print('Sua compra de R$ {} vai custar R$ {:.2f} no final'.format(preco, credito2x))
elif op == 4:
    p = int(input('Quantas parcelas ? '))
    print('Sua compra sera parcelada em {}x de R$ {:.2f} COM JUROS'.format(p,credito3x/p))
    print('Sua compra de R$ {} vai custar R$ {:.2f} no final'.format(preco, credito3x))
else:
    print('Opção inválida')
