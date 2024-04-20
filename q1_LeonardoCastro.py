USER1 = lambda: {"senha": 1234, "saldo": 1000}
USER2 = lambda: {"senha": 5678, "saldo": 2000}

usuario1 = USER1()
usuario2 = USER2()

contasBancoFunc = lambda x, y: {"usuario1": x, "usuario2": y}

contasBanco = contasBancoFunc(usuario1, usuario2)

# Operação de Cash
def cash(valor):
    imprimir("\nOperação de Cash")
    imprimir(f"Valor: {valor}")
    return confirmarCash(valor) if checkSaldo(list(usuarioLogado.keys())[0], valor) else f"Saldo insuficiente para efetuar o pagamento de R$ {valor}."

def confirmarCash(valor):
    descontarSaldo(list(usuarioLogado.keys())[0], valor)
    imprimir(f"Pagamento de R$ {valor} efetuado com sucesso.")
    imprimir(f"Saldo atual: {contasBanco[list(usuarioLogado.keys())[0]]['saldo']}")
    return transacaoCompleta()

# Operação de Transferência
def fund(conta, valor):
    imprimir("\nOperação de Transferência")
    imprimir("Informações da conta para transferência:")
    imprimir(f"Conta: {conta}")
    imprimir(f"Valor: {valor}")
    return confirmarOuCancelarFund if checkUsuario(conta) and checkSaldo(conta, valor) else cancelar()

def confirmarFund(conta, valor):
    descontarSaldo(list(usuarioLogado.keys())[0], valor)
    creditarSaldo(conta, valor)
    imprimir(f"Transferência de R$ {valor} para a conta {conta} efetuada com sucesso.")
    imprimir(f"Saldo atual: {contasBanco[list(usuarioLogado.keys())[0]]['saldo']}")
    return transacaoCompleta()

# Operação de Crédito
def credit(conta, valor):
    imprimir("\nOperação de Crédito")
    imprimir("Informações da conta para creditar:")
    imprimir(f"Conta: {conta}")
    imprimir(f"Valor: {valor}")
    return confirmarOuCancelarCredit if checkUsuario(conta) else "Conta inválida."

def confirmarCredit(conta, valor):
    creditarSaldo(conta, valor)
    imprimir(f"Crédito de R$ {valor} na conta {conta} efetuado com sucesso.")
    imprimir(f"Saldo atual: {contasBanco[conta]['saldo']}")

def confirmarCredit(conta, valor):
    creditarSaldo(conta, valor)
    return transacaoCompleta()

# Operação de Login e Seleção de Transação
def loginAction(usuario):
    usuarioLogado.update({usuario: contasBanco[usuario]})
    return criarTransacao

listaTransacaoFunc = lambda cash, fund, credit: (cash, fund, credit)
listaTransacao = listaTransacaoFunc(cash, fund, credit)

imprimir = lambda funcao: print(funcao)

checkUsuario = lambda usuario: usuario in contasBanco
checkSaldo = lambda usuario, valor: contasBanco[usuario]["saldo"] >= valor

login = lambda usuario, senha: usuario in contasBanco and contasBanco[usuario]["senha"] == senha

usuarioLogado = {}
executarLogin = lambda usuario, senha: loginAction(usuario) if login(usuario, senha) else "Usuário ou senha inválidos."

descontarSaldo = lambda usuario, valor: contasBanco[usuario].update({"saldo": contasBanco[usuario]["saldo"] - valor})
creditarSaldo = lambda usuario, valor: contasBanco[usuario].update({"saldo": contasBanco[usuario]["saldo"] + valor})

criarTransacao = lambda escolha: listaTransacao[int(escolha)]
confirmarOuCancelarFund = lambda escolha, conta = None, valor = None: confirmarFund(conta, valor) if escolha else cancelar()
confirmarOuCancelarCredit = lambda escolha, conta = None, valor = None: confirmarCredit(conta, valor) if escolha else cancelar()

confirmar = lambda: transacaoCompleta() + "\n" + transacaoEncerrada()
cancelar = lambda: transacaoCancelada() + "\n" + transacaoEncerrada()

transacaoCompleta = lambda: "Operação autorizada pelo banco.\nTransação completa."
transacaoEncerrada = lambda: "Transação encerrada."
transacaoCancelada = lambda: "Transação cancelada."

# imprimir(executarLogin("usuario1", 1234)(0)(100))
# imprimir(executarLogin("usuario1", 1234)(1)("usuario2", 100)(False))
# imprimir(executarLogin("usuario1", 1234)(2)("usuario2", 100)(True, "usuario2", 150))