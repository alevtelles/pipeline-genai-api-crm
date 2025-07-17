import streamlit as st
from datetime import datetime, time

def main():

    st.title("Optimus Sistema de CRM e Vendas")
    st.write("Bem-vindo ao nosso sistema de CRM e Vendas! Aqui, você pode gerenciar suas vendas e clientes de forma eficiente.")
    st.divider()

    nome = st.text_input("Nome do vendedor")
    email = st.text_input("Digite o e-mail do vendedor")
    data = st.date_input("Data da venda", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9, 0))
    valor = st.number_input("Valor de venda",min_value=0.0, format="%2.f")
    quantidade =st.number_input("Quantidade de produto", min_value=1, step=1)
    produto =st.selectbox("Selecione o produto", ["ZapFlow com Gemini", "ZapFlow com OpenAI", "ZapFlow com Ilama3"])
    

    if st.button("Salvar"):
        data_hora = datetime.combine(data, hora)
        st.write("Venda salva com sucesso!")
        st.write("Nome:", nome)
        st.write("Email:", email)
        st.write("Data:", data)
        st.write("Hora:", hora)
        st.write("Valor:", valor)
        st.write("Quantidade:", quantidade)
        st.write("Produto:", produto)



if __name__ == "__main__":
    main()