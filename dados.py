import pandas as pd

# Lista de perguntas com opções e respostas
perguntas = [
    {
        "pergunta": "Como era o nome da raça extraterrestre na qual o \"Outro\" era líder?",
        "op": ["Patonianos", "Molóides", "Chitauri", "Beyonders"],
        "res": 2
    },
    {
        "pergunta": "Qual é o nome de reino fictício onde Loki e o Tesseract retornam após o ataque fracassado à Terra?",
        "op": ["Midgard", "Alfheim", "Vanaheim", "Asgard"],
        "res": 3
    },
    {
        "pergunta": "Qual o nome de elemento químico necessário para estabilizar o poder de Tesseract?",
        "op": ["Praseodímio", "Ítrio", "Neodímio", "Irídio"],
        "res": 3
    },
    {
        "pergunta": "Em qual planeta se localizava a joia da alma?",
        "op": ["Vormir", "Asgard", "Terra", "Xandar"],
        "res": 0
    },
    {
        "pergunta": "Quem traz Tony Stark e Nebulosa de volta a Terra?",
        "op": ["Rato", "Guardiões da Galáxia", "Vingadores", "Capitã Marvel"],
        "res": 3
    },
    {
        "pergunta": "Como as joias do infinito são recuperadas?",
        "op": ["Indo até o Thanos", "Viagem no tempo", "Produzindo novas"],
        "res": 1
    },
    {
        "pergunta": "Como o Homem Formiga consegue voltar do reino quântico?",
        "op": ["Rato", "Vingadores", "Guardiões da Galáxia", "Capitã Marvel"],
        "res": 0
    },
    {
        "pergunta": "No filme, Vingadores: Ultimato, qual dos heróis usaram a nova manopla?",
        "op": ["Hulk e Capitão América", "Homem de Ferro e Capitão América", "Hulk e Homem de Ferro", "Homem de Ferro e Homem formiga"],
        "res": 2
    },
    {
        "pergunta": "Em Vingadores: Guerra Infinita, qual é a motivação alegada pelo vilão, Thanos, para seus atos?",
        "op": ["Acabar com o universo", "Vingança", "Equilibrar o universo", "Derrotar seus inimigos"],
        "res": 2
    },
    {
        "pergunta": "Qual das 6 joias do infinito foi acoplada na testa do personagem Visão?",
        "op": ["Espaço (azul)", "Mente (amarela)", "Alma (laranja)", "Poder (roxa)"],
        "res": 1
    },
    {
        "pergunta": "Ultron vai até a costa africana em busca do ferro mais poderoso da terra para derrotar a humanidade, qual ferro era este?",
        "op": ["Vibranium", "Tungstênio", "Titânio", "Adamantium"],
        "res": 0
    },
    {
        "pergunta": "Por que Mercúrio não aparece no filme depois de Era de Ultron?",
        "op": ["Porque ele ficou preso no espaço", "Porque ele se tornou o rei de mercúrio", "Porque ele desapareceu da galáxia", "Porque ele morreu"],
        "res": 3
    }
]

# Cria um DataFrame
df = pd.DataFrame(perguntas)

# Salva em um arquivo Excel
df.to_excel("questions.xlsx", index=False)
print("Perguntas inseridas no arquivo questions.xlsx")
