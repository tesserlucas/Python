print('-'*30)
print('CADASTRO DE JOGADOR DE FUTEBOL')
print('-'*30)
jogador = {}
lista = list()
cont = 0
jogador['nome']= str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
for c in range(0,tot):
    lista.append(int(input(f'Quantos gols na partida {c+1} ? ')))
jogador['gols'] = lista[:]
jogador['total'] = sum(lista) #este sum é para somar 
print('-='*25)
print(jogador)
print('-='*25)
for k,v in jogador.items():
    print(f' O campo {k} tem valor {v}')
print('-='*25)
print(f'O jogador {jogador['nome']} jogou {tot} partidas')
for i,v in enumerate(lista):
    print(f'   => Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {jogador['total']} gols')
print('-='*25)