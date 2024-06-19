def leiaInt(msg): #Função para ler um número inteiro
    while True:
        try: #Tente fazer isso
            ni = int(input(msg))
        except (ValueError,TypeError): #Se der algum problema retorna os erros
            print('\033[31mERRO! Por favor digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('\033[31m O usuário preferiou não digitar um número \033[m')
            return 0
        else: #Se não der problema então retorna o valor de ni
            return ni

def leiafloat(msg):
    while True:
        try:
            nf = float(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO! Por favor digite um número real válido\033[m')
        except KeyboardInterrupt:
            print('\033[31m O usuário preferiou não digitar um número \033[m')
            return 0
        else:
            return nf


print() #Comando para pular linha
ni = leiaInt('Número inteiro: ')
nf = leiafloat('Número real: ')
print(f'O valor inteiro digitado foi {ni} e o valor real digitado foi {nf}')
