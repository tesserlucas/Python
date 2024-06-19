estado = {}
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #esse metodo .copy() é para copiar o conteúdo do dicionário
for e in brasil: # para cada estado no brasil, esse for é da lista
    for v in e.values(): #esse for aqui de dentro é do dicionário
        #print(f'O campo {k} tem valor {v}') # para esse comando fazer o for k,v in e.items()
        print(v, end=' ')
    print()