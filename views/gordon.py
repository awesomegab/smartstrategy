import yfinance as yf
import streamlit as st

def get_dividend_price(ticker):
    stock = yf.Ticker(ticker)
    price = stock.fast_info['last_price']
    history = stock.history(period="1y")
    dividends = history['Dividends'].sum()
    return round(dividends,2), round(price,2)

def teto_fiis(dividendo, tesouro):
    plus = 3
    taxa_desconto = (plus+tesouro)/100
    resultado = round(dividendo/taxa_desconto,2)
    return resultado

st.title("Calculadora Gordon")
st.write("""**A calculadora Gordon oferece uma forma rápida de estimar um preço teto para um fundo imobiliário com base
 nos dividendos e numa taxa de desconto que reflete o retorno livre de risco e o risco adicional. No entanto, para tomar
  uma decisão de investimento sólida, é essencial realizar uma análise mais abrangente, considerando todos os fatores
   que podem impactar o valor do investimento no longo prazo.**""")

st.text("Como usar: ")

col1, col2 = st.columns(2, gap="large", vertical_alignment="top")

with col1:
    st.video("Como usar a Calculadora Gordon.mp4")
    try:
        ticker = st.text_input("Ticker").upper()
        ticker = ticker+".SA"
        st.write('''**USE "." para separar casas decimais. Ex.: 25.448**''')
        tesouro = float(st.text_input("Taxa Tesouro IPCA (Disponível no site do tesouro direto)"))
    except Exception:
        st.write("""Digite o ticker de um fundo imobiliário e a taxa do tesouro IPCA.""")
        pass
    try:
        dividendos, preço = get_dividend_price(ticker)
        resultado = teto_fiis(dividendos, tesouro)
        desconto = ((resultado-preço)/resultado)*100
        st.write(f"""Preço atual: **R${preço}**.""")
        st.write(f"""Preço Gordon: **R${resultado}**.""")
        if desconto > 0:
            st.write(f"""Este fundo está com desconto de **{round(desconto,2)}%** segundo o modelo Gordon.""")
        else:
            st.write(f"""Esse fundo está **{round(desconto,2)}%** acima do preço teto segundo o modelo Gordon.""")

    except Exception:
        pass





