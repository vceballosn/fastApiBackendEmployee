import psycopg 
import json

class UserConnection():
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=ems  user=postgres  password=81942686 host=localhost port=5432")
        except  psycopg.OperationalError as err:
            print(err)
            self.conn.close()

    def get_all(self):
        with self.conn.cursor() as cur:     
            data = cur.execute("""SELECT * FROM "employees"
                              """)    
            rows = data.fetchall()
  
            column_names = [description[0] for description in cur.description]

            result_list = []
            for row in rows:
                row_dict = {}
                for i, col_name in enumerate(column_names):
                    row_dict[col_name] = row[i]
                result_list.append(row_dict)

            json_output = json.dumps(result_list, indent=4)
            
            print(json_output)

        return  json.loads(json_output)
    
    def  write(self,data):
          with self.conn.cursor() as cur:
              cur.execute("""    
              INSERT INTO "employees"(first_name,last_name,email_id) VALUES (%(first_name)s,%(last_name)s,%(email_id)s) 
                         """,data)  # interpolacion data es un dicionario en python 
              self.conn.commit()
    
    def __def__(self):
        self.conn.close()        

   