# Exibe o título do jogo.
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("JOGO DA BATALHA NAVAL")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

# Controla a repetição do menu principal.
opcao = 0

# Armazena as estatísticas acumuladas durante toda a sessão.
vitoriasjg1 = vitoriasjg2 = totalpartidas = 0


while opcao != 3:

    print("Escolha uma opção:")
    print("[ 1 ] Jogar")
    print("[ 2 ] Regras")
    print("[ 3 ] Sair")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    # Valida a escolha do usuário sem converter diretamente a entrada para inteiro.
    valido = False

    while not valido:

        entrada = input("Digite sua escolha: ")

        for n in range(1, 4):
            if entrada == str(n):
                opcao = n
                valido = True

        if not valido:
            print("Opção inválida! Digite uma das opções")


    if opcao == 1:

        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

        # Solicita os nomes dos jogadores para identificar as suas ações durante o jogo.
        jg1 = input("Digite o nome do 1º jogador: ")
        jg2 = input("Digite o nome do 2º jogador: ")

        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

        # Controla a repetição das partidas com os mesmos jogadores.
        jogar = True

        while jogar:

            # Reinicia os navios e as variáveis de controle para uma nova partida.
            barcosjg1 = barcosjg2 = 4
            parimpar1 = parimpar2 = vezjg = ""

            # O primeiro jogador escolhe PAR ou IMPAR para definir quem começará.
            while parimpar1 != "PAR" and parimpar1 != "IMPAR":
                parimpar1 = input(f"Jogador {jg1}, escolha PAR ou IMPAR (escreva a resposta toda em maiúsculo): ")

                if parimpar1 == "PAR":
                    print(f"Muito bem, o jogador {jg2} está com IMPAR!\n")

                elif parimpar1 == "IMPAR":
                    print(f"Muito bem, o jogador {jg2} está com PAR!\n")

                else:
                    print("OPÇÃO INVÁLIDA! Por favor, tente novamente!")

            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

            # Recebe e valida os números escolhidos pelos dois jogadores.
            valida = False
            escolhajg1 = escolhajg2 = 0

            while not valida:
                entrada = input(f"Jogador {jg1}, digite um número (de 0 a 9): ")

                for n in range(0, 10):
                    if entrada == str(n):
                        valida = True
                        escolhajg1 = n

                if not valida:
                    print("Opção inválida. Digite um número entre 0 e 9")

            valida = False
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            while not valida:

                entrada = input(f"Jogador {jg2}, digite um número (de 0 a 9): ")

                for n in range(0, 10):
                    if entrada == str(n):
                        valida = True
                        escolhajg2 = n

                if not valida:
                    print("Opção inválida. Digite um número entre 0 e 9")


            # Calcula o resto da divisão da soma por 2 para identificar PAR ou IMPAR.
            rst = (escolhajg1 + escolhajg2) % 2

            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

            if rst == 0:
                print("O resultado deu PAR!")
            else:
                print("O resultado deu IMPAR!")

            # Compara o resultado com a escolha do primeiro jogador para definir quem começa.
            if parimpar1 == "PAR":

                if rst == 0:
                    vezjg = "jg1"
                    print(f"O jogador que vai iniciar a partida é o {jg1}!")
                    print()

                else:
                    vezjg = "jg2"
                    print(f"O jogador que vai iniciar a partida é o {jg2}!")
                    print()

            elif parimpar1== "IMPAR":

                if rst != 0:
                    vezjg = "jg1"
                    print(f"O jogador que vai iniciar a partida é o {jg1}!")
                    print()

                else:
                    vezjg = "jg2"
                    print(f"O jogador que vai iniciar a partida é o {jg2}!")
                    print()

            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

            # Anuncia o início da partida.
            print(f"Muito bem, jogador {jg1} e jogador {jg2}, QUE COMECEM OS JOGOS!!!")

            # Cria os tabuleiros dos jogadores com coordenadas de 00 a 55.
            tabuleiro1 = [
                ['00', '01', '02', '03', '04', '05'],
                ['10', '11', '12', '13', '14', '15'],
                ['20', '21', '22', '23', '24', '25'],
                ['30', '31', '32', '33', '34', '35'],
                ['40', '41', '42', '43', '44', '45'],
                ['50', '51', '52', '53', '54', '55']
            ]

            tabuleiro2 = [
                ['00', '01', '02', '03', '04', '05'],
                ['10', '11', '12', '13', '14', '15'],
                ['20', '21', '22', '23', '24', '25'],
                ['30', '31', '32', '33', '34', '35'],
                ['40', '41', '42', '43', '44', '45'],
                ['50', '51', '52', '53', '54', '55']
            ]

            # Inicializa as variáveis utilizadas no posicionamento dos navios.
            escolha = ''
            navios1 = navios2 = 0

            # Reinicia as estatísticas individuais para a partida atual.
            tentativajg1 = tentativajg2 = 0
            acertojg1 = acertojg2 = 0
            errojg1 = errojg2 = 0

            # Armazena temporariamente as coordenadas de linha e coluna.
            posicaol = posicaoc = 0

            # Inicia a etapa de posicionamento dos navios do primeiro jogador.
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print(f"CARO JOGADOR {jg1}")
            print("POSICIONE OS SEUS BARCOS NA TABELA ABAIXO INFORMANDO SUAS POSIÇÕES")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print()

            # Repete o posicionamento até que os quatro navios sejam informados.
            while navios1 < 4:

                print("    0    1    2    3    4    5")

                # Percorre as linhas e colunas para exibir o tabuleiro.
                for i in range(6):
                    print(f"{i}", end=" ")
                    for j in range(6):
                        print(f"[{tabuleiro1[i][j]}]", end=" ")

                    print()

                print()

                # Solicita e valida uma coordenada disponível para posicionar o navio.
                is_valida = False
                while not is_valida:
                    escolha = input(f"Posição do Navio {navios1 + 1}: ")

                    for i in range(6):
                        for j in range(6):
                            if escolha == tabuleiro1[i][j]:
                                is_valida = True

                    if not is_valida:
                        print("Posição inválida!")

                # Marca a posição escolhida com 'x' para representar um navio.
                for i in range(6):
                    for j in range(6):
                        posicao = tabuleiro1[i][j]

                        if escolha == posicao:
                            tabuleiro1[i][j] = 'x'

                # Atualiza a quantidade de navios posicionados.
                navios1 += 1

            print()
            print()
            print()
            print()

            # Inicia a etapa de posicionamento dos navios do segundo jogador.
            escolha = ""

            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print(f"CARO JOGADOR {jg2}")
            print("POSICIONE OS SEUS BARCOS NA TABELA ABAIXO INFORMANDO SUAS POSIÇÕES")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print()

            # Repete o posicionamento até que os quatro navios sejam informados.
            while navios2 < 4:

                print("   0    1    2    3    4    5")

                # Percorre as linhas e colunas para exibir o tabuleiro.
                for i in range(6):
                    print(f"{i}", end=" ")
                    for j in range(6):
                        print(f"[{tabuleiro2[i][j]}]", end=" ")

                    print()

                print()

                # Solicita e valida uma coordenada disponível para posicionar o navio.
                is_valida = False
                while not is_valida:
                    escolha = input(f"Posição do Navio {navios2 + 1}: ")

                    for i in range(6):
                        for j in range(6):
                            if escolha == tabuleiro2[i][j]:
                                is_valida = True

                    if not is_valida:
                        print("Posição inválida!")

                # Marca a posição escolhida com 'x' para representar um navio.
                for i in range(6):
                    for j in range(6):
                        posicao = tabuleiro2[i][j]

                        if escolha == posicao:
                            tabuleiro2[i][j] = 'x'

                # Atualiza a quantidade de navios posicionados.
                navios2 += 1

                # Exibe o tabuleiro após o posicionamento do navio.
                print("   0    1    2    3    4    5")

                for i in range(6):
                    print(f"{i}", end=" ")
                    for j in range(6):
                        print(f"[{tabuleiro2[i][j]}]", end=" ")

                    print()

                print()

            print()
            print()
            print()

            # Mantém a partida ativa enquanto os dois jogadores tiverem navios.
            while barcosjg1 > 0 and barcosjg2 > 0:

                # Executa as ações do turno do primeiro jogador.
                if vezjg == "jg1":

                    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                    print(f"TURNO DO JOGADOR: {jg1}")
                    print("DIGITE O COMANDO DE ATAQUE COM BASE NA TABELA ABAIXO INFORMANDO SUAS POSIÇÕES")
                    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                    print()

                    # Exibe o tabuleiro adversário sem revelar a posição dos navios.
                    print("   0   1   2   3   4   5")

                    for i in range(6):
                        print(f"{i}", end=" ")
                        for j in range(6):
                            print("[~]", end=" ")
                        print()

                    print()

                    # Solicita e valida a coordenada da linha do ataque.
                    valida_l = False
                    while not valida_l:
                        entrada_l = input("Digite a coordenada da LINHA (0-5): ")
                        for n in range(0, 6):
                            if entrada_l == str(n):
                                posicaol = n
                                valida_l = True

                        if not valida_l:
                            print("Coordenada inválida! Digite apenas um número de 0 a 5.")

                    # Solicita e valida a coordenada da coluna do ataque.
                    valida_c = False
                    while not valida_c:
                        entrada_c = input("Digite a coordenada da COLUNA que queira atacar (0-5): ")

                        for n in range(0, 6):
                            if entrada_c == str(n):
                                posicaoc = n
                                valida_c = True

                        if not valida_c:
                            print("Coordenada inválida! Digite apenas um número de 0 a 5.")

                    # Verifica se a coordenada escolhida contém um navio adversário.
                    if tabuleiro2[posicaol][posicaoc] == "x":

                        # Diminui a quantidade de navios restantes do segundo jogador.
                        barcosjg2 -= 1

                        print(f"Parabéns você acertou um Navio Inimigo! Faltam {barcosjg2} serem derrubados para a vitória!")

                        # Marca o navio atingido para impedir que seja contabilizado novamente.
                        tabuleiro2[posicaol][posicaoc] = "AC"

                        # Atualiza as estatísticas de tentativas e acertos do primeiro jogador.
                        tentativajg1 += 1
                        acertojg1 += 1

                    else:
                        # Registra a tentativa e o erro quando a posição não contém um navio.
                        print("Você errou! Bomba na Água, passando a vez...")
                        tentativajg1 += 1
                        errojg1 += 1

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

                    # Exibe o tabuleiro adversário sem revelar a posição dos navios.
                    print("   0   1   2   3   4   5")

                    for i in range(6):
                        print(f"{i}", end=" ")
                        for j in range(6):
                            print("[~]", end=" ")
                        print()

                    print()

                    # Solicita e valida a coordenada da linha do ataque.
                    valida_l = False

                    while not valida_l:
                        entrada_l = input("Digite a coordenada da LINHA (0-5): ")
                        for n in range(0, 6):
                            if entrada_l == str(n):
                                posicaol = n
                                valida_l = True

                        if not valida_l:
                            print("Coordenada inválida! Digite apenas um número de 0 a 5.")

                    # Solicita e valida a coordenada da coluna do ataque.
                    valida_c = False
                    while not valida_c:
                        entrada_c = input("Digite a coordenada da COLUNA que queira atacar (0-5): ")

                        for n in range(0, 6):
                            if entrada_c == str(n):
                                posicaoc = n
                                valida_c = True

                        if not valida_c:
                            print("Coordenada inválida! Digite apenas um número de 0 a 5.")

                    # Verifica se a coordenada escolhida contém um navio adversário.
                    if tabuleiro1[posicaol][posicaoc] == "x":

                        # Diminui a quantidade de navios restantes do primeiro jogador.
                        barcosjg1 -= 1

                        print(f"Parabéns você acertou um Navio Inimigo! Faltam {barcosjg1} serem derrubados para a vitória!")

                        # Marca o navio atingido para impedir que seja contabilizado novamente.
                        tabuleiro1[posicaol][posicaoc] = "AC"

                        # Atualiza as estatísticas de tentativas e acertos do segundo jogador.
                        tentativajg2 += 1
                        acertojg2 += 1

                    else:
                        # Registra a tentativa e o erro quando a posição não contém um navio.
                        print("Você errou! Bomba na Água, passando a vez")
                        tentativajg2 += 1
                        errojg2 += 1

                    # Reinicia as variáveis auxiliares das coordenadas.
                    posicaol = 0
                    posicaoc = 0

                # Alterna o turno entre os dois jogadores.
                if vezjg == "jg1":
                    vezjg = "jg2"
                else:
                    vezjg = "jg1"

                # Verifica se algum jogador perdeu todos os seus navios.
                if barcosjg1 == 0 or barcosjg2 == 0:

                    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                    print("Jogo finalizado! \n")

                    # Identifica o vencedor e atualiza a sua quantidade de vitórias.
                    if barcosjg1 == 0:
                        print(f"O jogador vencedor é o {jg2}")
                        vitoriajogador = "jg2"
                        vitoriasjg2 += 1
                    else:
                        print(f"O jogador vencedor é o {jg1}")
                        vitoriajogador = "jg1"
                        vitoriasjg1 += 1

                    # Atualiza o total de partidas realizadas durante a sessão.
                    totalpartidas += 1

                    # Apresenta as opções disponíveis após o encerramento da partida.
                    opcaofim = 0
                    menu_final = True

                    while menu_final:

                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                        print("MENU FINAL")
                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                        print("[ 1 ] Rejogar")
                        print("[ 2 ] Estatísticas Gerais")
                        print("[ 3 ] Menu Principal")
                        print("[ 4 ] Sair")
                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

                        # Valida a opção escolhida no menu final.
                        valida = False

                        while not valida:

                            entrada = input("Digite sua escolha: ")

                            for n in range(1, 5):
                                if entrada == str(n):
                                    opcaofim = n
                                    valida = True

                            if not valida:
                                print("Opção inválida!")

                        # Encerra o menu final para iniciar uma nova partida com os mesmos jogadores.
                        if opcaofim == 1:
                            menu_final = False

                        # Exibe as estatísticas acumuladas e os resultados da última partida.
                        elif opcaofim == 2:
                            print()
                            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                            print("ESTATÍSTICAS GERAIS")
                            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                            print(f"Total de partidas: {totalpartidas}")
                            print(f"Vitórias do Jogador 1: {vitoriasjg1}")
                            print(f"Vitórias do Jogador 2: {vitoriasjg2}")

                            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                            print(f"Tentativas do Jogador 1 no jogo: {tentativajg1}")
                            print(f"Acertos do Jogador 1 no jogo: {acertojg1}")
                            print(f"Tentativas do Jogador 2 no jogo: {tentativajg2}")
                            print(f"Acertos do Jogador 2 no jogo: {acertojg2}")
                            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                            print()

                        # Retorna ao menu principal para cadastrar novos jogadores.
                        elif opcaofim == 3:
                            menu_final = False
                            jogar = False
                            opcao = 0

                        # Encerra o jogo e impede a repetição dos menus.
                        elif opcaofim == 4:
                            menu_final = False
                            jogar = False
                            opcao = 3

    # Apresenta as regras e explica a mecânica básica do jogo.
    elif opcao == 2:

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

    # Encerra a repetição do menu principal quando o usuário escolhe sair.
    elif opcao == 3:

        print("----------------------------------------")
        print("Saindo do jogo...")

    else:

        print("Opção inválida! Digite outra opção!")

# Exibe a mensagem final após o encerramento do menu principal.
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Jogo encerrado... Até mais!")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")