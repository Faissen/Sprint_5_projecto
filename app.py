import streamlit as st
import pandas as pd
import plotly.express as px

# Ler arquivo num dataframe
car_data = pd.read_csv('vehicles.csv')

# Cabeçalho
st.header('Análise Exploratória de Dados - Carros   Usados à Venda nos EUA')

# Botão para criar histograma
hist_button = st.button('Criar histograma')

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'A criar um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Botão para criar ráfico de dispersão
disp_button = st.button('Criar gráfico de dispersão')
if disp_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'A criar um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
