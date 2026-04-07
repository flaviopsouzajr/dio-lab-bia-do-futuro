# 💰 José Finas — Educador Financeiro Virtual

Um agente de IA que ensina finanças pessoais de forma simples, personalizada e sem enrolação.

---

## O Problema

Mais de 60% dos brasileiros não entendem o básico de investimentos. A maioria quer aprender, mas se perde em conteúdos genéricos que não fazem sentido para a própria realidade.

## A Solução

O **José Finas** é um educador financeiro virtual que usa os **seus próprios dados** como exemplo. Nada de teoria solta — ele olha para o seu extrato, seu perfil e seus objetivos, e explica de forma concreta e acessível.

> ⚠️ O José Finas **educa**, não aconselha. Ele nunca recomenda onde investir — apenas explica como cada produto funciona e o que você precisa saber para decidir com autonomia.

---

## Como Funciona

```
Cliente → Interface Streamlit → LLM (GPT-4o) → Resposta personalizada
                                      ↑
                          Base de Conhecimento (CSV + JSON)
```

O agente carrega automaticamente o perfil do cliente, histórico de transações, atendimentos anteriores e produtos disponíveis — e usa tudo isso como contexto para responder.

---

## Base de Conhecimento

| Arquivo | O que contém |
|---|---|
| `data/perfil_investidor.json` | Nome, renda, objetivos e perfil de risco |
| `data/transacoes.csv` | Histórico de gastos por categoria |
| `data/historico_atendimento.csv` | Atendimentos anteriores |
| `data/produtos_financeiros.json` | Produtos disponíveis com risco e rentabilidade |

---

## Exemplos de Interação

**"O que é CDI?"**
> "CDI é a taxa que os bancos usam para emprestar dinheiro entre si. Quando um investimento rende '102% do CDI', significa que ele paga um pouco mais do que essa taxa. Faz sentido?"

**"Onde estou gastando mais?"**
> "Em outubro, sua maior despesa foi moradia (R$ 1.380), seguida de alimentação (R$ 570). Juntas, representam cerca de 79% dos seus gastos. Quer entender como organizar isso?"

**"Onde devo investir meu dinheiro?"**
> "Como educador financeiro, não posso recomendar onde investir — mas posso explicar como cada produto funciona para você decidir com mais segurança. Tem algum em específico que queira entender?"

---

## Como Rodar

```bash
# Instalar dependências
pip install streamlit pandas openai

# Configurar a chave da API
echo "OPENAI_API_KEY=sua_chave_aqui" > .env

# Rodar
streamlit run src/app.py
```

---

## Documentação

| Arquivo | Conteúdo |
|---|---|
| `docs/01-documentacao-agente.md` | Caso de uso, persona e arquitetura |
| `docs/02-base-conhecimento.md` | Estratégia de dados e contexto |
| `docs/03-prompts.md` | System prompt e edge cases |
| `docs/04-metricas.md` | Testes e avaliação de qualidade |
| `docs/05-pitch.md` | Roteiro do pitch de apresentação |

---

## Stack

- **Interface:** Streamlit  
- **LLM:** GPT-4o via OpenAI API  
- **Dados:** CSV e JSON mockados  
- **Linguagem:** Python
