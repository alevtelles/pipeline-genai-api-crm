import streamlit as st
from datetime import datetime, time
from contrato import Vendas, ProdutoEnum
from pydantic import ValidationError

def main():

    st.title("Optimus Sistema de CRM & Vendas")
    st.write("Bem-vindo ao nosso sistema de CRM e Vendas! Aqui, você pode gerenciar suas vendas e clientes de forma eficiente.")
    st.divider()

    nome = st.text_input("Nome do vendedor")
    email = st.text_input("Digite o e-mail do vendedor")
    data = st.date_input("Data da venda", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9, 0))
    valor = st.number_input("Valor de venda",min_value=0.0, format="%2.f")
    quantidade =st.number_input("Quantidade de produto", min_value=1, step=1)
    produtos_disponiveis = [ProdutoEnum.produto1, ProdutoEnum.produto2, ProdutoEnum.produto3]  
    produto = st.selectbox("Selecione o produto", produtos_disponiveis, format_func=lambda x: x.value)


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

            st.success("Venda registrada com sucesso!")
            st.json(venda.model_dump())

        except ValidationError as e:
            st.error("Os dados fornecidos não são válidos.")
            st.json(e.errors())


if __name__ == "__main__":
    main()