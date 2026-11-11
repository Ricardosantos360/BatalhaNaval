# ⚓ Batalha Naval Simplificada 6x6 - Terminal Python

Este projeto consiste em um jogo de Batalha Naval desenvolvido inteiramente em Python para rodar no terminal. O software foi construído como o trabalho prático da 2ª Avaliação da disciplina de **Coding** no curso de Bacharelado em Ciência da Computação (**UNINASSAU**).

## 📊 Organização e Gestão do Projeto
Para garantir que o código fosse desenvolvido de forma justa e organizada dentro do prazo, nossa equipe utilizou um quadro no **Trello** para mapear o Backlog, as tarefas em andamento e as revisões de código. 

Abaixo está a divisão real de funções do nosso trio:

*   **André Duarte:** Responsável pela geração dos tabuleiros 6x6, sistema de visualização inicial das tabelas para os jogadores, criação do menu de fim de jogo (sair/tentar novamente), tabela de estatísticas pós-partida e apoio na análise e correção de erros de lógica.

*   **Ricardo Araújo:** Responsável pela criação do Menu Principal, desenvolvimento da mecânica de Par ou Ímpar para decidir o turno inicial e suporte ativo no mapeamento e correção de bugs do sistema.

*   **Henrique Abreu:** Responsável pelo núcleo de funcionamento do jogo, lógica de posicionamento dos navios na matriz, sistema de turnos de ataque e implementação das rotinas de validação de dados.

## ⚙️ Funcionamento das Mecânicas Principais

### 1. Sistema de Par ou Ímpar (Quem começa?)
Para definir qual jogador inicia atacando sem desrespeitar a regra de não usar a biblioteca `random`, implementamos um sistema matemático limpo:
1. O Jogador 1 digita se quer `PAR` ou `IMPAR`. O Jogador 2 recebe o oposto.
2. Cada jogador digita um número inteiro qualquer.
3. O programa calcula a soma deles e usa o operador `% 2` (resto da divisão). Se o resto for 0 o resultado é PAR, se for 1 é ÍMPAR.
4. O sistema compara com a escolha inicial e define dinamicamente a variável `vezjg`.

### 2. A Lógica dos Tabuleiros (Matriz 6x6)
Os tabuleiros de jogo foram criados como matrizes por extenso de tamanho 6x6. Para facilitar a localização por parte dos jogadores, preenchemos inicialmente cada posição com strings que misturam números de linhas e colunas (de `'00'` até `'55'`). 
* Na fase de posicionamento, o jogador escolhe a casa digitando esse texto (ex: `"03"`).
* O programa faz uma varredura com um laço `for` na matriz e, ao encontrar a casa equivalente, substitui o texto pelo caractere `'x'`, que representa um barco guardado com sucesso.

## 📜 Regras e Mecânica Oficial (Extraído do Sistema)
Com base nas diretrizes internas implementadas no código da nossa partida, o jogo segue o seguinte regulamento de engajamento:
*   **Objetivo:** Destruir todos os navios do adversário antes que ele destrua os seus.
*   **Tabuleiro:** Cada jogador possui um tabuleiro (Matriz 6x6) com posições indexadas de 0 a 5 onde os navios ficam escondidos.
*   **Ataque:** Em cada turno, o jogador escolhe uma coordenada para tentar acertar um navio.
*   **Acerto:** Se atingir um navio, o jogador rival perde um barco no mar (a casa é marcada como `"AC"`).
*   **Erro:** Se não atingir nenhum navio, a jogada é considerada uma tentativa perdida.
*   **Turnos:** Os jogadores alternam suas jogadas de forma automatizada até o fim da partida.
*   **Vitória:** Vence quem destruir todos os 4 navios do adversário primeiro.

## 🎯 Desafio de Lógica Escolhido
Implementamos o desafio **"Estatísticas da Sessão ao Sair"**. Quando o menu principal recebe o comando de encerramento (`3`), o sistema compila os dados persistentes de todas as rodadas executadas, apresentando:
* Número de tentativas.
* Números de acertos.
* Número de erros.
* Quem foi o vencedor da última partida.

## 🛠️ Como Executar o Jogo
1. Certifique-se de possuir o interpretador do **Python 3** instalado em seu ambiente.
2. Faça o clone deste repositório ou realize o download do arquivo `main.py`.
3. Abra a janela de terminal ou PowerShell na pasta raiz correspondente ao arquivo e execute o programa.
  
