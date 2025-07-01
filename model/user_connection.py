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
            data = cur.execute("""SELECT id as id, email_id as email,first_name as "firstName", last_name as "lastName" FROM "employees"
                              """)    
            json_output = utility.jsonFormat(cur,data)
            print("get all ",json_output)
        return  json_output
    
   
    def get_id(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT
                    id as id,
                    email_id as email,
                    first_name as "firstName",
                    last_name as "lastName"
                FROM "employees"
                WHERE id = %s
            """, (id,)) # Pass id as a tuple (id,)

            # Fetch the single record after execution
            single_record = cur.fetchone()

            # Now, pass the fetched single record to jsonFormatSingle
            json_output = utility.jsonFormatSingle(cur, single_record)
            
        return json_output
    
    def  write(self,data):
          with self.conn.cursor() as cur:
              cur.execute("""    
              INSERT INTO "employees"(first_name,last_name,email_id) VALUES (%(firstName)s,%(lastName)s,%(email)s) 
                         """,data)  # interpolacion data es un dicionario en python 
              self.conn.commit()

    def  update(self,data):  
          with self.conn.cursor()  as cur:
               cur.execute("""    
               UPDATE "employees" SET first_name = %(firstName)s ,last_name = %(lastName)s , email_id=%(email)s   WHERE id = %(id)s
                         """,data)  # interpolacion data es un dicionario en python 
               self.conn.commit() 
                   

    def delete(self, id):
            with self.conn.cursor() as cur:
                # Pass 'id' as a single-element tuple (id,)
                cur.execute("""DELETE FROM "employees" WHERE id = %s""", (id,))
                self.conn.commit()
    def __def__(self): # descontrutor
        self.conn.close()        

   