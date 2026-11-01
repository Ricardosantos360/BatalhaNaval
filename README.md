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
Os tabuleiros de jogo foram criados como matrizes por extenso de tamanho 6x6. Para facilitar a localização por parte dos jogadores humanos, preenchemos inicialmente cada posição com strings amigáveis que misturam letras e números (de `'A1'` até `'F6'`). 
* Na fase de posicionamento, o jogador escolhe a casa digitando esse texto (ex: `"C3"`).
* O programa faz uma varredura com um laço `for` na matriz e, ao encontrar a casa equivalente, substitui o texto pelo caractere `'x'`, que representa um barco guardado com sucesso.
