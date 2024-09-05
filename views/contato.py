import streamlit as st

col1, col2= st.columns(2,gap="small", vertical_alignment="top")

with col1:
    st.title("Contato")
    st.write("""**Dúvidas? Sugestões? Entre em contato!**""")

    st.subheader("Email:")
    st.text("")
    st.write("""smartstrategy.py@gmail.com""")

    st.subheader("Instagram:")
    st.text("")
    st.write("""https://www.instagram.com/smartstrategy.py/""")

    st.subheader("Youtube:")
    st.text("")
    st.write("""https://www.youtube.com/channel/UCHkZ_ICjB4g5nTqHUCNazKA""")


st.subheader("Disclaimer:")
st.write("""**O conteúdo deste site não constitui uma recomendação de investimento. As ferramentas apresentadas têm como
     objetivo ajudar a filtrar opções e fornecer uma base para avaliar se está fazendo um bom negócio.**""")


