import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


st.set_page_config(layout='wide')
st.title('Analise por período de tempo')
df_data = st.session_state['data']
df_data['mes/ano'] = df_data['ano'].astype(str) + "-" +  df_data['mes'].astype(str).str.zfill(2)

dfmesano = df_data.groupby(by='mes/ano', as_index=False).agg({"Valor de Venda": "mean"})

precomesano = px.line(
    dfmesano,
    x='mes/ano',
    y='Valor de Venda',
    title='Evolução anual do preço do combustível',
    labels={
        'mes/ano': "período"
    }
)
precomesano.update_xaxes(title=None)
precomesano.update_layout({
    'title': {
        'xanchor': 'center',
        'x': 0.5
    }
})
st.plotly_chart(precomesano, use_container_width=True)

dfestadomesano = df_data.groupby(by=['mes/ano', 'Estado - Sigla'], as_index=False).agg({"Valor de Venda": "mean"})

# estadomesano = go.Figure()
# estadomesano.add_trace(
#     go.line(
#         x=dfestadomesano.loc[dfestadomesano['Estado - Sigla'].eq('MG'), 'mes/ano'],
#         y=dfestadomesano.loc[dfestadomesano['Estado - Sigla'].eq('MG'), 'Valor de Venda'],
#         name="MG"
#         )
# )

estadomesano = px.line(
    dfestadomesano,
    x='mes/ano',
    y='Valor de Venda',
    color='Estado - Sigla',
    title='Evolução anual do preço do combustível por estado'
)
estadomesano.update_xaxes(title=None)
estadomesano.update_layout({
    'title': {
        'xanchor': 'center',
        'x': 0.5
    }
})

st.plotly_chart(estadomesano, use_container_width=True)

dfestado = df_data.groupby(by='Estado - Sigla', as_index=False).agg({"Valor de Venda": "mean"})
estadovalor = px.bar(
    dfestado,
    x='Estado - Sigla',
    y='Valor de Venda',
    title='Preço médio por estado',
    color='Estado - Sigla',
    labels={
        'Estado - Sigla': "Estado"
    },
    text_auto='.4s'
)
estadovalor.update_layout(showlegend=False, title_x=0.5)
estadovalor.update_layout({
    'title': {
        'xanchor': 'center',
        'x': 0.5
    }
})
estadovalor.update_xaxes(title=None)

df_data['cidade/mes'] = df_data['Municipio'] + "/" +  df_data['Estado - Sigla']
dfcidade = df_data.groupby(by='cidade/mes', as_index=False).agg({"Valor de Venda": "mean"})
dfcidade = dfcidade.sort_values(by="Valor de Venda", ascending=False)

cidadevalor = px.bar(
    dfcidade[:10],
    y='cidade/mes',
    x='Valor de Venda',
    title='Cidades com os maiores preços médios',
    color='cidade/mes',
    orientation='h',
    labels={
        'cidade/mes': "Cidade"
    }
)
cidadevalor.update_layout(showlegend=False, title_x=0.5)
cidadevalor.update_layout({
    'title': {
        'xanchor': 'center',
        'x': 0.5
    }
})
cidadevalor.update_xaxes(range=[6,6.6])
cidadevalor.update_yaxes(title=None)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(estadovalor, use_container_width=True)

with col2:
    st.plotly_chart(cidadevalor, use_container_width=True)
    
dfbandeira = df_data.groupby(by='Bandeira', as_index=False).agg({"Valor de Venda": "mean"})
dfbandeira = dfbandeira.sort_values(by='Valor de Venda', ascending=False)
bandeiravalor = px.bar(
    dfbandeira,
    y='Bandeira',
    x='Valor de Venda',
    title='Bandeiras com os maiores preços médios',
    color='Bandeira',
    height=700
)
bandeiravalor.update_xaxes(range=[4,6.7])
bandeiravalor.update_layout(showlegend=False)

st.plotly_chart(bandeiravalor, use_container_width=True)