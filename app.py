from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Lista de nombres
names = ['fer', 'jose', 'juan', 'pedro', 'luis', 'maria', 'ana', 'laura', 'sofia', 'lucia']

# Modelo para el cuerpo del POST
class NameData(BaseModel):
    name: str

# Método GET
@app.get("/names")
async def get_names():
    print("Se ha llamado al método GET para obtener los nombres")
    return names

# Método POST
@app.post("/names")
async def add_name(data: NameData):
    print(f"Se ha llamado al método POST con el nombre: {data.name}")
    return {"name": data.name}