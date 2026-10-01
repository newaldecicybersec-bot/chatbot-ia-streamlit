# Chatbot com Streamlit + OpenAI
# Fluxo: campo de mensagem -> mostrar no chat -> IA responde -> mostrar resposta

import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Chatbot IA", page_icon="🤖")
st.title("🤖 Chatbot com IA")

# memória: histórico da conversa
if "historico" not in st.session_state:
    st.session_state.historico = []

# mostrar a conversa antiga
for msg in st.session_state.historico:
    st.chat_message(msg["role"]).write(msg["content"])

# campo de mensagem (input)
mensagem_usuario = st.chat_input("Digite sua mensagem...")

if mensagem_usuario:
    # mostrar a mensagem do usuário na conversa
    st.chat_message("user").write(mensagem_usuario)
    st.session_state.historico.append({"role": "user", "content": mensagem_usuario})

    # mandar a mensagem pra IA responder (com memória!)
    client = OpenAI()  # usa a variável de ambiente OPENAI_API_KEY
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente simpático e prestativo."}
        ] + st.session_state.historico,
    )
    resposta_ia = resposta.choices[0].message.content

    # mostrar a resposta da IA no chat
    st.chat_message("assistant").write(resposta_ia)
    st.session_state.historico.append({"role": "assistant", "content": resposta_ia})
