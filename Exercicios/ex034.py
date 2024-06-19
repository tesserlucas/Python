casa = float(input('Qual é o valor da casa: R$ '))
salario = float(input('Qual é o salário do comprador: R$ '))
ano = int(input('Em quantos anos você vai pagar ? '))
p = (casa / ano) / 12
s = salario * 30 / 100
print('Para pagar uma casa de R$ {} em {} anos a prestação será de R$ {:.2f}'.format(casa,ano,p))
if p <= s:
    print('Empréstimo pode ser concedido')
else:
    print('Empréstimo negado')