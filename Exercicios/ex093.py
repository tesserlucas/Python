def mensagem(msg):
    tam = len(msg) + 4 #comando para deixar a quantidade de linha de acordo com o tamanho da frase
    print('-'*tam) #em vezes de fazer vezes tantos traços faz vezes o tam que dai ele faz do tamanho da frase
    print(f'  {msg}')
    print('-'*tam)

mensagem('Curso de Python')
mensagem('Curso em vídeo')
mensagem('Lucas')