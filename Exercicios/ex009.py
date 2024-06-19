n=float(input("Quanto dinheiro você tem ? R$ "))
dolar = n/4.96
euro =n/5.35
print('Com {} reias você pode comprar {:.2f} USD'.format(n,dolar))
print('Com {} reais, você pode comprar {:.2f} euros'.format(n,euro))
