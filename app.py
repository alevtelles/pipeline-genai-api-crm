import streamlit as st
from datetime import datetime, time
from contrato import Vendas, ProdutoEnum
from pydantic import ValidationError
from database import salvar_dados

def main():

    st.title("Optimus Sistema de CRM & Vendas")
    st.write("Bem-vindo ao nosso sistema de CRM e Vendas! Aqui, você pode gerenciar suas vendas e clientes de forma eficiente.")
    st.divider()

    # Linha 1: Nome e Email lado a lado
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome do vendedor")
    with col2:
        email = st.text_input("Digite o e-mail do vendedor")

    # Linha 2: Data e Hora
    col3, col4 = st.columns(2)
    with col3:
        data = st.date_input("Data da venda", datetime.now())
    with col4:
        hora = st.time_input("Hora da compra", value=time(9, 0))

    # Linha 3: Valor, Quantidade e Produto
    col5, col6, col7 = st.columns(3)
    with col5:
        produtos_disponiveis = [
            ProdutoEnum.produto1,
            ProdutoEnum.produto2,
            ProdutoEnum.produto3,
        ]
        produto = st.selectbox(
            "Selecione o produto", produtos_disponiveis, format_func=lambda x: x.value
        )
    with col6:
        valor = st.number_input("Valor de venda", min_value=0.0, format="%2.f")
    with col7:
        quantidade = st.number_input("Quantidade de produto", min_value=1, step=1)
   

    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data, hora)

            venda = Vendas(
                nome=nome,
                email=email,
                data_hora=data_hora,  # Campo correto
                valor=valor,
                quantidade=quantidade,
                produto=produto
            ) # type: ignore

            salvar_dados(venda)
            st.success("Venda registrada com sucesso!")

        except ValidationError as e:
            st.error("Os dados fornecidos não são válidos.")
            st.json(e.errors())


if __name__ == "__main__":
    main()