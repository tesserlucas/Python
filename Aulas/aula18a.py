galera = list()
dado = list()
totmen = 0
totmai = 0
for c in range(0,5):
    dado.append(str(input('Digite seu nome:')))
    dado.append(int(input('Sua idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >=21: #para mostrar as pessoas maior de 21 anos
        print(f'O {p[0]} é maior de idade')
        totmai = totmai +1
    else:
        print(f'O {p[0]} é de menor')
        totmen = totmen +1
print(f'Temos {totmai} maiores e {totmen} menores')