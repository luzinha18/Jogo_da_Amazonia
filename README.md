# Jogo de Adivinhação Educativo: Floresta Amazônica

## Objetivo do Projeto

Este projeto consiste em um jogo de adivinhação educativo interativo, desenvolvido em Python, focado na fauna, flora e geografia da Floresta Amazônica. O objetivo é proporcionar uma experiência de aprendizado divertida, onde os jogadores respondem a perguntas sobre a Amazônia e recebem feedback imediato, além de uma classificação final baseada em seu desempenho.

## Lógica Computacional Implementada

O jogo é estruturado em torno de um quiz interativo com as seguintes características:

1.  **Banco de Perguntas**: As perguntas, suas alternativas e a resposta correta são armazenadas em uma lista de dicionários. Cada dicionário representa uma pergunta e contém as chaves `pergunta`, `alternativas` (uma lista de strings) e `correta` (a letra da alternativa correta).

2.  **Sorteio Aleatório e Sem Repetição**: Utiliza o módulo `random` para sortear as perguntas de forma aleatória. Uma lista auxiliar de índices é embaralhada, garantindo que cada pergunta seja apresentada apenas uma vez durante a sessão do jogo.

3.  **Laço Principal (`while`)**: O fluxo do jogo é controlado por um laço `while` que itera sobre todas as perguntas disponíveis.

4.  **Condicionais (`if/elif/else`)**: São empregadas para:
    *   Validar a entrada do usuário, garantindo que a resposta seja uma das opções válidas (A, B, C ou D).
    *   Fornecer feedback imediato ao jogador, indicando se a resposta está correta ou incorreta.
    *   Calcular a pontuação e classificar o jogador ao final do jogo.

5.  **Função com Parâmetros**: Uma função `exibir_ranking(pontuacao, total_perguntas)` é utilizada para processar e exibir a classificação final do jogador. Esta função recebe a pontuação obtida e o número total de perguntas para determinar o percentual de acertos e atribuir uma classificação (ex: "Guardião da Floresta", "Aprendiz").

6.  **Acumulador de Pontuação**: Uma variável `pontuacao` atua como acumulador, incrementando a cada resposta correta.

## Como Executar o Jogo

Para executar o jogo, siga os passos abaixo:

1.  **Pré-requisitos**: Certifique-se de ter o Python 3 instalado em seu sistema.

2.  **Clonar o Repositório**: Se você estiver em um ambiente Git, clone este repositório para sua máquina local:
    ```bash
    git clone [URL_DO_REPOSITORIO]
    cd Jogo_da_Amazonia
    ```
    (A URL do repositório será fornecida após a publicação no GitHub.)

3.  **Executar o Script**: Navegue até o diretório do projeto e execute o script `main.py` usando o interpretador Python:
    ```bash
    python3 main.py
    ```

4.  **Interagir com o Jogo**: Siga as instruções no terminal para responder às perguntas. Ao final, você receberá sua pontuação e classificação.

Link: [quiz](https://colab.research.google.com/drive/1Y2jMfwjcfFyoRZI_oOpVrvNsZAYMBph5?usp=sharing)
