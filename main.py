# Exibe o título do jogo.
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("JOGO DA BATALHA NAVAL")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

# Controla a repetição do menu principal.
# O programa continua enquanto a opção escolhida for diferente de 3.
opcao = 0

while opcao != 3:

    print("Escolha uma opção:")
    print("[ 1 ] Jogar")
    print("[ 2 ] Regras")
    print("[ 3 ] Sair")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    # O input recebe a escolha como texto, e int converte o valor para inteiro.
    opcao = int(input("Digite sua escolha: "))

    if opcao == 1:

        # Reinicia os dados necessários para uma nova partida.
        vitoriajogador = ""
        barcosjg1 = barcosjg2 = 4

        # Define as variáveis utilizadas para registrar as escolhas de PAR ou IMPAR
        # e identificar qual jogador começará a partida.
        parimpar1 = parimpar2 = vezjg = ""

        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

        # Armazena os nomes dos jogadores para personalizar as mensagens do jogo.
        jg1 = input("Digite o nome do 1º jogador: ")
        jg2 = input("Digite o nome do 2º jogador: ")

        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

        # Solicita uma escolha válida para o primeiro jogador.
        # O segundo jogador recebe automaticamente a escolha oposta.
        while parimpar1 != "PAR" and parimpar1 != "IMPAR":
            parimpar1 = input(f"Jogador {jg1}, escolha PAR ou IMPAR (escreva a resposta toda em maiúsculo): ")

            if parimpar1 == "PAR":
                parimpar2 = "IMPAR"
                print(f"Muito bem, o jogador {jg2} está com IMPAR!\n")

            elif parimpar1 == "IMPAR":
                parimpar2 = "PAR"
                print(f"Muito bem, o jogador {jg2} está com PAR!\n")

            else:
                print("OPÇÃO INVÁLIDA! Por favor, tente novamente!")

        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

        # Recebe um número de cada jogador.
        escolhajg1 = int(input(f"Jogador {jg1}, digite um número: "))
        escolhajg2 = int(input(f"Jogador {jg2} digite outro número: "))

        # O operador % calcula o resto da divisão.
        # O resto 0 representa PAR, enquanto o resto 1 representa IMPAR.
        rst = (escolhajg1 + escolhajg2) % 2

        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

        if rst == 0:
            print("O resultado deu PAR!")
        else:
            print("O resultado deu IMPAR!")

        # Compara o resultado da soma com a escolha do primeiro jogador.
        # A variável vezjg identifica quem iniciará a partida.
        if parimpar1 == "PAR":

            if rst == 0:
                vezjg = "jg1"
                print(f"O jogador que vai iniciar a partida é o {jg1}!")

            else:
                vezjg = "jg2"
                print(f"O jogador que vai iniciar a partida é o {jg2}!")

        elif parimpar1== "IMPAR":

            if rst != 0:
                vezjg = "jg1"
                print(f"O jogador que vai iniciar a partida é o {jg1}!")

            else:
                vezjg = "jg2"
                print(f"O jogador que vai iniciar a partida é o {jg2}!")

        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

        # Anuncia o início da partida.
        print(f"Muito bem, jogador {jg1} e jogador {jg2}, QUE COMECEM OS JOGOS!!!\n")

        # Cada matriz representa o tabuleiro de um jogador.
        # As linhas e colunas armazenam as coordenadas das posições.
        # Inicialmente, cada posição contém uma identificação, como A1 ou B3.
        tabuleiro1 = [
            ['A1', 'A2', 'A3', 'A4', 'A5', 'A6'],
            ['B1', 'B2', 'B3', 'B4', 'B5', 'B6'],
            ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
            ['D1', 'D2', 'D3', 'D4', 'D5', 'D6'],
            ['E1', 'E2', 'E3', 'E4', 'E5', 'E6'],
            ['F1', 'F2', 'F3', 'F4', 'F5', 'F6']
        ]

        tabuleiro2 = [
            ['A1', 'A2', 'A3', 'A4', 'A5', 'A6'],
            ['B1', 'B2', 'B3', 'B4', 'B5', 'B6'],
            ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
            ['D1', 'D2', 'D3', 'D4', 'D5', 'D6'],
            ['E1', 'E2', 'E3', 'E4', 'E5', 'E6'],
            ['F1', 'F2', 'F3', 'F4', 'F5', 'F6']
        ]

        # Guarda as letras que identificam as linhas do tabuleiro.
        linhas = 'ABCDEF'

        # Variáveis auxiliares para as escolhas e coordenadas.
        escolha = ''

        # Contabiliza a quantidade de navios posicionados por cada jogador.
        navios1 = navios2 = 0

        # Registra a quantidade de tentativas e acertos de cada jogador.
        tentativajg1 = tentativajg2 = 0
        acertojg1 = acertojg2 = 0

        # Armazena temporariamente as coordenadas de linha e coluna.
        posicaol = posicaoc = 0

        # Exibe o tabuleiro para o primeiro jogador posicionar seus navios.
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(f"CARO JOGADOR {jg1}")
        print("POSICIONE OS SEUS BARCOS NA TABELA ABAIXO INFORMANDO SUAS POSIÇÕES")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print()

        # Repete o posicionamento até que os quatro navios sejam informados.
        while navios1 < 4:

            # Percorre as seis linhas e as seis colunas da matriz.
            for i in range(6):
                for j in range(6):

                    # Obtém a posição atual do tabuleiro.
                    posicao = tabuleiro1[i][j]

                    # Marca a posição escolhida com 'x'.
                    if escolha == posicao:
                        tabuleiro1[i][j] = 'x'

                    # end=" " mantém as posições da mesma linha lado a lado.
                    print(f"[{tabuleiro1[i][j]}]", end=" ")

                # Pula uma linha após exibir todas as colunas.
                print()

            print()

            # Solicita a coordenada do próximo navio.
            escolha = input(f"Posição do Navio {navios1 + 1}: ")

            # Atualiza o contador de navios posicionados.
            navios1 += 1

        # Limpa a variável antes de iniciar o posicionamento do segundo jogador.
        escolha = ""

        # Exibe o tabuleiro para o segundo jogador posicionar seus navios.
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(f"CARO JOGADOR {jg2}")
        print("POSICIONE OS SEUS BARCOS NA TABELA ABAIXO INFORMANDO SUAS POSIÇÕES")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print()

        # Repete o processo de posicionamento para o segundo tabuleiro.
        while navios2 < 4:

            for i in range(6):
                for j in range(6):

                    # Obtém a posição atual do segundo tabuleiro.
                    posicao = tabuleiro2[i][j]

                    # Marca a posição escolhida com 'x'.
                    if escolha == posicao:
                        tabuleiro2[i][j] = 'x'

                    print(f"[{tabuleiro2[i][j]}]", end=" ")

                print()

            print()

            escolha = input(f"Posição do Navio {navios2 + 1}: ")

            # Atualiza o contador de navios posicionados.
            navios2 += 1

        # Mantém a partida ativa enquanto os dois jogadores ainda tiverem navios.
        # Quando um deles chegar a zero, a condição será falsa e a partida terminará.
        while barcosjg1 > 0 and barcosjg2 > 0:

            # Executa as ações do turno do primeiro jogador.
            if vezjg == "jg1":

                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print(f"TURNO DO JOGADOR: {jg1}")
                print("DIGITE O COMANDO DE ATAQUE COM BASE NA TABELA ABAIXO INFORMANDO SUAS POSIÇÕES")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                # Mostra o tabuleiro do adversário, onde estão os navios a serem atingidos.
                print("    1   2   3   4   5   6")

                for i in range(6):
                    for j in range(6):
                        print(f"[{tabuleiro2[i][j]}]", end=" ")
                    print()

                print()

                # Recebe os índices da linha e da coluna escolhidas para o ataque.
                posicaol = int(input("Digite a coordenada da LINHA que queira atacar: "))
                posicaoc = int(input("Digite a coordenada da COLUNA que queira atacar: "))

                # Verifica se a posição escolhida contém um navio.
                if tabuleiro2[posicaol][posicaoc] == "x":

                    # Um acerto reduz a quantidade de navios restantes do adversário.
                    barcosjg2 -= 1

                    print(f"Parabéns você acertou um Navio Inimigo! Faltam {barcosjg2} serem derrubados para a vitória!")

                    # Atualiza as estatísticas do primeiro jogador.
                    tentativajg1 += 1
                    acertojg1 += 1

                else:
                    # Em caso de erro, registra somente a tentativa.
                    print("Você errou! Bomba na Água, passando a vez...")
                    tentativajg1 += 1

                # Reinicia as variáveis auxiliares das coordenadas.
                posicaol = 0
                posicaoc = 0

            # Executa as ações do turno do segundo jogador.
            elif vezjg == "jg2":

                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print(f"TURNO DO JOGADOR: {jg2}")
                print("DIGITE O COMANDO DE ATAQUE COM BASE NA TABELA ABAIXO INFORMANDO SUAS POSIÇÕES")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                # Mostra o tabuleiro do primeiro jogador.
                print("    1   2   3   4   5   6")

                for i in range(6):
                    for j in range(6):
                        print(f"[{tabuleiro1[i][j]}]", end=" ")
                    print()

                print()

                # Recebe as coordenadas do ataque do segundo jogador.
                posicaol = int(input("Linha: "))
                posicaoc = int(input("Coluna: "))

                # Verifica se a posição escolhida contém um navio.
                if tabuleiro1[posicaol][posicaoc] == "x":

                    # Um acerto reduz a quantidade de navios restantes do primeiro jogador.
                    barcosjg1 -= 1

                    print(f"Parabéns você acertou um Navio Inimigo! Faltam {barcosjg1} serem derrubados para a vitória!")

                    # Atualiza as estatísticas do jogador.
                    tentativajg2 += 1
                    acertojg2 += 1

                else:
                    # Em caso de erro, registra somente a tentativa.
                    print("Você errou! Bomba na Água, passando a vez")
                    tentativajg1 += 1

                # Reinicia as variáveis auxiliares das coordenadas.
                posicaol = 0
                posicaoc = 0

            # Alterna o jogador que terá o próximo turno.
            if vezjg == "jg1":
                vezjg = "jg2"
            else:
                vezjg = "jg1"

            # Espaço reservado para implementar a análise das estatísticas dos jogadores.

            # Verifica se algum jogador perdeu todos os seus navios.
            if barcosjg1 == 0 or barcosjg2 == 0:

                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("Jogo finalizado! \n")

                # Identifica o vencedor com base na quantidade de navios restantes.
                if barcosjg1 == 0:
                    print(f"O jogador vencedor é o {jg2}")
                    vitoriajogador = "jg2"
                else:
                    print(f"O jogador vencedor é o {jg1}")
                    vitoriajogador = "jg1"

                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

                # Exibe as opções disponíveis após o encerramento da partida.
                # A opção 1 retorna ao menu principal; a opção 2 mostra as estatísticas.
                while opcao != 1:

                    print("Gostaria de voltar ao menu principal (para começar novamente ou sair) ou deseja ver as estastisticas gerais?")
                    print("[ 1 ] Voltar o menu principal")
                    print("[ 2 ] Tabela de Pontos")
                    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

                    opcao = int(input("Digite sua escolha: "))

                    if opcao == 1:
                        print("Tudo bem, voltando ao Menu principal!")
                        break

                    elif opcao == 2:

                        # Apresenta o resumo das estatísticas da partida.
                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                        print("         ESTATÍSTICAS DA PARTIDA")
                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

                        # Mostra as tentativas, os acertos e o resultado do primeiro jogador.
                        print(f"Jogador: {jg1}")
                        print(f"Tentativas: {tentativajg1}")
                        print(f"Acertos: {acertojg1}")

                        if vitoriajogador == "jg1":
                            print("VENCEDOR da última partida!")
                            print()
                        else:
                            print("PERDEDOR da última partida!")
                            print()

                        # Mostra as tentativas, os acertos e o resultado do segundo jogador.
                        print(f"Jogador: {jg2}")
                        print(f"Tentativas: {tentativajg2}")
                        print(f"Acertos: {acertojg2}")

                        if vitoriajogador == "jg2":
                            print("VENCEDOR da última partida!")
                            print()
                        else:
                            print("PERDEDOR da última partida!")
                            print()

                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

                    else:
                        # Solicita uma nova escolha caso a opção seja inválida.
                        opcao = int(input("Opção inválida! Digite outra opção: "))

    elif opcao == 2:

        # Apresenta as regras e explica a mecânica básica do jogo.
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("REGRAS E MECÂNICA")
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

        print("Objetivo: destruir todos os navios do adversário antes que ele destrua os seus.")
        print("Tabuleiro: cada jogador possui um tabuleiro com posições onde os navios ficam escondidos.")
        print("Ataque: em cada turno, o jogador escolhe uma coordenada para tentar acertar um navio.")
        print("Acerto: se atingir um navio, o jogador rival perde um barco no mar.")
        print("Erro: se não atingir nenhum navio, a jogada é considerada uma tentativa perdida.")
        print("Turnos: os jogadores alternam suas jogadas até o fim da partida.")
        print("Vitória: vence quem destruir todos os 4 navios do adversário primeiro.")

        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

    elif opcao == 3:

        # Encerra a repetição do menu principal ao escolher a opção 3.
        print("----------------------------------------")
        print("Saindo do jogo...")

    else:

        # Informa quando a opção escolhida não corresponde às opções disponíveis.
        print("Opção inválida! Digite outra opção!")

# Mensagem exibida quando o laço do menu principal termina.
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Jogo encerrado... Até mais!")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
