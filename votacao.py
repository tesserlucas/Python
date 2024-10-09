# Programa para simular uma votação municipal 

candidatos_prefeito = {
    45: {'nome': 'Diogo Siqueira', 'votos': 0},
    22: {'nome': 'Heliomar', 'votos': 0},
    55: {'nome': 'Paulo Caleffi', 'votos': 0},
    15: {'nome': 'Sebastião Mello', 'votos': 0},
}

candidatos_vereador = {
    45111: {'nome': 'Luiz Carlos', 'votos': 0},
    11000: {'nome': 'Eduardo', 'votos': 0},
    11111: {'nome': 'Davi', 'votos': 0},
    45000: {'nome': 'José', 'votos': 0},
}

while True:
    print('\n'"\033[31m      Votação Municipal   \033[m")
    print('-='*15)
    print("1 - Votar no Prefeito")
    print("2 - Votar no Vereador")
    print("3 - Ver resultados Parciais")
    print("4 - Sair")
    print('-='*15)
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nCandidatos ao Prefeito:")
        print('-'*30)
        for numero, info in candidatos_prefeito.items():
            print(f"{numero} - {info['nome']}")
        print('-'*30)
        
        while True:
            try:
                numero = int(input("Digite o número do candidato ao prefeito: (ou 0 para voltar ao menu): "))
                if numero == 0:
                    break
                elif numero in candidatos_prefeito:
                    candidatos_prefeito[numero]['votos'] += 1
                    print(f"Voto computado para {candidatos_prefeito[numero]['nome']}")
                else:
                    print("Número de candidato inválido")
            except ValueError:
                print("Número de candidato inválido")
    elif opcao == '2':
        print("\nCandidatos ao Vereador:")
        print('-'*30)
        for numero, info in candidatos_vereador.items():
            print(f"{numero} - {info['nome']}")
        print('-'*30)

        while True:
            try:
                numero = int(input("Digite o número do candidato ao vereador: (ou 0 para voltar ao menu): "))
                if numero == 0:
                    break
                if numero in candidatos_vereador:
                    candidatos_vereador[numero]['votos'] += 1
                    print(f"Voto computado para {candidatos_vereador[numero]['nome']}")
                else:
                    print("Número de candidato inválido")
            except ValueError:
                print("Número de candidato inválido")
    elif opcao == "3":
        print("\n\033[32mResultados Parciais para Prefeito:\033[m")
        print('-'*40)
        for info in candidatos_prefeito.values():
            print(f"{info['nome']} - {info['votos']} votos")
        
        print("\n\033[32mResultados parciais para Vereador:\033[m")
        print('-'*40)
        for info in candidatos_vereador.values():
            print(f"{info['nome']} - {info['votos']} votos")
    elif opcao == "4":
        print("Encerrando o programa, Até Mais!")
        break
    else:
        print("Opção inválida, por favor escolha uma opção válida")