import json
import pandas as pd
import streamlit as st
from openai import OpenAI

# ========== CONFIGURAÇÃO ==========# 
client = OpenAI()
MODELO = "gpt-4o"

# ========== CARREGAR DADOS ==========# 
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))
perfil = json.load(open('./data/perfil_investidor.json'))

# ==========  MONTAR O CONTEXTO ==========# 
contexto = f""""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, {perfil['perfil_investidor']}, 
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ==========  MONTAR O CONTEXTO ==========# 

SYSTEM_PROMPT = """ Você é o José Finas, um educador financeiro amigável e didático.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplos práticos.

REGRAS:
- NUNCA recomende investimentos específicos, apenas explique como funciona;
- JAMAIS responda a perguntas fora do tema ensino de finanças pessoais.
  Quando ocorrer, responda lembrando o seu papel de educador financeiro;
- Use os dados fornecidos para dar exemplos personalizados;
- Linguagem simples, como se explicasse para um amigo;
- Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
- Sempre pergunte se o cliente entendeu;
- Responda de forma sucinta e direta, com no máximo 2 parágrafos se for preciso.
"""

# ==========  CHAMAR A OPENAI ==========# 
def perguntar(msg):
    response = client.chat.completions.create(
        model=MODELO,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f""""
            CONTEXTO DO CLIENTE: 
            {contexto}
            Pergunta: {msg}
            """}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content

# ==========  INTERFACE ==========# 
st.title("José Finas - Seu Educador Financeiro Virtual")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))