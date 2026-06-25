import random

def exibir_ranking(pontuacao, total_perguntas):
    percentual = (pontuacao / total_perguntas) * 100
    print("\n" + "="*30)
    print(" RANKING FINAL")
    print("="*30)
    print(f"Sua pontuação: {pontuacao}/{total_perguntas}")

    if percentual == 100:
        classificacao = "Guardião da Floresta"
        mensagem = "Incrível! Você conhece a Amazônia como ninguém."
    elif percentual >= 70:
        classificacao = "Explorador Experiente"
        mensagem = "Muito bem! Você tem um ótimo conhecimento sobre a região."
    elif percentual >= 50:
        classificacao = "Aprendiz"
        mensagem = "Bom trabalho! Continue estudando para proteger nossa floresta."
    else:
        classificacao = "Visitante Curioso"
        mensagem = "A Amazônia é vasta! Que tal aprender um pouco mais sobre ela?"

    # Exibir classificação e retorno 
    print(f"Classificação: {classificacao}")
    print(f"Feedback: {mensagem}")
    print("="*30 + "\n")

def jogar():

    # Banco de dados de perguntas (Lista de Dicionários)
    perguntas = [
        {
            "pergunta": "Qual é o maior peixe de água doce da Amazônia?",
            "alternativas": ["A) Tucunaré", "B) Pirarucu", "C) Tambaqui", "D) Piranha"],
            "correta": "B"
        },
        {
            "pergunta": "Qual árvore é conhecida como a 'Rainha da Floresta'?",
            "alternativas": ["A) Castanheira", "B) Seringueira", "C) Samaúma", "D) Ipê"],
            "correta": "C"
        },
        {
            "pergunta": "Qual desses animais é um símbolo da fauna amazônica e vive nos rios?",
            "alternativas": ["A) Arara-azul", "B) Boto-cor-de-rosa", "C) Onça-pintada", "D) Mico-leão-dourado"],
            "correta": "B"
        },
        {
            "pergunta": "A Floresta Amazônica abrange o território de quantos países?",
            "alternativas": ["A) 5", "B) 7", "C) 9", "D) 12"],
            "correta": "C"
        },
        {
            "pergunta": "Qual destas aves é típica da Amazônia?",
            "alternativas": ["A) Avestruz", "B) Pinguim", "C) Pelicano", "D) Arara"],
            "correta": "D"
        },
        {
            "pergunta": "Qual é o clima predominante na Amazônia?",
            "alternativas": ["A) Desértico", "B) Mediterrâneo", "C) Tropical úmido", "D) Verão"],
            "correta": "C"
        },
        {
            "pergunta": "Qual destes animais não vive na Amazônia?",
            "alternativas": ["A) Sucuri", "B) Boto-cor-de-rosa", "C) Girafa", "D) Sauim-de-coleira"],
            "correta": "C"
        },
        {
            "pergunta": "A Floresta Amazônica é frequentemente chamada de:",
            "alternativas": ["A) Os Pulmões do Planeta", "B) O Coração do Mundo", "C) A Terra Gelada", "D) Matagal"],
            "correta": "A"
        },
        {
            "pergunta": "Qual é o maior golfinho de água doce no mundo?",
            "alternativas": ["A) Golfinho-de-risso", "B) Boto-cor-de-rosa", "C) Golfinho-chileno", "D) Golfinho-comum"],
            "correta": "B"
        },
        {
            "pergunta": "Qual é o maior país que abriga a Floresta Amazônica?",
            "alternativas": ["A) Peru", "B) Venezuela", "C) Colômbia", "D) Brasil"],
            "correta": "D"
        }

    ]

    indices_disponiveis = list(range(len(perguntas)))
    random.shuffle(indices_disponiveis)

    pontuacao = 0
    total_perguntas = len(perguntas)
    pergunta_atual = 0

    print("*"*50)
    print(" BEM-VINDO AO QUIZ EDUCATIVO: FLORESTA AMAZÔNICA")
    print("*"*50)

    # Laço principal do jogo
    while pergunta_atual < total_perguntas:
        idx = indices_disponiveis[pergunta_atual]
        item = perguntas[idx]
        
        print(f"\nPergunta {pergunta_atual + 1}: {item['pergunta']}")
        for alt in item['alternativas']:
            print(alt)

        # Validação da entrada do usuário
        resposta = ""
        while resposta not in ["A", "B", "C", "D"]:
            resposta = input("Sua resposta (A, B, C ou D): ").strip().upper()
            # Se a reposta for diferente de A, B, C, D
            if resposta not in ["A", "B", "C", "D"]:
                print("Por favor, escolha uma opção válida (A, B, C ou D).")

        # Condicional de feedback
        if resposta == item['correta']:
            print("\n Correto! Você está indo muito bem.") 
            pontuacao += 1
        else:
            print(f"\n Incorreto. A resposta certa era a letra {item['correta']}.")

        pergunta_atual += 1  #incrementa sempre

    exibir_ranking(pontuacao, total_perguntas)

# Se o arquivo for rodado diretamente, inicia o jogo
if __name__ == "__main__":
    jogar()