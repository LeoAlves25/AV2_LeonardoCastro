from q2_LeonardoCastro import *
from flask import Flask, request, render_template
import random

app = Flask(__name__, template_folder='templates')

users = lambda : {
    "usuario1": cesar(fencrypt, "1234"),
    "usuario2": cesar(fencrypt, "4321")
}

numeroRandomico = lambda: random.randint(1, 100)
numeroAleatorio = numeroRandomico()

join = lambda l : "".join(str(x) for x in l)
fcrypt = lambda b, c, v : (b and chr (ord (c) + v)) or (not b and chr (ord (c) - v))
fencrypt = lambda c : fcrypt (True, c, numeroAleatorio)
fdecrypt = lambda c : fcrypt (False, c, numeroAleatorio)
cesar = lambda f, s : join ([f (x) for x in list (s)])

wrong = lambda : "Usuário ou senha incorretos."
invalid = lambda : "Usuário não existe."
password_match = lambda dict : cesar(fdecrypt, dict[f'{request.form["username"]}']) == request.form["password"]
check_password = lambda : welcome() if password_match(users()) else wrong()
check_if_user_exists = lambda : check_password() if f'{request.form["username"]}' in users() else invalid()
reqresp = lambda : check_if_user_exists() if request.method == "POST" else render_template("index.html")

def welcome():
    executarTestes()
    return f"Bem-vindo {request.form['username']}!\nA execução dos testes se encontram no console."

app.add_url_rule('/index/', 'index', reqresp, methods=['GET', 'POST'])
app.run(host='0.0.0.0', port=8080)