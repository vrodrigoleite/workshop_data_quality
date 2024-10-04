from pydantic import BaseModel, PositiveFloat, PositiveInt
import pandera as pa
import pandas as pd

dict_vendas = {
    "nome":["livro","cadeira"],
    "quantidade":[10,20],
    "valor":[50.5,80.9]
}

df_vendas = pd.DataFrame(dict_vendas)

class SchemaDados(BaseModel):
    nome: str
    quantidade: PositiveInt
    valor: PositiveFloat


schema = pa.infer_schema(df_vendas)
print(schema)