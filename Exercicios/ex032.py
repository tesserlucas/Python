nome = input('Digite o nome do funcionário: ')
salario = float(input('Qual é o salário do funcionário {} '.format(nome)))
if salario > 1250:
    print('O funcionário {} recebia R$ {} com o aumento de 10% irá receber R$ {}'.format(nome, salario,salario+(salario*10/100)))
else:
    print('O funcionário {} recebia R$ {} com o aumento de 15% irá receber R$ {}'.format(nome,salario,salario+(salario*15/100)))
