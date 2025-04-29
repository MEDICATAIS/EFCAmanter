import streamlit as st

st.set_page_config(page_title="Escala EFCA", layout="centered")

opcoes = {"Nunca": 1, "Raras vezes": 2, "Às vezes": 3, "Quase sempre": 4, "Sempre": 5}

# Define as perguntas
perguntas = {
    2: "Acalmo minhas emoções com comida.",
    4: "Tenho o hábito de beliscar (pequenas ingestões entre refeições principais).",
    7: "Belisco entre refeições por ansiedade, tédio, solidão, medo, raiva, tristeza ou cansaço.",
    10: "Como nos momentos em que estou aborrecido, ansioso, nervoso, triste, cansado, zangado ou sozinho.",
    1: "Como até me sentir muito cheio.",
    3: "Peço mais comida quando termino meu prato.",
    6: "Costumo comer mais de um prato nas refeições principais.",
    5: "Quando começo a comer algo que gosto muito, tenho dificuldade em parar.",
    8: "Sinto-me tentado a comer quando vejo/cheiro comida de que gosto e/ou passo em frente a uma padaria, pizzaria ou fast food.",
    12: "Quando estou diante de algo que gosto muito, mesmo sem fome, acabo por comê-la.",
    14: "Quando como algo que gosto, finalizo toda a porção.",
    9: "Tomo café da manhã todos os dias (pontuação invertida).",
    11: "Pulo alguma ou pelo menos uma refeição principal.",
    16: "Passo mais de 5h do dia sem comer.",
    13: "Como muita comida em pouco tempo.",
    15: "Quando como algo que gosto muito, como muito rápido."
}

respostas = {}
st.title("Escala de Fenótipos de Comportamento Alimentar (EFCA)")
st.write("Responda todas as questões abaixo:")

for idx in sorted(perguntas.keys()):
    escolha = st.radio(perguntas[idx], list(opcoes.keys()), key=idx)
    valor = opcoes[escolha]
    if idx == 9:  # pontuação invertida
        valor = 6 - valor
    respostas[idx] = valor

# Funções para calcular resultados
def calcular_resultados(respostas):
    resultados = {}
    resultados['Comer Emocional'] = sum(respostas[i] for i in [2,4,7,10])
    resultados['Hiperfagia'] = sum(respostas[i] for i in [1,3,6])
    resultados['Comer Hedônico'] = sum(respostas[i] for i in [5,8,12,14])
    resultados['Comer Desorganizado'] = sum(respostas[i] for i in [9,11,16])
    resultados['Comer Compulsivo'] = sum(respostas[i] for i in [13,15])
    return resultados

def classificar(score, faixa):
    if score <= faixa[0]:
        return "Baixo"
    elif faixa[0] < score <= faixa[1]:
        return "Médio"
    else:
        return "Alto"

if st.button("Ver Resultado"):
    resultados = calcular_resultados(respostas)
    st.subheader("Resultados:")
    classificacoes = {
        'Comer Emocional': (8,12),
        'Hiperfagia': (5,8),
        'Comer Hedônico': (11,14),
        'Comer Desorganizado': (4,6),
        'Comer Compulsivo': (3,6)
    }
    for fenotipo, score in resultados.items():
        faixa = classificacoes[fenotipo]
        categoria = classificar(score, faixa)
        st.write(f"**{fenotipo}:** {score} pontos - {categoria}")
