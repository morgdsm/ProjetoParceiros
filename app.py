import streamlit as st
import pandas as pd
from datetime import datetime
from models.parceiros import adicionar_parceiro, listar_parceiros
from models.tarefas import adicionar_tarefa, listar_tarefas, contar_tarefas_por_status

# Título principal
st.title('Sistema de Gestão de Parceiros e Tarefas')

# Seção 1: Cadastro de Parceiros
st.header('Cadastro de Parceiro')
nome = st.text_input('Nome do parceiro')
email = st.text_input('Email')
telefone = st.text_input('Telefone')

if st.button('Cadastrar parceiro'):
    if nome:
        adicionar_parceiro(nome, email, telefone)
        st.success('Parceiro cadastrado com sucesso!')
    else:
        st.error('O nome é obrigatório.')

# Seção 2: Lista de Parceiros
st.subheader('Parceiros Cadastrados')
parceiros = listar_parceiros()
df_parceiros = pd.DataFrame(parceiros, columns=['ID', 'Nome', 'Email', 'Telefone'])
st.dataframe(df_parceiros)

# Seção 3: Cadastro de Tarefa
st.header('Cadastro de Tarefa')
descricao = st.text_input('Descrição da tarefa')
status = st.selectbox('Status', ['Pendente', 'Em andamento', 'Concluída'])
prazo = st.date_input('Prazo final', min_value=datetime.today())

# Carregar os IDs dos parceiros para selecionar
parceiros_dict = {f"{p[1]} (ID {p[0]})": p[0] for p in parceiros}
parceiro_nome_id = st.selectbox('Selecione o parceiro', list(parceiros_dict.keys()))
parceiro_id = parceiros_dict[parceiro_nome_id]

if st.button('Cadastrar tarefa'):
    if descricao:
        adicionar_tarefa(descricao, status, prazo, parceiro_id)
        st.success('Tarefa cadastrada com sucesso!')
    else:
        st.error('A descrição é obrigatória.')

# Seção 4: Lista de Tarefas
st.subheader('Tarefas Cadastradas')
tarefas = listar_tarefas()
df_tarefas = pd.DataFrame(tarefas, columns=['ID', 'Descrição', 'Status', 'Prazo', 'Parceiro'])
st.dataframe(df_tarefas)

# Seção 5: Dashboard
st.header('Dashboard de Tarefas')
dados_dashboard = contar_tarefas_por_status()
df_dashboard = pd.DataFrame(dados_dashboard, columns=['Status', 'Quantidade'])
st.bar_chart(df_dashboard.set_index('Status'))
