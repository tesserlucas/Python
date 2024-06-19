import moedas

num = float(input('Digite um valor: '))
print(f'O dobro de R${moedas.moeda(num)} é {moedas.moeda(moedas.dobro(num))} ')
print(f'A metade de R${moedas.moeda(num)} é {moedas.moeda(moedas.metade(num))}')
print(f'Aumentando R${moedas.moeda(num)} em 10% temos {moedas.moeda(moedas.aumentar(num,10))}') 