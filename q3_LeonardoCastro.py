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
mySqlConnection = lambda host, user, password, database: mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

dbConnection = mySqlConnection("localhost", "root", "12345678", "funcional_av2")

db_cursor = dbConnection.cursor()

# Funções com tabelas e colunas
USERS = lambda:  ("USERS", ["id", "name", "country", "id_console"])
VIDEOGAMES = lambda:  ("VIDEOGAMES", ["id_game", "name", "genre", "release_date", "id_console"])
COMPANY = lambda:  ("COMPANY", ["id_company", "name", "country"])
GAMES = lambda:  ("GAMES", ["id_game", "id_console", "title", "genre", "release_date"])


# Definir funções para inserção, remoção e consulta
def insertRecord(table, values):
    valuesJoin = joinValuesText(values)
    query = insertTabelaQuery(table, valuesJoin)
    db_cursor.execute(query)
    dbConnection.commit()

def deleteRecord(table, condition):
    query = deleteTabelaQuery(table, condition)
    db_cursor.execute(query)
    dbConnection.commit()

def selectRecords(table, columns=None, condition=None):
    columns_str = joinSelectText(columns)
    query = selectTabelaQuery(columns_str, table)
    query += conditionWhere(condition)
    db_cursor.execute(query)
    return db_cursor.fetchall()

genInsertRecord = lambda table, values: insertRecord(table[0], values)
genDeleteRecord = lambda table, condition: deleteRecord(table[0], condition)
genSelectRecord = lambda table, condition = None: selectRecords(table[0], table[1], condition)

# Inserir um registro na tabela USERS
genInsertRecord(USERS(), [2, 1,"Teste", "Chile"])

# Remover um registro da tabela USERS
genDeleteRecord(USERS(), "id = 2")

# Consultar registros da tabela USERS
print(genSelectRecord(USERS(), "id = 1"))

# Fechar a conexão com o banco de dados ao final do uso
db_cursor.close()
dbConnection.close()