# Passo a passo de execução


## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit)
```

## Código Completo

Todo o código fonte está no arquivo `app.py`

## Como Rodar

```bash
# Instalar dependências
pip install streamlit pandas openai

# Garantir que a API KEY da OpenAi está configurada
- Criar arquivo `.env` na raiz do projeto 
- Adicionar: OPENAI_API_KEY=XXXXXXXXXXX

# Rodar a aplicação
streamlit run ./src/app.py
```
