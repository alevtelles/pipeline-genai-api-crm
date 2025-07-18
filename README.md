# Optimus Sistema de CRM & Vendas

Sistema para gerenciamento de vendas e relacionamento com clientes, com integração a banco de dados PostgreSQL.

## 📋 Funcionalidades

- Cadastro de vendas com validação de dados
- Registro de informações do vendedor (nome e e-mail)
- Controle de data/hora, valor e quantidade das vendas
- Seleção de produtos disponíveis
- Armazenamento em banco de dados PostgreSQL

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Streamlit (interface web)
- Pydantic (validação de dados)
- PostgreSQL (banco de dados)
- Psycopg2 (conexão com PostgreSQL)
- Python-dotenv (gerenciamento de variáveis de ambiente)

## ⚙️ Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone [URL_DO_REPOSITORIO]

2. Crie e ative um ambiente virtual
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate    # Windows

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt

4. Crie um arquivo .env na raiz do projeto com as variáveis de ambiente:
    ```bash
    DB_HOST=seu_host_postgres
    DB_NAME=seu_banco_de_dados
    DB_USER=seu_usuario
    DB_PASS=sua_senha


5. Execute a aplicação:
    ```bash
    streamlit run app.py


## 🗃️ Estrutura do Banco de Dados
Certifique-se de ter uma tabela vendas com a seguinte estrutura:

```bash
CREATE TABLE vendas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    data_hora TIMESTAMP NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    quantidade INTEGER NOT NULL,
    produto VARCHAR(50) NOT NULL
);

```

## 🚀 Como Usar
- Preencha os dados do vendedor (nome e e-mail)
- Informe a data e hora da venda
- Selecione o produto vendido
- Insira o valor e quantidade
- Clique em "Salvar" para registrar a venda

## 📝 Modelo de Dados
Os dados são validados conforme o seguinte modelo:

```
class Vendas(BaseModel):
    nome: str
    email: EmailStr
    data_hora: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum
```