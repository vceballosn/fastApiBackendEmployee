from fastapi import FastAPI
from model.user_connection import UserConnection
from schema.user_schema    import UserSchema

app = FastAPI() # <-- This line is crucial!
conn = UserConnection()

@app.get("/")
async def root():
    items =[]
   ## for data in conn.read_all():
   ##     print(data)

    return conn.get_all()


@app.post("/api/insert/")
def insert(user_data:UserSchema):
    data = user_data.dict()
    data.pop("id") # para eliminar el atributo id del formato json 
    print(data)
    conn.write(data)

