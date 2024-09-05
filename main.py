import streamlit as st
from st_paywall import add_auth

# Esconder o ícone do GitHub
hide_github_icon = """
    <style>
    .stApp > header {visibility: hidden;}
    </style>
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)

st.image("top banner.png")

add_auth(required=True)

bazin_page = st.Page(
    page="views/bazin_page.py",
    title="Método Bazin",
    icon=":material/chevron_right:",
    default=True,
)
graham_page = st.Page(
    page="views/graham_page.py",
    title="Método Graham",
    icon=":material/chevron_right:",
    default=False
)
balanceamento_page = st.Page(
    page="views/balanceamento.py",
    title="Calculadora rebalanceamento",
    icon=":material/calculate:",
    default=False
)
lynch_page = st.Page(
    page="views/lynch.py",
    title="Método Peter Lynch",
    icon=":material/chevron_right:",
    default=False
)
mayer_page = st.Page(
    page="views/mayer.py",
    title="Múltiplo de Mayer (Cripto)",
    icon=":material/currency_bitcoin:",
    default=False
)
gordon_page = st.Page(
    page="views/gordon.py",
    title="Método Gordon (FIIS)",
    icon=":material/chevron_right:"
)
contato_page = st.Page(
    page="views/contato.py",
    title="Entre em contato",
    icon=":material/contact_support:"
)
privacidade_page = st.Page(
    page="views/privacidade.py",
    title="Política de Privacidade",
    icon=":material/policy:"
)


pg = st.navigation({"Métodos de valuation":[bazin_page,graham_page,lynch_page,mayer_page,gordon_page],
                    "Rebalanceamento de carteira": [balanceamento_page],"Outro": [contato_page, privacidade_page] })

st.logo("assets/logo.png")

st.sidebar.text("Smart Strategy Premium")

pg.run()