pessoas = {'nome':'Lucas','sexo':'M','idade':21}
del pessoas['idade'] #comando para remover 
pessoas['nome'] = 'Pedro' #comando para trocar tal coisa, no caso a pessoa nome deixar de ser lucas e vai ser pedro.
pessoas['peso'] = 65 # comando para adicionar um elemento no dicionário.
for k,v in pessoas.items(): #para cada uma das chaves.
    print(f'{k} = {v}')
