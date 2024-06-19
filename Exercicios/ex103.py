import moedas

num = float(input('Digite um valor: '))
print(f'O dobro de R${num} é R${moedas.dobro(num)} ')
print(f'A metade de R${num} é R${moedas.metade(num)}')
print(f'Aumentando R${num} em 10% temos R${moedas.aumentar(num,10)}') #Esse 10 vai aumentar o valor em 10%