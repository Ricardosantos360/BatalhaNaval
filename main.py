# Cria duas variáveis para representar as vidas dos jogadores para ser usado depois.
# As duas começam com o valor 0.
vidajg1 = vidajg2 = 4

# Exibe o título do jogo.
# O operador * repete o texto "-=" vinte vezes.
print("-=" * 20)
print("JOGO DA BATALHA NAVAL")
print("-=" * 20)

# Define a opção inicial como 0 para que o menu comece.
opcao = 0

# Repete o menu enquanto o jogador não escolher a opção 3 (Sair).
while opcao != 3:

    # Exibe as opções disponíveis no menu principal.
    print("Escolha uma opção:")
    print("[ 1 ] Jogar")
    print("[ 2 ] Regras")
    print("[ 3 ] Sair")
    print("-=" * 20)

    # Recebe a opção digitada pelo usuário.
    # input() recebe o texto e int() tenta convertê-lo em número inteiro para análise.
    opcao = int(input("Digite sua escolha: "))

    # Verifica se o usuário escolheu iniciar uma partida.
    if opcao == 1:

        print("-+" * 20)

        # Solicita os nomes dos dois jogadores.
        jg1 = input("Digite o nome do 1º jogador: ")
        jg2 = input("Digite o nome do 2º jogador: ")

        print("-+" * 20)

        # !!!!! Sistema para escolher o jogador que vai iniciar de forma aleatoria. !!!!!
        escolhajg1 = int(input(f"Jogador {jg1}, digite um número de 1 a 10: "))
        escolhajg2 = int(input(f"Jogador {jg2} digite um número de 1 a 10: "))
        rst = (escolhajg1 * escolhajg2) % 2

        if rst == 0:
            vezjg = "jg1"
            print(f"O jogador que vai iniciar a partida é o {jg1}! ")
        else:
            vezjg = "jg2"
            print(f"O jogador que vai iniciar a partida é o {jg2}! ")
        print("-+" * 20)



        # Apresenta os jogadores e anuncia o início da partida.
        print(f"Muito bem, jogador {jg1} e jogador {jg2}, QUE COMECEM OS JOGOS!!!\n")

        # Apresentação da tabela/matriz de posicionamento dos barcos.
        print("-=" * 20)
        print(f"CARO JOGADOR {jg1}")
        print("POSICIONE OS SEUS BARCOS NA TABELA ABAIXO INFORMANDO SUAS POSIÇÕES")
        print("-=" * 20)
        print()

        # Exibição do tabuleiro 6x6 em branco antes do posicionamento
        print("    1   2   3   4   5   6")
        for i in range(6):
            print(i + 1, end="  ")  # Imprime o número da linha na lateral
            for j in range(6):
                print("[~]", end=" ")
            print()
        print()

        print("-=" * 20)
        print(f"CARO JOGADOR {jg2}")
        print("POSICIONE OS SEUS BARCOS NA TABELA ABAIXO INFORMANDO SUAS POSIÇÕES")
        print("-=" * 20)
        print()

        # Exibição do tabuleiro 6x6 em branco antes do posicionamento
        print("    1   2   3   4   5   6")
        for i in range(6):
            print(i + 1, end="  ")  # Imprime o número da linha na lateral
            for j in range(6):
                print("[~]", end=" ")
            print()
        print()

        while vidajg1 > 0 or vidajg2 > 0:
            if vezjg == "jg1":
                print("-=" * 20)
                print(f"TURNO DO JOGADOR: {jg1}")
                print("DIGITE O COMANDO DE ATAQUE COM BASE NA TABELA ABAIXO INFORMANDO SUAS POSIÇÕES")
                print("-=" * 20)
                print()

                # Exibição do tabuleiro 6x6 para o ataque do jogador
                print("    1   2   3   4   5   6")
                for i in range(6):
                    print(i + 1, end="  ")
                    for j in range(6):
                        print("[~]", end=" ")
                    print()
                print()
                ataquejg1 = input("COMANDO COORDENADA")

            elif vezjg == "jg2":
                print("-=" * 20)
                print(f"TURNO DO JOGADOR: {jg2}")
                print("DIGITE O COMANDO DE ATAQUE COM BASE NA TABELA ABAIXO INFORMANDO SUAS POSIÇÕES")
                print("-=" * 20)
                print()

                # Exibição do tabuleiro 6x6 para o ataque do jogador
                print("    1   2   3   4   5   6")
                for i in range(6):
                    print(i + 1, end="  ")
                    for j in range(6):
                        print("[~]", end=" ")
                    print()
                print()
                ataquejg2 = input("COMANDO COORDENADA")


            # analisando a estatiticas dos jogadores


        # Verifica se pelo menos um dos jogadores está com 0 vidas.
        # Como as vidas começam em 0, essa condição será verdadeira, então será usada mais depois.
        if vidajg1 == 0 or vidajg2 == 0:
            print("Jogo finalizado!")

    # Verifica se o usuário escolheu visualizar as regras.
    elif opcao == 2:

        print("-+" * 20)
        print("REGRAS E MECÂNICA")
        print("-+" * 20)

        # Explica o objetivo e o funcionamento básico do jogo.
        print("Objetivo: destruir todos os navios do adversário antes que ele destrua os seus.")
        print("Tabuleiro: cada jogador possui um tabuleiro com posições onde os navios ficam escondidos.")
        print("Ataque: em cada turno, o jogador escolhe uma coordenada para tentar acertar um navio.")
        print("Acerto: se atingir um navio, o jogador rival perde um ponto de vida.")
        print("Erro: se não atingir nenhum navio, a jogada é considerada uma tentativa perdida.")
        print("Turnos: os jogadores alternam suas jogadas até que a partida termine.")
        print("Vitória: vence quem destruir todos os navios do adversário primeiro.")

        print("-+" * 20)

    # Verifica se o usuário escolheu sair do jogo.
    elif opcao == 3:

        print("--" * 20)
        print("Saindo do jogo...")

    # Executa esta parte se o usuário digitar uma opção diferente de 1, 2 ou 3.
    else:
        print("Opção inválida! Digite outra opção!")

# Quando a opção 3 encerra o while, o programa chega a esta parte.
print("-=" * 20)
print("Jogo encerrado... Até mais!")
print("-=" * 20)