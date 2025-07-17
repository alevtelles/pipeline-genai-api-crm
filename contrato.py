from datetime import datetime
from pydantic import BaseModel, EmailStr, field_validator, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "Agente com Gemini" 
    produto2 = "Agente com OpenAI"
    produto3 = "Agentes com Ilama3"

class Vendas(BaseModel):
    nome: str
    email: EmailStr
    data_hora: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum

    @field_validator("produto")
    @classmethod
    def categoria_produto_enum(cls, v):
        return v
