#Exercicio: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
#a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

def leiaInt(msg): #Função para ler um número inteiro
    """
    -> Função para ler um número inteiro
    :param msg: Mensagem a ser exibida
    :return: Retorna o número inteiro
    """
    ok = False #Recebe False(falso)
    valor = 0 #Recebe 0
    while True: #Enquanto o valor for diferente de um número inteiro, o programa vai ficar em loop
        n = str(input(msg)) #Transforma o valor em string
        if n.isnumeric(): #Faz a validação para ver se é um número inteiro
            valor = int(n) #Transforma o valor em inteiro
            ok = True #Se for um número inteiro, ok recebe True(verdadeiro)
        else:
            print('\033[31m ERRO! Digite um número inteiro válido \033[m')
        if ok: #Se o valor for um número inteiro, o programa vai sair do loop
            break
    return n #Retorna o valor

print() #Comando para pular linha
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
print('-'*35)
print('\033[31m MANUAL DA FUNÇÃO leiaInt\033[m')
print('-'*35)
help(leiaInt)