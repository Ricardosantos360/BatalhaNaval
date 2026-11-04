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

        # Variáveis auxiliares para as escolhas e coordenadas.
        escolha = ''

        # Contabiliza a quantidade de navios posicionados por cada jogador.
        navios1 = navios2 = 0

        # Registra a quantidade de tentativas, acertos e erros de cada jogador.
        tentativajg1 = tentativajg2 = 0
        acertojg1 = acertojg2 = 0
        errojg1 = errojg2 = 0

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

            print("    0    1    2    3    4    5")

            # Percorre as seis linhas e as seis colunas da matriz.
            for i in range(6):
                print(f"{i}", end=" ")
                for j in range(6):

                    # Obtém a posição atual do tabuleiro.
                    posicao = tabuleiro1[i][j]

                    # end=" " mantém as posições da mesma linha lado a lado.
                    print(f"[{tabuleiro1[i][j]}]", end=" ")

                # Pula uma linha após exibir todas as colunas.
                print()

            print()

            # Solicita a coordenada do próximo navio.
            escolha = input(f"Posição do Navio {navios1 + 1}: ")

            for i in range(6):
                for j in range(6):

                    # Obtém a posição atual do tabuleiro.
                    posicao = tabuleiro1[i][j]

                    # Marca a posição escolhida com 'x'.
                    if escolha == posicao:
                        tabuleiro1[i][j] = 'x'
            

            # Atualiza o contador de navios posicionados.
            navios1 += 1
        print()
        print()
        print()
        print()

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

            print("   0    1    2    3    4    5")

            # Percorre as seis linhas e as seis colunas da matriz.
            for i in range(6):
                print(f"{i}", end=" ")
                for j in range(6):

                    # Obtém a posição atual do tabuleiro.
                    posicao = tabuleiro2[i][j]

                    # end=" " mantém as posições da mesma linha lado a lado.
                    print(f"[{tabuleiro2[i][j]}]", end=" ")

                # Pula uma linha após exibir todas as colunas.
                print()

            print()

            # Solicita a coordenada do próximo navio.
            escolha = input(f"Posição do Navio {navios2 + 1}: ")

            for i in range(6):
                for j in range(6):

                    # Obtém a posição atual do tabuleiro.
                    posicao = tabuleiro2[i][j]

                    # Marca a posição escolhida com 'x'.
                    if escolha == posicao:
                        tabuleiro2[i][j] = 'x'
                    

            # Atualiza o contador de navios posicionados.
            navios2 += 1
        print()
        print()
        print()

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
                print("   0   1   2   3   4   5")

                for i in range(6):
                    print(f"{i}", end=" ")
                    for j in range(6):
                        print("[~]", end=" ")
                    print()

                print()

                # Recebe os índices da linha e da coluna escolhidas para o ataque.
                valida_l = False
                while valida_l == False:
                    entrada_l = input("Digite a coordenada da LINHA que queira atacar (0-5): ")
                    for n in range(0, 6):
                        if entrada_l == str(n):
                            posicaol = n
                            valida_l = True
                    if valida_l == False:
                        print("Coordenada inválida! Digite apenas um número de 0 a 5.")

                valida_c = False
                while valida_c == False:
                    entrada_c = input("Digite a coordenada da COLUNA que queira atacar (0-5): ")
                    for n in range(0, 6):
                        if entrada_c == str(n):
                            posicaoc = n
                            valida_c = True
                    if valida_c == False:
                        print("Coordenada inválida! Digite apenas um número de 0 a 5.")

                # Verifica se a posição escolhida contém um navio.
                if tabuleiro2[posicaol][posicaoc] == "x":

                    # Um acerto reduz a quantidade de navios restantes do adversário.
                    barcosjg2 -= 1

                    print(f"Parabéns você acertou um Navio Inimigo! Faltam {barcosjg2} serem derrubados para a vitória!")

                     # Faz com que o usuario não consiga acerta o mesmo barco varia vezes
                    tabuleiro2[posicaol][posicaoc] = "AC"

                    # Atualiza as estatísticas do primeiro jogador.
                    tentativajg1 += 1
                    acertojg1 += 1

                else:
                    # Em caso de erro, registra somente a tentativa.
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

                # Mostra o tabuleiro do primeiro jogador.
                print("   0   1   2   3   4   5")

                for i in range(6):
                    print(f"{i}", end=" ")
                    for j in range(6):
                        print("[~]", end=" ")
                    print()

                print()

                valida_l = False
                while valida_l == False:
                    # Lemos o input puro como texto (string), o que nunca quebra o código
                    entrada_l = input("Linha (0-5): ")
                    
                    # Varremos os números válidos e transformamos em texto para comparar
                    for n in range(0, 6): # Testa de "0" até "5"
                        if entrada_l == str(n):
                            valida_l = True
                            posicaol = n # Guarda o número inteiro de forma segura
                            
                    if valida_l == False:
                        print("Coordenada inválida! Digite apenas um número de 0 a 5.")

                valida_c = False
                while valida_c == False:
                    entrada_c = input("Coluna (0-5): ")
                    
                    for n in range(0, 6):
                        if entrada_c == str(n):
                            valida_c = True
                            posicaoc = n
                            
                    if valida_c == False:
                        print("Coordenada inválida! Digite apenas um número de 0 a 5.")


                # Verifica se a posição escolhida contém um navio.
                if tabuleiro1[posicaol][posicaoc] == "x":

                    # Um acerto reduz a quantidade de navios restantes do primeiro jogador.
                    barcosjg1 -= 1

                    print(f"Parabéns você acertou um Navio Inimigo! Faltam {barcosjg1} serem derrubados para a vitória!")

                    # Faz com que o usuario não consiga acerta o mesmo barco varia vezes
                    tabuleiro1[posicaol][posicaoc] = "AC"

                    # Atualiza as estatísticas do jogador.
                    tentativajg2 += 1
                    acertojg2 += 1

                else:
                    # Em caso de erro, registra somente a tentativa.
                    print("Você errou! Bomba na Água, passando a vez")
                    tentativajg2 += 1
                    errojg2 += 1

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
                opcaofim = 0 

                while opcaofim != 1:

                    print("Gostaria de voltar ao menu principal (para começar novamente ou sair) ou deseja ver as estastisticas gerais?")
                    print("[ 1 ] Voltar o menu principal")
                    print("[ 2 ] Tabela de Pontos")
                    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

                    opcaofim = int(input("Digite sua escolha: "))
                    print()

                    if opcaofim == 1:
                        print("Tudo bem, voltando ao Menu principal!")
                        opcao = 1
                        print()
                        break

                    elif opcaofim == 2:

                        # Apresenta o resumo das estatísticas da partida.
                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                        print("         ESTATÍSTICAS DA PARTIDA")
                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

                        # Mostra as tentativas, os acertos e o resultado do primeiro jogador.
                        print(f"Jogador: {jg1}")
                        print(f"Tentativas: {tentativajg1}")
                        print(f"Acertos: {acertojg1}")
                        print(f"Erros: {errojg1}")

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
                        print(f"Erros: {errojg2}")

                        if vitoriajogador == "jg2":
                            print("VENCEDOR da última partida!")
                            print()
                        else:
                            print("PERDEDOR da última partida!")
                            print()

                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

                    else:
                        # Solicita uma nova escolha caso a opção seja inválida.
                        opcaofim = int(input("Opção inválida! Digite outra opção: "))

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
