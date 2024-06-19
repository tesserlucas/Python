num = [1,2,3,4]
num[3] = 8 #este comando muda o valor da lista na posição selecionada.
num.append(4) # comando para adicionar um valor na lista
num.sort() # comando para deixar a lista em ordem
num.insert(2, 0) #comando para inserir valor, ali quero add o zero na posição dois.
del num[3] #comando para remover elemento, ali quero remover o elemento da posição 3.
num.pop() #comando para remover, se deixar vazio ele vai remover o último elemento.
num.remove(0) #comando para remover, ele vai remover o elemento zero e não o da posição zero.
#num.sort(reverse=True) # comando para deixar a lista em ordem inversa
if 5 in num: #comando usado para que se tiver o número 4 na lista ele remove, senão não remove nada
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos')