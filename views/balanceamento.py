import streamlit as st

def soma_partes(lista):
    soma = 0
    for i in lista:
        i = float(i)
        soma += i
    return soma

def calculo(lista, valor, soma):
    constante = valor/soma
    partes_proporcionais = []
    for i in lista:
        i = float(i)
        result = i*constante
        partes_proporcionais.append(round(result))
    return partes_proporcionais


st.title("Rebalanceamento de carteira")

col3, col4= st.columns(2, gap="large", vertical_alignment="top")

with col3:
    st.text("Como usar:")
    st.video("Como usar a Calculadora de Rebalanceamento.mp4")

st.write('''**USE "." para separar casas decimais. Ex.: 25.448**''')


colu1, colu2 = st.columns(2, gap="small", vertical_alignment="top")

with colu1:
    try:
        patrimonio = float(st.text_input("Patrimônio: "))
    except Exception:
        pass

with colu2:
    try:
        aporte = float(st.text_input("Aporte: "))
    except Exception:
        pass

col1, col2 = st.columns(2, gap="small", vertical_alignment="top")

with col1:

    try:
        por_a = float(st.text_input("% ideal Ações: "))/100
        por_f = float(st.text_input("% ideal Fiis: "))/100
        por_c = float(st.text_input("% ideal Caixa: "))/100
        por_u = float(st.text_input("% ideal USA: "))/100
        por_cry = float(st.text_input("% ideal Cripto: "))/100
    except Exception:
        pass
    try:
        v_a = (patrimonio+aporte)*por_a
        v_f = (patrimonio+aporte)*por_f
        v_c = (patrimonio+aporte)*por_c
        v_u = (patrimonio+aporte)*por_u
        v_cry = (patrimonio+aporte)*por_cry
    except Exception:
        pass

with col2:

    try:
        ok = por_cry+2
        carteira_acoes = float(st.text_input("Patrimônio ações: "))
        carteira_fiis = float(st.text_input("Patrimônio fiis: "))
        carteira_caixa = float(st.text_input("Patrimônio caixa: "))
        carteira_usa = float(st.text_input("Patrimônio USA: "))
        carteira_crypto = float(st.text_input("Patrimônio cripto: "))
    except Exception:
        pass
    try:
        lista = [v_a-carteira_acoes,v_f-carteira_fiis,v_c-carteira_caixa,v_u-carteira_usa,v_cry-carteira_crypto]
    except Exception:
        pass

try:
        ok = carteira_crypto + 2
        st.subheader("Ajuste com venda: ")
        st.write(f"""Ajuste ações: **{round(lista[0],2)}**""")
        st.write(f"""Ajuste fiis: **{round(lista[1],2)}**""")
        st.write(f"""Ajuste caixa: **{round(lista[2],2)}**""")
        st.write(f"""Ajuste USA: **{round(lista[3],2)}**""")
        st.write(f"""Ajuste cripto: **{round(lista[4],2)}**""")
except Exception:
        pass
try:
        faltando = []

        for i in lista:
            if i > 0:
                faltando.append(i)
            else:
                faltando.append(0)

        soma = soma_partes(faltando)
        proporcional = calculo(faltando, aporte, soma)
        st.subheader("Ajuste apenas com aporte: ")
        st.write(f"""Aporte ações: **{proporcional[0]}**""")
        st.write(f"""Aporte fiis: **{proporcional[1]}**""")
        st.write(f"""Aporte caixa: **{proporcional[2]}**""")
        st.write(f"""Aporte USA: **{proporcional[3]}**""")
        st.write(f"""Aporte cripto: **{proporcional[4]}**""")
except Exception:
        pass

