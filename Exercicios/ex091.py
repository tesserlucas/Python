print('-'*30)
print('CADASTRO DE JOGADOR DE FUTEBOL')
print('-'*30)
jogador = {}
lista = list()
time = list()
while True:
    jogador.clear()
    jogador['nome']= str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
    lista.clear()
    for c in range(0,tot):
        lista.append(int(input(f'   Quantos gols na partida {c+1} ? ')))
    jogador['gols'] = lista[:]
    jogador['total'] = sum(lista) #este sum é para somar 
    time.append(jogador.copy())
    op = " "
    while op not in "SN":
        op = str(input('Quer continuar [S/N] ? ')).upper()
        if op in "SN":
            break
        print('Erro! Responda somente S ou N')
    if op == "N":
        break
print('-='*30)
print('cod ', end='') # esse código da linha 26 até a 29 faz o cabeçalho 
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-='*30)
for k,v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
while True:
    busca = int(input('Mostra dado de qual jogador ? (999 para interromper) '))
    if busca == 999:
        break
    if busca >=len(time):
        print(f'ERRO! Não existe jogador com código {busca}! ')
    else:
        print(f'----- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'     No jogo {i+1} fez tantos {g} gols')
    print('-'*40)
print('<<<<< VOLTE SEMPRE! >>>>>')
