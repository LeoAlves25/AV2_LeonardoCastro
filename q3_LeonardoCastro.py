import mysql.connector

joinColumnsText = lambda columns: ", ".join(columns) if columns else "*"
joinValuesText = lambda values: ", ".join([f"'{value}'" if isinstance(value, str) else f"{value}" for value in values])

joinSelectText = lambda columns: ", ".join(columns) if columns else "*"

joinSelectQuery = lambda query, colum, values: f"{query} {colum} FROM {values}"

insertTabelaQuery = lambda table, values: f"INSERT INTO {table} VALUES ({values})"
deleteTabelaQuery = lambda table, condition: f"DELETE FROM {table} WHERE {condition}"
selectTabelaQuery = lambda columns_str, table: f"SELECT {columns_str} FROM {table}"

conditionWhere = lambda condition: f" WHERE {condition}" if condition else ""

# Conectar ao banco de dados MySQL
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="funcional_av2"
)
db_cursor = db_connection.cursor()

# Funções com tabelas e colunas

USERS = lambda:  ("USERS", ["id", "name", "country", "id_console"])
VIDEOGAMES = lambda:  ("VIDEOGAMES", ["id_game", "name", "genre", "release_date", "id_console"])
COMPANY = lambda:  ("COMPANY", ["id_company", "name", "country"])
GAMES = lambda:  ("GAMES", ["id_game", "id_console", "title", "genre", "release_date"])


# Definir funções para inserção, remoção e consulta

def insert_record(table, values):
    valuesJoin = joinValuesText(values)
    query = insertTabelaQuery(table, valuesJoin)
    return query
    # db_cursor.execute(query)
    # db_connection.commit()

def delete_record(table, condition):
    query = deleteTabelaQuery(table, condition)
    # return query
    db_cursor.execute(query)
    db_connection.commit()

def select_records(table, columns=None, condition=None):
    columns_str = joinSelectText(columns)
    query = selectTabelaQuery(columns_str, table)
    query += conditionWhere(condition)
    # return query
    db_cursor.execute(query)
    return db_cursor.fetchall()

gen_insert_record = lambda table, values: insert_record(table[0], values)
gen_delete_record = lambda table, condition: delete_record(table[0], condition)
gen_select_record = lambda table, condition = None: select_records(table[0], table[1], condition)

# Inserir um registro na tabela USERS
print(gen_insert_record(USERS(), [2, 1,"Teste", "Chile"]))

# Remover um registro da tabela USERS
# gen_delete_record(USERS(), "id = 2")

# Consultar registros da tabela GAMES
print(gen_select_record(USERS(), "id = 1"))

# Fechar a conexão com o banco de dados ao final do uso
db_cursor.close()
db_connection.close()