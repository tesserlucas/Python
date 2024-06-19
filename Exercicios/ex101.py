#Exercicio; Faça um programa que tenha uma função notas() que pode receber várias 
#notas de alunos e vai retornar um dicionário.

def notas(*n,sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict() #Dicionário vazio
    r['total'] = len(n) #r recebe o total de notas
    r['maior'] = max(n) #r recebe o maior valor
    r['menor'] = min(n) #r recebe o menor valor
    r['média'] = sum(n)/len(n) #r recebe a média das notas
    if sit:
        if r['média'] > 7:
            r['situação']  = 'BOA'
        elif r['média'] >=5:
            r['situação'] = 'REGULAR'
        else:
            r['situação'] = 'RUIM'
    
    return r


#Programa principal
resp = notas(5.5,2.5,9,8.5, sit=True)
print(resp)
print('-='*20)
help(notas) #Mostra a documentação da função
print('-='*20)