def dobra(lista):
    pos = 0
    while pos < len(lista): #enquantos a posição for menor que a quantidade da lista
        lista[pos] *=2 # faze lista vezes 2 
        pos = pos + 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores) #imprime os valores 