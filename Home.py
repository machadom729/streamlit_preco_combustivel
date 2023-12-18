import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title='Home')
df_data = pd.read_parquet('ca-2021-2023.parquet')

df_data['Valor de Venda'] = df_data['Valor de Venda'].str.replace(',', '.', regex=True)
df_data['Valor de Venda'] = df_data['Valor de Venda'].astype(float)

if 'data' not in st.session_state:
    st.session_state['data'] = df_data

st.title('Analise do preço de combustível')
st.text("""
        Em cumprimento às determinações da Lei do Petróleo (Lei nº 9478/1997, artigo 8º), 
        a ANP acompanha os preços praticados por revendedores de combustíveis automotivos
        e de gás liquefeito de petróleo envasilhado em botijões de 13 quilos (GLP P13), 
        por meio de uma pesquisa semanal de preços realizada por empresa contratada. 
        """)
