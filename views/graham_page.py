import yfinance as yf
import streamlit as st
import math
import streamlit_shadcn_ui as ui

def get_graham(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        price = stock.fast_info['last_price']
        eps = info['trailingEps']
        book = info['bookValue']
        if eps > 0 and book > 0:
            graham = math.sqrt(22.5*eps*book)
        else:
            graham = 0
        return round(graham,2), round(price,2)
    except Exception:
        return 0

st.title("Calculadora Graham")

st.write("""**A calculadora Graham estima o valor intrínseco de uma empresa utilizando a fórmula de Graham,
 que multiplica o Lucro por Ação (LPA) pelo Valor Patrimonial por Ação (VPA) e, em seguida, calcula a raiz quadrada do
  produto dessa multiplicação com a constante de Graham, que é 22,5. O resultado fornece uma estimativa do valor justo
   da empresa. No entanto, é fundamental utilizar esse método como parte de uma análise fundamentalista mais ampla, não
    como a única base para decisões de investimento.**""")

col3, col4= st.columns(2, gap="large", vertical_alignment="top")

with col3:
    st.text("Como usar:")
    st.video("Como usar a Calculadora Graham.mp4")


st.text("Selecione um país:")

country_selection = ui.select("Selecione um país: ", options=["BR","US"], key=2)

col1, col2 = st.columns(2, gap="medium", vertical_alignment="top")

with col1:
    st.text("")
    st.text("")
    ticker = st.text_input("Ticker: ").upper()

    if ticker:
        if country_selection == "BR":
            ticker = ticker + ".SA"
        try:
            graham, price = get_graham(ticker)
            desconto_graham = ((graham-price)/graham)*100

            if country_selection == "BR":
                st.write(f"""Preço atual: **R${price}**""")
                st.write(f"""Preço Teto Graham: **R${graham}**""")
                if desconto_graham > 0:
                    st.write(f"""Essa ação está com desconto de **{round(desconto_graham,2)}%** segundo o método Graham.""")
                elif graham == 0:
                    st.write("""Não há preço teto Graham para essa ação.""")
                elif desconto_graham < 0:
                    st.write(f"""Essa ação está **{round((desconto_graham*(-1)),2)}%** acima do preço teto Graham.""")
                elif desconto_graham == 0:
                    st.write("""A cotação atual é igual ao preço teto.""")

            elif country_selection == "US":
                st.write(f"""Preço atual: **U${price}**""")
                st.write(f"""Preço Teto Graham: **U${graham}**""")
                if desconto_graham > 0:
                    st.write(f"""Essa ação está com desconto de **{round(desconto_graham, 2)}%** segundo o método Graham.""")
                elif graham == 0:
                    st.write("""Não há preço teto Graham para essa ação.""")
                elif desconto_graham < 0:
                    st.write(f"""Essa ação está **{round((desconto_graham * (-1)), 2)}%** acima do preço teto Graham.""")
                elif desconto_graham == 0:
                    st.write("""A cotação atual é igual ao preço teto.""")

        except Exception:
            st.write("""Digite um ticker válido.""")

