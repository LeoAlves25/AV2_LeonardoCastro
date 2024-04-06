user1 = {"name": "Leonardo", "balance": 1000, "account": 1234}
user2 = {"name": "Lucas", "balance": 1000, "account": 5678}
user3 = {"name": "Pedro", "balance": 1000, "account": 9101}
user4 = {"name": "João", "balance": 1000, "account": 1121}

logedUser = user1
accountList = [user1, user2, user3, user4]

checkCash = lambda cash: cash if cash.isnumeric() and int(cash) > 0 else "Invalid Value" if cash.isalpha() else "Invalid Value"
checkAccount = lambda account: any(user["account"] == int(account) for user in accountList)
checkAccountBalance = lambda account, value: (account if checkAccount(account) and int(value) <= logedUser["balance"] else "Insufficient funds") if account.isnumeric() and value.isnumeric() else "Invalid Value" if account.isalpha() or value.isalpha() else "Invalid Value"

addBalance = lambda account, value: [user.update({"balance": user["balance"] + int(value)}) for user in accountList if user["account"] == int(account)]
removeBalance = lambda account, value: [user.update({"balance": user["balance"] - int(value)}) for user in accountList if user["account"] == int(account)]

def cash():
    print("Cash")
    value = input("Enter the amount to withdraw: ")
    print(checkAccountBalance(str(logedUser["balance"]), value))
    return completeCashTransaction(logedUser["account"], int(value)) if checkCash(value) == value else cash()

def fund():
    print("Fund Transfer")
    account = input("Enter the account number: ")
    value = input("Enter the amount to transfer: ")
    print(checkAccountBalance(account, value))
    return completeFundTransaction(account, value) if checkAccountBalance(account, value) == account else fund()


def credit():
    print("Credit")
    value = input("Enter the amount to deposit: ")
    print(checkCash(value))
    return completeCashTransaction(logedUser["account"], int(value)) if checkCash(value) == value else credit()

transactionChoice = (cash, fund, credit)

createTransaction = lambda escolha:  (transactionChoice[int(escolha)]() if int(escolha) <= 2 else "ERROR") if escolha.isnumeric() else "ERROR" if escolha.isalpha() else "ERROR"

def completeCashTransaction(account, value):
    removeBalance(account, value)
    print("User: ", logedUser["name"])
    print("User Balance: ", logedUser["balance"])
    return completeTransaction()

def completeFundTransaction(accountReceive, value):
    removeBalance(logedUser["account"], value)
    addBalance(accountReceive, value)
    
    print("User: ", logedUser["name"])
    print("User Balance: ", logedUser["balance"])
    
    print("User Receive: ", accountList[accountList.index(next(user for user in accountList if user["account"] == int(accountReceive)))]["name"])
    print("User Balance: ", next(user["balance"] for user in accountList if user["account"] == int(accountReceive)))
    return completeTransaction()

completeTransaction = lambda: "Transaction Completed"
closeTransaction = lambda: "Transaction Closed"

print(createTransaction(input("Choose a transaction: \n0 - Cash \n1 - Fund Trasnfer \n2 - Credit:\n")))
