from fastapi import FastAPI, Response
from starlette.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_204_NO_CONTENT
from starlette import status

from model.user_connection import UserConnection
from schema.user_schema    import UserSchema

app = FastAPI() # <-- This line is crucial!
conn = UserConnection()

@app.get("/api/python",status_code= HTTP_200_OK)
async def root():
    items =[]
   ## for data in conn.read_all():
   ##     print(data)

    return conn.get_all()

@app.post("/api/python/",status_code=HTTP_201_CREATED)
def insert(user_data:UserSchema):
    data = user_data.dict()
    data.pop("id") # para eliminar el atributo id del formato json 
    print(data)
    conn.write(data)
    return Response (status_code=HTTP_201_CREATED)

@app.get("/api/python/{id}",status_code=HTTP_200_OK)
def get_id(id:str):
    return conn.get_id(id)

@app.delete("/api/python/{id}",status_code=HTTP_204_NO_CONTENT)
def delete(id:str):
    print(id)
    conn.delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.put("/api/python/",status_code=HTTP_204_NO_CONTENT)
def update(user_data:UserSchema):   
      data = user_data.dict()  
      print(data)
      conn.update(data)
      return Response(status_code=HTTP_204_NO_CONTENT)
