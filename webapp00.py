import streamlit as st
st.title("Bem vinda")

st.header("Se você que esta lendo é Lilian Maria da Silva, esse site é para você")

st.subheader("Eu te amo meu amor")



st.write("Você é Lilian Maria da Silva?")

resposta = st.radio("Escolha uma opção:", ["Sim", "Não"])

if resposta == "Sim":
    st.markdown("## Eu te amo, meu amor! 💕")
    st.write("Bem-vinda a esse site que eu fiz para você como presente, espero que goste!")
elif resposta == "Não":
    st.markdown("## Vá embora! 😡")
