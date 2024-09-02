import textwrap

def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return menu

saldo = 0
limite = 500
extrato_info = ""
numero_saques = 0
LIMITE_SAQUES = 3

def saque(saldo, numero_saques, extrato):
    global limite, LIMITE_SAQUES
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, numero_saques, extrato


def deposito(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f'{valor:.2f} depositado com sucesso')
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def extrato(saldo, extrato_info):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato_info else extrato_info)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:
    opcao = input(menu())
    if opcao == "d":
        saldo, extrato_info = deposito(saldo, extrato_info)
    elif opcao == "s":
        saldo, numero_saques , extrato_info= saque(saldo, numero_saques, extrato_info)
    elif opcao == "e":
        extrato(saldo, extrato_info)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
