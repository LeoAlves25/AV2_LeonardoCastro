listaColunas = lambda t1, t2: [e for e in t1[1] if e in t2[1]]

colunasJoin = lambda table, columns=None: f"\n, {table[0].lower()}.".join(columns) if columns else "*"

textInnerJoin = lambda t1, t2: f" INNER JOIN {t2[0]} {t2[2]} ON "
textInnerJoinColmuns = lambda t1, t2, commonattrs: ''.join(map(lambda i_attr: " AND " + f"{t1[2]}.{i_attr[1]} = {t2[2]}.{i_attr[1]}" if i_attr[0] > 0 else f"{t1[2]}.{i_attr[1]} = {t2[2]}.{i_attr[1]}", enumerate(commonattrs)))

textSelect = lambda table, columns_str: f"SELECT {table[0].lower()}.{columns_str} \nFROM {table} {table[0].lower()}"

conditionWhere = lambda condition: f" WHERE {condition}" if condition else ""

def gen_inner_join(t1, t2):
    commonattrs = listaColunas(t1, t2)
    code = textInnerJoin(t1, t2)
    code += textInnerJoinColmuns(t1, t2, commonattrs)
    return code

def select_records(table, columns=None, condition=None):
    columns_str = colunasJoin(table, columns)
    query = textSelect(table, columns_str)
    query += conditionWhere(condition)
    return query

VIDEOGAMES = lambda:  ("VIDEOGAMES", ["id_game", "name", "genre", "release_date", "id_console"], "v")
GAMES = lambda:  ("GAMES", ["id_game", "id_console", "title", "genre", "release_date", "id_company"], "g")
COMPANY = lambda:  ("COMPANY", ["id_company", "name", "country"], "c")

imprimir = lambda f1, f2, f3: print(f"{f1}\n{f2}\n{f3}")

imprimir(select_records(GAMES()[0], GAMES()[1]), gen_inner_join(GAMES(), VIDEOGAMES()), gen_inner_join(GAMES(), COMPANY()))