listaColunas = lambda t1, t2: [e for e in t1[1] if e in t2[1]]

colunasJoin = lambda colunas=None: f"\n, ".join(colunas) if colunas else "*"

addColAlias = lambda arraDeTuplas: [f"{tabela[2]}.{col}" for tabela in arraDeTuplas for col in tabela[1]] if arraDeTuplas else None

textoInnerJoin = lambda t2: f" INNER JOIN {t2[0]} {t2[2]} ON "
textoInnerJoinColmuns = lambda t1, t2, commonattrs: ''.join(map(lambda i_attr: " AND " + f"{t1[2]}.{i_attr[1]} = {t2[2]}.{i_attr[1]}" if i_attr[0] > 0 else f"{t1[2]}.{i_attr[1]} = {t2[2]}.{i_attr[1]}", enumerate(commonattrs)))

textoSelect = lambda tabela, colunasStr: f"SELECT {colunasStr} \nFROM {tabela} {tabela[0].lower()}"

condicaoWhere = lambda condicao: f" WHERE {condicao}" if condicao else ""

def montarJoin(t1, t2):
    commonattrs = listaColunas(t1, t2)
    code = textoInnerJoin(t2)
    code += textoInnerJoinColmuns(t1, t2, commonattrs)
    return code

def montarSelect(tabela, colunas=None, condicao=None):
    colunasArray = addColAlias(colunas)
    colunasStr = colunasJoin(colunasArray)
    query = textoSelect(tabela, colunasStr)
    query += condicaoWhere(condicao)
    return query

# Tabelas sendo salvas como tuplas onde vai ter o nome da tabela, as colunas e um alias para a tabela
VIDEOGAMES = lambda:  ("VIDEOGAMES", ["id_game", "name", "genre", "release_date", "id_console"], "v")
GAMES = lambda:  ("GAMES", ["id_game", "id_console", "title", "genre", "release_date", "id_company"], "g")
COMPANY = lambda:  ("COMPANY", ["id_company", "name", "country"], "c")

imprimir = lambda f1, f2, f3: print(f"{f1}\n{f2}\n{f3}")

# imprimir(montarSelect(GAMES()[0], (GAMES(), VIDEOGAMES(), COMPANY()), "v.id_game = 1"), montarJoin(GAMES(), VIDEOGAMES()), montarJoin(GAMES(), COMPANY()))