import mysql.connector

joinColumnsText = lambda columns: ", ".join(columns)
joinValuesText = lambda values: ", ".join(["%s"] * len(values))

joinSelectText = lambda columns: ", ".join(columns) if columns else "*"

joinSelectQuery = lambda query, colum, values: f"{query} {colum} FROM {values}"

insertTabelaQuery = lambda table, columns, values: f"INSERT INTO {table} ({columns}) VALUES ({values})"
deleteTabelaQuery = lambda table, condition: f"DELETE FROM {table} WHERE {condition}"
selectTabelaQuery = lambda columns_str, table: f"SELECT {columns_str} FROM {table}"

conditionWhere = lambda condition: f" WHERE {condition}" if condition else ""

# Conectar ao banco de dados MySQL
# db_connection = mysql.connector.connect(
#     host="localhost",
#     user="seu_usuario",
#     password="sua_senha",
#     database="seu_banco_de_dados"
# )
# db_cursor = db_connection.cursor()

# Funções com tabelas e colunas

USERS = lambda:  ("USERS", ["id", "name", "country", "id_console"])
VIDEOGAMES = lambda:  ("VIDEOGAMES", ["id_game", "name", "genre", "release_date", "id_console"])
COMPANY = lambda:  ("COMPANY", ["id_company", "name", "country"])
GAMES = lambda:  ("GAMES", ["id_game", "id_console", "title", "genre", "release_date"])


# Definir funções para inserção, remoção e consulta

def insert_record(table, columns, values):
    query = insertTabelaQuery(table, columns, values)
    return query
    # db_cursor.execute(query, values)
    # db_connection.commit()

def delete_record(table, condition):
    query = deleteTabelaQuery(table, condition)
    return query
    # db_cursor.execute(query)
    # db_connection.commit()

def select_records(table, columns=None, condition=None):
    columns_str = joinSelectText(columns)
    query = selectTabelaQuery(columns_str, table)
    query += conditionWhere(condition)
    return query
    # db_cursor.execute(query)
    # return db_cursor.fetchall()

gen_insert_record = lambda table, values: insert_record(table[0], table[1], values)
gen_delete_record = lambda table, condition: delete_record(table[0], condition)
gen_select_record = lambda table, condition = None: select_records(table[0], table[1], condition)

# Inserir um registro na tabela USERS
print(gen_insert_record(USERS(), [1, "UserName", "Country", 1]))

# Remover um registro da tabela VIDEOGAMES
print(gen_delete_record(VIDEOGAMES(), "name = 'GameName'"))

# Consultar registros da tabela GAMES
print(gen_select_record(GAMES(), ["id_game", "title", "genre", "release_date", "id_console"]))

# Fechar a conexão com o banco de dados ao final do uso
# db_cursor.close()
# db_connection.close()