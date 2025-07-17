import os
import psycopg2
from psycopg2 import sql
from contrato import Vendas
import streamlit as st
from dotenv import load_dotenv

# carregar as variaveis de ambiente
load_dotenv()

#configuração do banco de dados PostgreSQL
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Função para salvar os dados no banco de dados
def salvar_dados(dados: Vendas):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )

        cursor = conn.cursor()

        # Inserir dados na tabela de vendas
        insert_query = sql.SQL(
            "INSERT INTO vendas (nome, email, data_hora, valor, quantidade, produto) VALUES (%s, %s, %s, %s, %s, %s)"
        )

        cursor.execute(insert_query, (
            dados.nome,
            dados.email,
            dados.data_hora,
            dados.valor,
            dados.quantidade,
            dados.produto.value
        ))
        conn.commit()
        cursor.close()
        conn.close()
        
    except Exception as e:
        st.error(f"Erro ao salvar no banco de dados {e}")