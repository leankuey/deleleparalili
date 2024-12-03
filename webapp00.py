import streamlit as st
st.title("Bem vinda")

st.header("Se você que esta lendo é Lilian Maria da Silva, esse site é para você")

st.subheader("Eu te amo meu amor")

st.write("Você é Lilian Maria da Silva?")

# Opções de resposta
resposta = st.radio("Escolha uma opção:", ["Sim", "Não"])

# Verificar a resposta inicial
if resposta == "Sim":
    st.markdown("## Eu te amo, meu amor! 💕")
    st.write("Bem-vinda a esse site que eu fiz para você como presente, espero que goste!")

    # Adicionar entrada de data
    data = st.date_input("Insira uma data especial:")

    # Verificar se a data é 7 de dezembro
    if data.month == 12 and data.day == 7:
        st.markdown(
            """
            ## Meu amor, esse é um dia muito especial para o homem misterioso que criou esse site.  
            O dia que nasceu o ser mais perfeito nesse mundo: **o dia do seu nascimento**.  
            Eu agradeço muito a Deus por ter você na minha vida e por ter seu amor para mim.  
            O presente quem está dando sou eu, mas como uma forma de te agradecer.  
            **Obrigado por me salvar, me mudar e me amar.**
            """
        )
    else:
        st.markdown("## Eu não ligo para essa data. 🙄")
elif resposta == "Não":
    st.markdown("## Vá embora! 😡")
    st.stop()

st.write("Você aceita me amar para todo o sempre?")
agree = st.checkbox("Eu aceito")

if agree:
    st.write("Eu te amo muito e para todo o sempre meu amor")
