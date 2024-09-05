import yfinance as yf
import streamlit as st
import streamlit_shadcn_ui as ui

def get_mayer(coin):
    crypto = yf.Ticker(coin)
    info = crypto.fast_info
    day200 = info['twoHundredDayAverage']
    price = info['lastPrice']
    mayer = price/day200
    return round(mayer,2)


st.title("Múltiplo de Mayer")

st.write(f"""**O Múltiplo de Mayer é um indicador utilizado principalmente no mercado de criptomoedas, especificamente
 para avaliar o preço do Bitcoin em relação à sua média móvel de 200 dias. Esse múltiplo é uma ferramenta simples, mas
  poderosa, para entender se o Bitcoin está supervalorizado ou subvalorizado em determinado momento.**""")

col3, col4= st.columns(2, gap="large", vertical_alignment="top")

with col3:
    st.text("Como usar:")
    st.video("Como usar o Múltiplo de Mayer.mp4")

st.text("Selecione uma criptomoeda: ")

coin_select = ui.select("Escolha uma cripto",
                        options=["Bitcoin","Ethereum","XRP","Solana","BNB","Dogecoin","Cardano", "Polygon","Avalanche","Tron"], key=1)

try:
    if coin_select == "Bitcoin":
        coin = "BTC-USD"
        MM = get_mayer(coin)
        st.write(f"""Múltiplo de Mayer atual do Bitcoin é: **{MM}**""")
    elif coin_select =="Ethereum":
        coin = "ETH-USD"
        MM = get_mayer(coin)
        st.write(f"""Múltiplo de Mayer atual do Ethereum é: **{MM}**""")
    elif coin_select =="XRP":
        coin = "XRP-USD"
        MM = get_mayer(coin)
        st.write(f"""Múltiplo de Mayer atual do XRP é: **{MM}**""")
    elif coin_select =="Solana":
        coin = "SOL-USD"
        MM = get_mayer(coin)
        st.write(f"""Múltiplo de Mayer atual do Solana é: **{MM}**""")
    elif coin_select =="BNB":
        coin = "BNB-USD"
        MM = get_mayer(coin)
        st.write(f"""Múltiplo de Mayer atual do BNB é: **{MM}**""")
    elif coin_select =="Dogecoin":
        coin = "DOGE-USD"
        MM = get_mayer(coin)
        st.write(f"""Múltiplo de Mayer atual do Dogecoin é: **{MM}**""")
    elif coin_select =="Cardano":
        coin = "ADA-USD"
        MM = get_mayer(coin)
        st.write(f"""Múltiplo de Mayer atual do Cardano é: **{MM}**""")
    elif coin_select =="Polygon":
        coin = "MATIC-USD"
        MM = get_mayer(coin)
        st.write(f"""Múltiplo de Mayer atual do Polygon é: **{MM}**""")
    elif coin_select =="Avalanche":
        coin = "AVAX-USD"
        MM = get_mayer(coin)
        st.write(f"""Múltiplo de Mayer atual do Avalanche é: **{MM}**""")
    elif coin_select =="Tron":
        coin = "TRX-USD"
        MM = get_mayer(coin)
        st.write(f"""Múltiplo de Mayer atual do Tron é: **{MM}**""")
except Exception:
    st.text("Um erro ocorreu, tente novamente.")

st.subheader("Legenda:")
st.write("""**Múltiplo de Mayer menor que 1:** Abaixo da média móvel, pode estar descontado.""")
st.write("""**Múltiplo de Mayer maior que 1:** Acima da média móvel, pode estar supervalorizado.""")
st.write("""**Múltiplo de Mayer maior que 2.4:** Historicamente, representa um pico de preço.""")


