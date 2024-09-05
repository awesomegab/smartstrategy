import yfinance as yf
import streamlit as st
import streamlit_shadcn_ui as ui

def get_bazin(ticker):
    try:
        stock = yf.Ticker(ticker)
        history = stock.history(start='2019-01-01', end='2024-01-01')
        price = stock.fast_info['last_price']
        dividends = history['Dividends'].sum()
        bazin = (dividends/5)/0.06
        return round(bazin,2), round(price,2)
    except Exception:
        return 0, 0

st.title("Calculadora Bazin")

st.write("""**A calculadora Bazin calcula o preço justo de uma ação somando os dividendos pagos nos últimos 5 anos
 completos, excluindo o ano atual. Em seguida, divide essa soma por 5 para obter a média anual dos dividendos. O valor
  resultante é então dividido por 6%, que é a taxa mínima de retorno recomendada por Bazin. É importante ressaltar que
   esse método é uma ferramenta complementar e deve ser utilizado em conjunto com uma análise fundamentalista
    abrangente, não sendo recomendado como única base para decisões de investimento.**""")

col3, col4= st.columns(2, gap="large", vertical_alignment="top")

with col3:
    st.text("Como usar:")
    st.video("Como usar a Calculadora Bazin.mp4")


st.text("")
st.text("Selecione um país:")

country_selection = ui.select("Escolha um país", options=["BR","US"], key=1)

col1, col2 = st.columns(2, gap="medium", vertical_alignment="top")

with col1:
    st.text("")
    ticker = st.text_input("Ticker: ").upper()

    if ticker:
        if country_selection == "BR":
            ticker = ticker + ".SA"
        try:
            bazin, price = get_bazin(ticker)
            desconto_bazin = ((bazin-price)/bazin)*100

            if country_selection == "BR":
                st.write(f"""Preço atual: **R${price}**""")
                st.write(f"""Preço Teto Bazin: **R${bazin}**""")
                if desconto_bazin > 0:
                    st.write(f"""Essa ação está com desconto de **{round(desconto_bazin,2)}%** segundo o método Bazin.""")
                elif bazin == 0:
                    st.write("""Não há preço teto Bazin para essa ação.""")
                elif desconto_bazin < 0:
                    st.write(f"""Essa ação está **{round((desconto_bazin*(-1)),2)}%** acima do preço teto Bazin.""")
                elif desconto_bazin == 0:
                    st.write("""A cotação atual é igual ao preço teto.""")

            elif country_selection == "US":
                st.write(f"""Preço atual: **U${price}**""")
                st.write(f"""Preço Teto Bazin: **U${bazin}**""")
                if desconto_bazin > 0:
                    st.write(f"""Essa ação está com desconto de **{round(desconto_bazin, 2)}%** segundo o método Bazin.""")
                elif bazin == 0:
                    st.write("""Não há preço teto Bazin para essa ação.""")
                elif desconto_bazin < 0:
                    st.write(f"""Essa ação está **{round((desconto_bazin * (-1)), 2)}%** acima do preço teto Bazin.""")
                elif desconto_bazin == 0:
                    st.write("""A cotação atual é igual ao preço teto.""")

        except Exception:
            st.write("""Digite um ticker com pelo menos 5 anos desde o IPO.""")



