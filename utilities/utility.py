import json

def jsonFormat(cur, rows):
    """
    Formatea los resultados de una consulta de base de datos a una cadena JSON.

    Args:
        cur: El objeto cursor de la base de datos, que contiene la descripción de las columnas.
        rows: Una lista de tuplas, donde cada tupla representa una fila de resultados.

    Returns:
        Una cadena JSON formateada con los nombres de las columnas como claves
        y los valores de las filas como valores.
    """
    column_names = [description[0] for description in cur.description]
    result_list = []

    for row in rows:
        row_dict = {}
        for i, col_name in enumerate(column_names):
            # Asigna el valor de la columna a su nombre correspondiente en el diccionario.
            row_dict[col_name] = row[i]
        result_list.append(row_dict)

    # Convierte la lista de diccionarios a una cadena JSON con indentación para legibilidad.
    json_output = json.dumps(result_list, indent=4)
    

    return json.loads(json_output)