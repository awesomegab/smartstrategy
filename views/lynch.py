import yfinance as yf
import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd

def get_cagr(ticker):

        stock = yf.Ticker(ticker)
        history = stock.history(period="5y")
        info = stock.info
        start_price = history.iloc[0,3]
        end_price = history.iloc[-1,3]
        cagr = ((end_price/start_price)**(1/5)-1)*100
        pl = info['trailingPE']
        dy = info['trailingAnnualDividendYield']*100
        return cagr


def get_lynch(ticker, cagr):

        stock = yf.Ticker(ticker)
        info = stock.info
        pl = info['trailingPE']
        dy = info['trailingAnnualDividendYield']*100
        lynch = (cagr+dy)/pl
        return round(lynch,2)




st.title("Calculadora Peter Lynch")

st.write("""**O método Peter Lynch combina a taxa de crescimento anual composta (CAGR) com o Dividend Yield (DY) e 
    divide o resultado pelo preço/lucro (P/L) da empresa. Isso permite comparar a taxa de crescimento com a lucratividade
     da empresa, incorporando também o impacto dos dividendos, oferecendo uma visão mais equilibrada do potencial
      de investimento.**""")

col3, col4= st.columns(2, gap="large", vertical_alignment="top")

with col3:
    st.text("Como usar:")
    st.video("Como usar a Calculadora Peter Lynch.mp4")

st.text("Selecione um país: ")

country_selection = ui.select("Escolha um país", options=["BR","US"], key=1)

col1, col2 = st.columns(2, gap="medium", vertical_alignment="top")

with col1:
    try:
        st.text("")
        st.text("")
        ticker = st.text_input("Ticker: ").upper()
        if country_selection == "BR" and ticker:
            ticker = ticker+".SA"
    except Exception:
        pass
    if ticker:
        try:
            cagr = get_cagr(ticker)
            lynch = get_lynch(ticker, cagr)
            st.write(f""" Resultado Lynch: **{lynch}**""")
            st.text("")
            st.subheader("Legenda:")
            st.write("""Resultado menor que 1: **Ruim** """)
            st.write("""Resultado entre 1 e 2: **Aceitável**""")
            st.write("""Resultado maior que 2: **Excelente**""")
        except Exception:
            st.write(f"""Não há valor Lynch para essa ação.""")
