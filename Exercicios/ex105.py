import moedas

num = float(input('Digite um valor: '))
print(f'O dobro de {moedas.moeda(num)} é {moedas.dobro(num,True)} ') #Esse true é para mostrar o R$
print(f'A metade de {moedas.moeda(num)} é {moedas.metade(num,True)}')
print(f'Aumentando {moedas.moeda(num)} em 10% temos {moedas.aumentar(num,10,True)}') 
print(f'Dimunuindo {moedas.aumentar(num)} em 15% temos {moedas.dimunuir(num,15,True)}')