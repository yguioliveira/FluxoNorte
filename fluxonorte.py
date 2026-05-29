import os

# =========================================
# SISTEMA FLUXONORTE
# =========================================

pedidos = []
entregadores = []

LIMITE_PEDIDOS_POR_VEICULO = {
    "Moto": 2,
    "Carro": 3,
    "Van": 5
}


# =========================================
# LIMPAR TELA
# =========================================

def limpar_tela():
    os.system("cls")


# =========================================
# FUNCOES AUXILIARES
# =========================================

def buscar_pedido(id_pedido):
    for pedido in pedidos:
        if pedido["id"] == id_pedido:
            return pedido

    return None


def buscar_entregador(id_entregador):
    for entregador in entregadores:
        if entregador["id"] == id_entregador:
            return entregador

    return None


def pausar():
    input("\nENTER para continuar...")


def ler_id_pedido():
    valido = 0

    while valido == 0:
        id_pedido = input("Digite o ID do pedido (Ex: P0001): ").upper()

        if len(id_pedido) != 5:
            print("\nO ID deve possuir 1 letra e 4 numeros!")
        elif not id_pedido[0].isalpha():
            print("\nO primeiro caractere deve ser uma letra!")
        elif not id_pedido[1:].isdigit():
            print("\nOs ultimos 4 caracteres devem ser numeros!")
        else:
            valido = 1

    return id_pedido


def ler_id_entregador():
    valido = 0

    while valido == 0:
        id_entregador = input("Digite o ID do entregador (4 digitos): ")

        if not id_entregador.isdigit():
            print("\nDigite apenas numeros!")
        elif len(id_entregador) != 4:
            print("\nO ID do entregador deve possuir exatamente 4 digitos!")
        else:
            valido = 1

    return id_entregador


def ler_prioridade():
    valido = 0

    while valido == 0:
        prioridade = input("Prioridade (Alta/Normal): ").capitalize()

        if prioridade == "Alta" or prioridade == "Normal":
            valido = 1
        else:
            print("\nPrioridade invalida! Digite Alta ou Normal.")

    return prioridade


def ler_veiculo():
    valido = 0

    while valido == 0:
        veiculo = input("Veiculo (Carro/Van/Moto): ").capitalize()

        if veiculo == "Carro" or veiculo == "Van" or veiculo == "Moto":
            valido = 1
        else:
            print("\nVeiculo invalido! Digite Carro, Van ou Moto.")

    return veiculo


def ler_pagamento():
    valido = 0

    while valido == 0:
        pagamento = input("Pedido ja foi pago? (S/N): ").upper()

        if pagamento == "S":
            return "Sim"
        elif pagamento == "N":
            return "Nao"
        else:
            print("\nOpcao invalida! Digite S para sim ou N para nao.")


def calcular_disponibilidade(entregador):
    if len(entregador["pedidos_ativos"]) < limite_pedidos_entregador(entregador):
        return "Disponivel"

    return "Indisponivel"


def limite_pedidos_entregador(entregador):
    return LIMITE_PEDIDOS_POR_VEICULO[entregador["veiculo"]]


def prioridade_valor(pedido):
    if pedido["prioridade"] == "Alta":
        return 0

    return 1


def remover_pedido_ativo_do_entregador(pedido):
    if pedido["entregador"] != "":
        entregador = buscar_entregador(pedido["entregador"])

        if entregador != None:
            if pedido["id"] in entregador["pedidos_ativos"]:
                entregador["pedidos_ativos"].remove(pedido["id"])


def registrar_entrega_realizada(pedido):
    if pedido["entregador"] != "":
        entregador = buscar_entregador(pedido["entregador"])

        if entregador != None:
            if pedido["id"] not in entregador["entregas_realizadas"]:
                entregador["entregas_realizadas"].append(pedido["id"])


def processar_reembolso(pedido):
    if pedido["pago"] == "Sim":
        pedido["reembolso"] = "Gerado"
        print("\nPedido pago. Reembolso gerado para o cliente.")
    else:
        pedido["reembolso"] = "Nao necessario"
        print("\nPedido nao pago. Nenhum reembolso foi gerado.")


# =========================================
# MENU PEDIDOS
# =========================================

def menu_pedidos():
    opcao = -1

    while opcao != 0:
        limpar_tela()

        print("=================================")
        print("            PEDIDOS")
        print("=================================")
        print("1 - Cadastrar Pedido")
        print("2 - Atualizar Status")
        print("3 - Buscar Pedido")
        print("4 - Pedidos Pendentes")
        print("5 - Pedidos Entregues")
        print("0 - Voltar")

        entrada = input("\nEscolha uma opcao: ")

        if entrada.isdigit():
            opcao = int(entrada)

            if opcao == 1:
                cadastrar_pedido()
            elif opcao == 2:
                atualizar_status()
            elif opcao == 3:
                buscar_por_id()
            elif opcao == 4:
                pedidos_pendentes()
            elif opcao == 5:
                pedidos_entregues()
            elif opcao == 0:
                print()
            else:
                print("\nOpcao invalida!")
                pausar()
        else:
            print("\nDigite apenas numeros!")
            pausar()


# =========================================
# MENU ENTREGADORES
# =========================================

def menu_entregadores():
    opcao = -1

    while opcao != 0:
        limpar_tela()

        print("=================================")
        print("         ENTREGADORES")
        print("=================================")
        print("1 - Cadastrar Entregador")
        print("2 - Associar Entregador")
        print("3 - Remover Associacao")
        print("4 - Entregadores Disponiveis")
        print("5 - Entregas por Entregador")
        print("0 - Voltar")

        entrada = input("\nEscolha uma opcao: ")

        if entrada.isdigit():
            opcao = int(entrada)

            if opcao == 1:
                cadastrar_entregador()
            elif opcao == 2:
                associar_entregador()
            elif opcao == 3:
                remover_associacao()
            elif opcao == 4:
                entregadores_disponiveis()
            elif opcao == 5:
                entregas_por_entregador()
            elif opcao == 0:
                print()
            else:
                print("\nOpcao invalida!")
                pausar()
        else:
            print("\nDigite apenas numeros!")
            pausar()


# =========================================
# MENU RELATORIOS
# =========================================

def menu_relatorios():
    opcao = -1

    while opcao != 0:
        limpar_tela()

        print("=================================")
        print("           RELATORIOS")
        print("=================================")
        print("1 - Relatorio Geral")
        print("0 - Voltar")

        entrada = input("\nEscolha uma opcao: ")

        if entrada.isdigit():
            opcao = int(entrada)

            if opcao == 1:
                relatorios()
            elif opcao == 0:
                print()
            else:
                print("\nOpcao invalida!")
                pausar()
        else:
            print("\nDigite apenas numeros!")
            pausar()


# =========================================
# CADASTRAR PEDIDO
# =========================================

def cadastrar_pedido():
    limpar_tela()

    print("===== CADASTRO DE PEDIDO =====\n")

    valido = 0

    while valido == 0:
        id_pedido = ler_id_pedido()

        if buscar_pedido(id_pedido):
            print("\nPedido ja cadastrado!")
        else:
            valido = 1

    cliente = input("Nome do cliente: ")
    endereco = input("Endereco: ")
    prioridade = ler_prioridade()
    descricao = input("Descricao do pedido: ")
    pago = ler_pagamento()

    pedido = {
        "id": id_pedido,
        "cliente": cliente,
        "endereco": endereco,
        "prioridade": prioridade,
        "descricao": descricao,
        "status": "Pendente",
        "entregador": "",
        "pago": pago,
        "reembolso": "Nao solicitado"
    }

    pedidos.append(pedido)

    print("\nPedido cadastrado com sucesso!")
    pausar()


# =========================================
# CADASTRAR ENTREGADOR
# =========================================

def cadastrar_entregador():
    limpar_tela()

    print("===== CADASTRO DE ENTREGADOR =====\n")

    valido = 0

    while valido == 0:
        id_entregador = ler_id_entregador()

        if buscar_entregador(id_entregador):
            print("\nEntregador ja cadastrado!")
        else:
            valido = 1

    nome = input("Nome do entregador: ")
    veiculo = ler_veiculo()

    entregador = {
        "id": id_entregador,
        "nome": nome,
        "veiculo": veiculo,
        "pedidos_ativos": [],
        "entregas_realizadas": []
    }

    entregadores.append(entregador)

    print("\nEntregador cadastrado com sucesso!")
    pausar()


# =========================================
# ASSOCIAR ENTREGADOR
# =========================================

def associar_entregador():
    limpar_tela()

    print("===== ASSOCIAR ENTREGADOR =====\n")

    pedido_encontrado = 0

    while pedido_encontrado == 0:
        id_pedido = input("Digite o ID do pedido: ").upper()
        pedido = buscar_pedido(id_pedido)

        if pedido == None:
            print("\nPedido nao encontrado!")
        else:
            pedido_encontrado = 1

    if pedido["status"] == "Cancelado":
        print("\nPedido cancelado nao pode ser associado!")
        pausar()
        return

    if pedido["status"] == "Entregue":
        print("\nPedido entregue nao pode ser associado novamente!")
        pausar()
        return

    if pedido["entregador"] != "":
        print("\nPedido ja possui entregador!")
        pausar()
        return

    entregador_encontrado = 0

    while entregador_encontrado == 0:
        id_entregador = ler_id_entregador()
        entregador = buscar_entregador(id_entregador)

        if entregador == None:
            print("\nEntregador nao encontrado!")
        else:
            entregador_encontrado = 1

    if len(entregador["pedidos_ativos"]) >= limite_pedidos_entregador(entregador):
        print("\nEntregador atingiu o limite de pedidos!")
        pausar()
        return

    pedido["entregador"] = id_entregador
    pedido["status"] = "Em Rota"

    entregador["pedidos_ativos"].append(id_pedido)

    print("\nEntregador associado com sucesso!")
    pausar()


# =========================================
# ATUALIZAR STATUS
# =========================================

def atualizar_status():
    limpar_tela()

    print("===== ATUALIZAR STATUS =====\n")

    encontrado = 0

    while encontrado == 0:
        id_pedido = input("Digite o ID do pedido: ").upper()
        pedido = buscar_pedido(id_pedido)

        if pedido == None:
            print("\nPedido nao encontrado!")
        else:
            encontrado = 1

    if pedido["status"] == "Cancelado":
        print("\nPedido cancelado nao pode ser reativado ou alterado.")
        pausar()
        return

    if pedido["status"] == "Entregue":
        print("\nPedido entregue nao pode ser alterado.")
        pausar()
        return

    print("1 - Pendente")
    print("2 - Em Rota")
    print("3 - Entregue")
    print("4 - Cancelado")

    opcao = input("\nEscolha o novo status: ")

    if opcao == "1":
        remover_pedido_ativo_do_entregador(pedido)
        pedido["entregador"] = ""
        pedido["status"] = "Pendente"

    elif opcao == "2":
        if pedido["entregador"] == "":
            print("\nPara colocar em rota, associe um entregador ao pedido.")
            pausar()
            return

        pedido["status"] = "Em Rota"

    elif opcao == "3":
        if pedido["entregador"] == "":
            print("\nPedido sem entregador nao pode ser marcado como entregue.")
            pausar()
            return

        if pedido["pago"] == "Nao":
            print("\nPedido nao pago nao pode ser marcado como entregue.")
            pausar()
            return

        pedido["status"] = "Entregue"
        registrar_entrega_realizada(pedido)
        remover_pedido_ativo_do_entregador(pedido)

    elif opcao == "4":
        remover_pedido_ativo_do_entregador(pedido)
        pedido["entregador"] = ""
        pedido["status"] = "Cancelado"
        processar_reembolso(pedido)

    else:
        print("\nOpcao invalida!")
        pausar()
        return

    print("\nStatus atualizado!")
    pausar()


# =========================================
# REMOVER ASSOCIACAO
# =========================================

def remover_associacao():
    limpar_tela()

    print("===== REMOVER ASSOCIACAO =====\n")

    encontrado = 0

    while encontrado == 0:
        id_pedido = input("Digite o ID do pedido: ").upper()
        pedido = buscar_pedido(id_pedido)

        if pedido == None:
            print("\nPedido nao encontrado!")
        else:
            encontrado = 1

    if pedido["entregador"] == "":
        print("\nPedido nao possui entregador!")
        pausar()
        return

    if pedido["status"] == "Entregue" or pedido["status"] == "Cancelado":
        print("\nNao e possivel remover associacao de pedido finalizado.")
        pausar()
        return

    remover_pedido_ativo_do_entregador(pedido)

    pedido["entregador"] = ""

    if pedido["status"] != "Entregue" and pedido["status"] != "Cancelado":
        pedido["status"] = "Pendente"

    print("\nAssociacao removida!")
    pausar()


# =========================================
# PEDIDOS PENDENTES
# =========================================

def pedidos_pendentes():
    limpar_tela()

    print("===== PEDIDOS PENDENTES =====")

    encontrou = 0

    pedidos_ordenados = sorted(pedidos, key=prioridade_valor)

    for pedido in pedidos_ordenados:
        if pedido["status"] == "Pendente":
            print("\n--------------------------")
            print("ID:", pedido["id"])
            print("Cliente:", pedido["cliente"])
            print("Prioridade:", pedido["prioridade"])
            print("Descricao:", pedido["descricao"])
            print("Pago:", pedido["pago"])

            encontrou = 1

    if encontrou == 0:
        print("\nNenhum pedido pendente.")

    pausar()


# =========================================
# PEDIDOS ENTREGUES
# =========================================

def pedidos_entregues():
    limpar_tela()

    print("===== PEDIDOS ENTREGUES =====")

    encontrou = 0

    for pedido in pedidos:
        if pedido["status"] == "Entregue":
            print("\n--------------------------")
            print("ID:", pedido["id"])
            print("Cliente:", pedido["cliente"])
            print("Entregador:", pedido["entregador"])
            print("Pago:", pedido["pago"])

            encontrou = 1

    if encontrou == 0:
        print("\nNenhum pedido entregue.")

    pausar()


# =========================================
# BUSCAR PEDIDO
# =========================================

def buscar_por_id():
    limpar_tela()

    print("===== BUSCAR PEDIDO =====\n")

    encontrado = 0

    while encontrado == 0:
        id_pedido = input("Digite o ID do pedido: ").upper()
        pedido = buscar_pedido(id_pedido)

        if pedido == None:
            print("\nPedido nao encontrado!")
        else:
            encontrado = 1

    print("\n===== DADOS DO PEDIDO =====")
    print("ID:", pedido["id"])
    print("Cliente:", pedido["cliente"])
    print("Endereco:", pedido["endereco"])
    print("Prioridade:", pedido["prioridade"])
    print("Descricao:", pedido["descricao"])
    print("Status:", pedido["status"])
    print("Pago:", pedido["pago"])
    print("Reembolso:", pedido["reembolso"])

    if pedido["entregador"] != "":
        entregador = buscar_entregador(pedido["entregador"])

        if entregador != None:
            print("Entregador:", entregador["nome"], "-", entregador["id"])
        else:
            print("Entregador:", pedido["entregador"])
    else:
        print("Entregador: Nenhum")

    pausar()


# =========================================
# ENTREGADORES DISPONIVEIS
# =========================================

def entregadores_disponiveis():
    limpar_tela()

    print("===== ENTREGADORES DISPONIVEIS =====")

    encontrou = 0

    for entregador in entregadores:
        if calcular_disponibilidade(entregador) == "Disponivel":
            print("\n--------------------------")
            print("ID:", entregador["id"])
            print("Nome:", entregador["nome"])
            print("Veiculo:", entregador["veiculo"])
            print("Pedidos ativos:", len(entregador["pedidos_ativos"]))
            print("Limite de pedidos:", limite_pedidos_entregador(entregador))
            print("Disponibilidade:", calcular_disponibilidade(entregador))

            encontrou = 1

    if encontrou == 0:
        print("\nNenhum entregador disponivel.")

    pausar()


# =========================================
# ENTREGAS POR ENTREGADOR
# =========================================

def entregas_por_entregador():
    limpar_tela()

    print("===== ENTREGAS POR ENTREGADOR =====\n")

    encontrado = 0

    while encontrado == 0:
        id_entregador = ler_id_entregador()
        entregador = buscar_entregador(id_entregador)

        if entregador == None:
            print("\nEntregador nao encontrado!")
        else:
            encontrado = 1

    print("\nNome:", entregador["nome"])
    print("Veiculo:", entregador["veiculo"])
    print("Limite de pedidos:", limite_pedidos_entregador(entregador))
    print("Disponibilidade:", calcular_disponibilidade(entregador))

    if len(entregador["pedidos_ativos"]) == 0:
        print("\nNenhum pedido ativo.")
    else:
        print("\nPedidos ativos:")

        for pedido_id in entregador["pedidos_ativos"]:
            print("-", pedido_id)

    if len(entregador["entregas_realizadas"]) == 0:
        print("\nNenhuma entrega realizada.")
    else:
        print("\nEntregas realizadas:")

        for pedido_id in entregador["entregas_realizadas"]:
            print("-", pedido_id)

    pausar()


# =========================================
# RELATORIOS
# =========================================

def relatorios():
    limpar_tela()

    print("===== RELATORIOS =====")

    total = len(pedidos)

    pendentes = 0
    em_rota = 0
    entregues = 0
    cancelados = 0
    alta = 0
    pagos = 0
    reembolsos = 0

    for pedido in pedidos:
        if pedido["status"] == "Pendente":
            pendentes += 1
        elif pedido["status"] == "Em Rota":
            em_rota += 1
        elif pedido["status"] == "Entregue":
            entregues += 1
        elif pedido["status"] == "Cancelado":
            cancelados += 1

        if pedido["prioridade"] == "Alta":
            alta += 1

        if pedido["pago"] == "Sim":
            pagos += 1

        if pedido["reembolso"] == "Gerado":
            reembolsos += 1

    print("\nTotal de pedidos:", total)
    print("Pedidos pendentes:", pendentes)
    print("Pedidos em rota:", em_rota)
    print("Pedidos entregues:", entregues)
    print("Pedidos cancelados:", cancelados)
    print("Pedidos alta prioridade:", alta)
    print("Pedidos pagos:", pagos)
    print("Reembolsos gerados:", reembolsos)

    if alta > 0:
        print("\nPedidos com alta prioridade:")

        for pedido in pedidos:
            if pedido["prioridade"] == "Alta":
                print("-", pedido["id"], "-", pedido["cliente"], "-", pedido["status"])

    maior_nome = ""
    maior_qtd = -1

    for entregador in entregadores:
        qtd_entregas = len(entregador["entregas_realizadas"])

        if qtd_entregas > maior_qtd:
            maior_qtd = qtd_entregas
            maior_nome = entregador["nome"]

    if maior_nome != "":
        print("Entregador com maior numero de entregas:", maior_nome)
        print("Quantidade de entregas:", maior_qtd)
    else:
        print("Entregador com maior numero de entregas: nenhum entregador cadastrado")

    pausar()


# =========================================
# MENU PRINCIPAL
# =========================================

opcao = -1

while opcao != 0:
    limpar_tela()

    print("=================================")
    print("         FLUXONORTE")
    print("=================================")
    print("1 - Pedidos")
    print("2 - Entregadores")
    print("3 - Relatorios")
    print("0 - Sair")

    entrada = input("\nEscolha uma opcao: ")

    if entrada.isdigit():
        opcao = int(entrada)

        if opcao == 1:
            menu_pedidos()
        elif opcao == 2:
            menu_entregadores()
        elif opcao == 3:
            menu_relatorios()
        elif opcao == 0:
            limpar_tela()
            print("Sistema encerrado!")
        else:
            print("\nOpcao invalida!")
            pausar()
    else:
        print("\nDigite apenas numeros!")
        pausar()
