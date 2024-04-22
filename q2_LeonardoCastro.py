from q1_LeonardoCastro import *

# Teste de Cash
test_login_and_cash = lambda usuario, senha, valor: executarLogin(usuario, senha)(0)(valor) == "Operação autorizada pelo banco.\nTransação completa."

# Teste de Transferência
test_login_and_fund = lambda usuario_origem, senha, usuario_destino, valor: executarLogin(usuario_origem, senha)(1)(usuario_destino, valor)(True, usuario_destino, valor) == "Operação autorizada pelo banco.\nTransação completa."

# Teste de Crédito
test_login_and_credit = lambda usuario_origem, senha, valor: executarLogin(usuario_origem, senha)(2)(valor)(True, usuario_origem, valor) == "Operação autorizada pelo banco.\nTransação completa."

# Teste de Estresse
test_stress_cash = lambda usuario, senha, valor: all(executarLogin(usuario, senha)(0)(valor) == "Operação autorizada pelo banco.\nTransação completa." or f"Saldo insuficiente para efetuar o pagamento de R$ {valor}." for _ in range(1000))

# Aconselho executar os testes um por um, pois o teste de estresse irá imprimir muitas mensagens no console
def executarTestes():
    # assert test_login_and_fund("usuario1", 1234, "usuario2", 100)
    # assert test_login_and_cash("usuario1", 1234, 100)
    # assert test_login_and_credit("usuario1", 1234, 100)
    assert test_stress_cash("usuario1", 1234, 1000)

executarTestes()
