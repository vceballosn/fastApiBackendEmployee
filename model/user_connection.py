import psycopg 
from utilities import utility # Importa la función desde tu archivo de utilidades

class UserConnection():
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=ems  user=postgres  password=81942686 host=localhost port=5432")
        except  psycopg.OperationalError as err:
            print(err)
            self.conn.close()

    def get_all(self):
        print("get all")
        with self.conn.cursor() as cur:     
            data = cur.execute("""SELECT * FROM "employees"
                              """)    
            json_output = utility.jsonFormat(cur,data)
            print("get all ",json_output)
        return  json_output
    
   
    def get_id(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute(""" SELECT * FROM "employees" WHERE id =%s """, (id,))
            # dataId =  cur.fetchone()
            json_output = utility.jsonFormat(cur,data)
        return  json_output
    
    def  write(self,data):
          with self.conn.cursor() as cur:
              cur.execute("""    
              INSERT INTO "employees"(first_name,last_name,email_id) VALUES (%(first_name)s,%(last_name)s,%(email_id)s) 
                         """,data)  # interpolacion data es un dicionario en python 
              self.conn.commit()
    
    def __def__(self):
        self.conn.close()        

   