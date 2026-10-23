# Define as vidas iniciais dos jogadores e as variáveis de controle da partida.
vidajg1 = vidajg2 = 4
parimpar = ["", ""]
vezjg = ""

# Exibe o título do jogo.
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("JOGO DA BATALHA NAVAL")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

# Mantém o menu ativo até o usuário escolher a opção 3.
opcao = 0

while opcao != 3:

    # Exibe as opções do menu principal.
    print("Escolha uma opção:")
    print("[ 1 ] Jogar")
    print("[ 2 ] Regras")
    print("[ 3 ] Sair")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    # Recebe a opção digitada e converte o texto para um número inteiro.
    opcao = int(input("Digite sua escolha: "))

    if opcao == 1:

        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

        # Solicita os nomes dos dois jogadores.
        jg1 = input("Digite o nome do 1º jogador: ")
        jg2 = input("Digite o nome do 2º jogador: ")

        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

        # Solicita PAR ou IMPAR até que o primeiro jogador informe uma opção válida.
        # Também define a escolha oposta para o segundo jogador.
        while parimpar[0] != "PAR" and parimpar[0] != "IMPAR":
            parimpar[0] = input(f"Jogador {jg1}, escolha PAR ou IMPAR (escreva a resposta toda em maiúsculo): ")
            if parimpar[0] == "PAR":
                parimpar[1] = "IMPAR"
                print(f"Muito bem, o jogador {jg2} está com IMPAR!\n")
            elif parimpar[0] == "IMPAR":
                parimpar[1] = "PAR"
                print(f"Muito bem, o jogador {jg2} está com PAR!\n")
            else:
                print("OPÇÃO INVÁLIDA! Por favor, tente novamente!")

        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

        # Recebe os números escolhidos pelos jogadores e calcula o resto da soma por 2.
        escolhajg1 = int(input(f"Jogador {jg1}, digite um número de 1 a 10: "))
        escolhajg2 = int(input(f"Jogador {jg2} digite um número de 1 a 10: "))
        rst = (escolhajg1 + escolhajg2) % 2

        # O resto 0 indica PAR; o resto 1 indica IMPAR.
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        if rst == 0:
            print("O resultado deu PAR!")
        else:
            print("O resultado deu IMPAR!")

        # Compara o resultado com a escolha do primeiro jogador para definir quem começa.
        if parimpar[0] == "PAR":
            if rst == 0:
                vezjg = "jg1"
                print(f"O jogador que vai iniciar a partida é o {jg1}!")
            else:
                vezjg = "jg2"
                print(f"O jogador que vai iniciar a partida é o {jg2}!")

        elif parimpar[0] == "IMPAR":
            if rst != 0:
                vezjg = "jg1"
                print(f"O jogador que vai iniciar a partida é o {jg1}!")
            else:
                vezjg = "jg2"
                print(f"O jogador que vai iniciar a partida é o {jg2}!")

        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

        # Anuncia o início da partida.
        print(f"Muito bem, jogador {jg1} e jogador {jg2}, QUE COMECEM OS JOGOS!!!\n")

        # Apresenta o tabuleiro vazio do primeiro jogador.
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(f"CARO JOGADOR {jg1}")
        print("POSICIONE OS SEUS BARCOS NA TABELA ABAIXO INFORMANDO SUAS POSIÇÕES")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print()

        # Cria visualmente um tabuleiro de 6 linhas por 6 colunas.
        # O primeiro for controla as linhas e o segundo controla as colunas.
        print("    1   2   3   4   5   6")
        for i in range(6):
            print(i + 1, end="  ")
            for j in range(6):
                print("[~]", end=" ")
            print()
        print()

        # Apresenta o tabuleiro vazio do segundo jogador.
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(f"CARO JOGADOR {jg2}")
        print("POSICIONE OS SEUS BARCOS NA TABELA ABAIXO INFORMANDO SUAS POSIÇÕES")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print()

        print("    1   2   3   4   5   6")
        for i in range(6):
            print(i + 1, end="  ")
            for j in range(6):
                print("[~]", end=" ")
            print()
        print()

        # Repete os turnos enquanto pelo menos um jogador tiver vidas.
        while vidajg1 > 0 or vidajg2 > 0:

            if vezjg == "jg1":

                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print(f"TURNO DO JOGADOR: {jg1}")
                print("DIGITE O COMANDO DE ATAQUE COM BASE NA TABELA ABAIXO INFORMANDO SUAS POSIÇÕES")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                # Exibe o tabuleiro durante o turno do primeiro jogador.
                print("    1   2   3   4   5   6")
                for i in range(6):
                    print(i + 1, end="  ")
                    for j in range(6):
                        print("[~]", end=" ")
                    print()
                print()

                # Recebe a coordenada de ataque do primeiro jogador.
                ataquejg1 = input("COMANDO COORDENADA")

            elif vezjg == "jg2":

                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print(f"TURNO DO JOGADOR: {jg2}")
                print("DIGITE O COMANDO DE ATAQUE COM BASE NA TABELA ABAIXO INFORMANDO SUAS POSIÇÕES")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                # Exibe o tabuleiro durante o turno do segundo jogador.
                print("    1   2   3   4   5   6")
                for i in range(6):
                    print(i + 1, end="  ")
                    for j in range(6):
                        print("[~]", end=" ")
                    print()
                print()

                # Recebe a coordenada de ataque do segundo jogador.
                ataquejg2 = input("COMANDO COORDENADA")

            # Espaço reservado para implementar a análise das estatísticas dos jogadores.

        # Verifica se pelo menos um jogador chegou a zero vidas para encerrar a partida.
        if vidajg1 == 0 or vidajg2 == 0:
            print("Jogo finalizado!")

    elif opcao == 2:

        # Exibe as regras e explica a mecânica básica do jogo.
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("REGRAS E MECÂNICA")
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

        print("Objetivo: destruir todos os navios do adversário antes que ele destrua os seus.")
        print("Tabuleiro: cada jogador possui um tabuleiro com posições onde os navios ficam escondidos.")
        print("Ataque: em cada turno, o jogador escolhe uma coordenada para tentar acertar um navio.")
        print("Acerto: se atingir um navio, o jogador rival perde um ponto de vida.")
        print("Erro: se não atingir nenhum navio, a jogada é considerada uma tentativa perdida.")
        print("Turnos: os jogadores alternam suas jogadas até que a partida termine.")
        print("Vitória: vence quem destruir todos os navios do adversário primeiro.")

        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

    elif opcao == 3:

        # Exibe a mensagem de saída escolhida pelo usuário.
        print("----------------------------------------")
        print("Saindo do jogo...")

    else:

        # Informa quando a opção digitada não corresponde a nenhuma opção do menu.
        print("Opção inválida! Digite outra opção!")

# Exibe a mensagem final quando o menu é encerrado.
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Jogo encerrado... Até mais!")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")