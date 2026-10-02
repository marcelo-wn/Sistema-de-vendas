# PASSO-A-PASSO

# 1. Importar bibliotecas
import pandas as pd
import streamlit as st
import plotly.express as px

# carregar base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

# 2. Título - sistema de vendas
st.write("# Sistema de vendas")

# 3. Seção - Cadastrar Vendas
st.sidebar.write("## Cadastrar vendas")

    # campo Data
data = st.sidebar.date_input("Data")
 
    # campo Vendedor
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])

    # campo produto
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])   

    # campo Quantidade
quantidade = st.sidebar.number_input("Quantidade")

    # campo Valor
valor = st.sidebar.number_input("Valor")

    # campo Cadastrar Venda > + Venda na tabela > atualizar Dashboard
botao_cadastrar = st.sidebar.button("Cadastrar venda")

        # lógica de cadastro
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas)
    tabela_vendas.loc[ultima_linha]=nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda cadastrada")

# 4. Seção - Vendas Cadastradas
st.write("## Vendas cadastradas")

    # tabela com as vendas
st.dataframe(tabela_vendas)

# 5. Seção - Dashboard
st.write("## Dashboard")

    # card/metrica > faturamento total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento total", f"R$ {faturamento}")


    # gráfico de barra/coluna > venda por vendedor
grafico = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico)

    # gráfico de pizza > venda por produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor")
st.plotly_chart(grafico2)

