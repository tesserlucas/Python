dia = int(input('Quantos dias o carro foi alugado ? '))
qtd = float(input('Quantos KM o carro percorreu ? '))
tot = (dia*60)+(qtd*0.15)
print('Foram {} dias e foi percorrido {} KM o valor total foi de R$ {}'.format(dia, qtd, tot))
