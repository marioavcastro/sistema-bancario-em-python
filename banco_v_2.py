import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [sc]\tSaldo Conta Corrente
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(valor, meu_saldo, /):
    if valor > 0:
        meu_saldo = meu_saldo + valor

    return meu_saldo

def sacar(*, meu_saldo, valor, max_saque, limite_saque, numero_saque):
    limite_excedido = valor > limite_saque
    maximo_saque_excedido = numero_saque >= max_saque

    if limite_excedido:
        print("Valor de saque acima do permitido")
    elif maximo_saque_excedido:
        print("Quantidade de saques diarios alcançado")
    elif valor > meu_saldo:
        print("Saldo Insuficiente")
    else:
        meu_saldo -= valor
        numero_saque = numero_saque + 1
        print(f"Valor sacado: {valor}")
    return meu_saldo

def exibirSaldo(meu_saldo):
    return meu_saldo

def cadastroUsuario(cpf, nome, endereco, cidade, estado):
    return {cpf: {"nome": nome, "endereco": endereco, "cidade": cidade, "estado": estado}}

def verificar_usuario(*usuarios):
    for users in usuarios:
        for i in users:
            if cpf == i[cpf]:
                print("Usuario cadastrado")

def listarUsuarios(*args):
    for chave in args:
        print(f"Acessando Chave '{chave}', valor = {args.get(chave)}")

def nova_conta(agencia,numero_conta,usuario):
    cpf = input("Digite o CPF: \n")
    return {"Agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

def main():
    MAX_SAQUE = 3
    LIMITE_SAQUE = 500.0
    extrato = []
    numero_saque = 0
    meu_saldo = 0.0
    usuarios = []
    contas = []


    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Digite o valor a ser depositado: "))
            meu_saldo = depositar(valor, meu_saldo)
            print(meu_saldo)
        elif opcao == "s":
            valor_a_sacar = float(input("Digite o valor a ser sacado: "))
            meu_saldo = sacar(meu_saldo=meu_saldo,
                              valor=valor_a_sacar,
                              numero_saque=numero_saque,
                              limite_saque=LIMITE_SAQUE,
                              max_saque=MAX_SAQUE)


        elif opcao == "sc":
            print(meu_saldo)
        elif opcao == "nu":
            cpf = input("Digite seu CPF: \n")
            nome = input("Digite o nome do titular da conta: \n")
            endereco = input("Digite o endereco: \n")
            cidade = input("Cidade: \n")
            estado = input("Estado: \n")
            usuarios.append(cadastroUsuario(cpf, nome, endereco, cidade, estado))
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = nova_conta(agencia, numero_conta, usuario)
        elif opcao == "q":
            break
        else:
            print("Operaçao invalida")

main()