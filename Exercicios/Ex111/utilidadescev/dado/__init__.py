def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        #Vai substituir todas as virgulas por pontos e o .strip vai remover os espaços
        if entrada.isalpha() or entrada == '': # Se a entrada for alfanúmerico vai dar erro
            #ou se a entrada tiver espaços vazios tbm vai dar erro.
            print(f'\033[31m ERRO! \"{entrada}\" preço inválido\033[m')
        else:
            valido = True
            return float(entrada)