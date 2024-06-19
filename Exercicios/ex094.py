print('-'*40)
print('PROGRAMA PARA FAZER CONTAGEM DE NÚMEROS')
print('-'*40)
from time import sleep
def contador (i,f,p):
    print('-='*20)
    print(f'Contagem de {i} até o {f} de {p} em {p}')
    sleep(2)
    if p < 0: #esse p menor que 0 é para ele funcionar a contagem quando que quiser número negativo
        p *= -1
    if p == 0: #esse p igual a 0 é para ele funcionar a contagem quando que quiser número zero
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True) #esse flush=True é para não ficar imprimindo tudo de uma vez
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p 
        print('FIM')
    print('-='*20)

#Programa principal
contador(1,10,1)
contador(10,0,2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)