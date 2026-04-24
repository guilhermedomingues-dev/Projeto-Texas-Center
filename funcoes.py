import readEstoque
import readClientes
import menu
import os
from datetime import datetime

estoque = readEstoque.read_json()
clientes = readClientes.read_json()

def telaInicial():
    print("=====TEXAS CENTER=====")
    print("|1- Produtos")
    print("|2- Masculino")
    print("|4- Feminino")
    print("|4- Marcas")
    print("|0- Configurações")

def data_hora():
    agora = datetime.now()
    print(agora.strftime("%d/%m/%Y %H:%M:%S"))

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def produtos():

    print("=====PRODUTOS=====")
    for produto in estoque["produtos"]:
        print(produto["id"],"-",produto["nome"])
    print("\n0 - Tela inicial")
             
    opcao = int(input("\n Qual produto deseja ver?: "))
    limpar()

    if opcao == 0:
        menu.menu()

    else:
        produto_encontrado = None
        for produto in estoque["produtos"]:
            if produto["id"] == opcao:
                produto_encontrado = produto
                break

        if produto_encontrado:
            print("=====", produto_encontrado["nome"], "=====")
            print("|Marca:", produto_encontrado["marca"])
            print("|Marca:", produto["marca"])
            print("|Gênero:", produto["genero"])
            print("|Tamanhos:", produto["tamanhos_disponiveis"])
            print("|Cores:", produto["cores"])
            if produto["estoque"]>=1:
                print("|Estoque: Disponível(", produto["estoque"],"un.)")
            else:
                print("|Estoque: Indisponível")
            print("|Preço: R$", produto["preco_original"])
            print("|Link: ", produto["link"])
            
            opcao= str(input("\nDeseja comprar?(S/N): ")).capitalize()
            limpar()
            if opcao=="S":
                comprar(produto)
            else:
                produtos()

        else:
            print("Produto não encontrado.")
            print("=======================")
            menu.menu()

def masculino():
    print("=====MASCULINO=====")

    masculinos = [p for p in estoque["produtos"] if p["genero"] in ("Masculino", "Unissex")]

    for produto in masculinos:
        print(produto["id"], "-", produto["nome"])

    print("\n0 - Tela inicial")

    opcao = int(input("\nQual produto deseja ver?: "))
    limpar()

    if opcao == 0:
        menu.menu()
    else:
        produto_encontrado = None
        for produto in masculinos:
            if produto["id"] == opcao:
                produto_encontrado = produto
                break

        if produto_encontrado:
            print("=====", produto_encontrado["nome"], "=====")
            print("|Marca:", produto_encontrado["marca"])
            print("|Gênero:", produto_encontrado["genero"])
            print("|Tamanhos:", produto_encontrado["tamanhos_disponiveis"])
            print("|Cores:", produto_encontrado["cores"])
            if produto_encontrado["estoque"] >= 1:
                print("|Estoque: Disponível (", produto_encontrado["estoque"], "un.)")
            else:
                print("|Estoque: Indisponível")
            print("|Preço: R$", produto_encontrado["preco_original"])

            opcao = str(input("\nDeseja comprar?(S/N): ")).capitalize()
            limpar()
            if opcao == "S":
                comprar(produto_encontrado, estoque)
        
        else:
                print("Produto não encontrado.")
                print("=======================")
                menu.menu()

def feminino():
    print("=====FEMININO=====")

    femininos = [p for p in estoque["produtos"] if p["genero"] in ("Feminino", "Unissex")]

    for produto in femininos:
        print(produto["id"], "-", produto["nome"])

    print("\n0 - Tela inicial")

    opcao = int(input("\nQual produto deseja ver?: "))
    limpar()

    if opcao == 0:
        menu.menu()
    else:
        produto_encontrado = None
        for produto in femininos:
            if produto["id"] == opcao:
                produto_encontrado = produto
                break

        if produto_encontrado:
            print("=====", produto_encontrado["nome"], "=====")
            print("|Marca:", produto_encontrado["marca"])
            print("|Gênero:", produto_encontrado["genero"])
            print("|Tamanhos:", produto_encontrado["tamanhos_disponiveis"])
            print("|Cores:", produto_encontrado["cores"])
            if produto_encontrado["estoque"] >= 1:
                print("|Estoque: Disponível (", produto_encontrado["estoque"], "un.)")
            else:
                print("|Estoque: Indisponível")
            print("|Preço: R$", produto_encontrado["preco_original"])

            opcao = str(input("\nDeseja comprar?(S/N): ")).capitalize()
            limpar()
            if opcao == "S":
                comprar(produto_encontrado, estoque)
        
        else:
                print("Produto não encontrado.")
                print("=======================")
                menu.menu()

def menuMarcas():
    print("=====MARCAS=====")
    indice = 1
                
    marcas = []

    for p in estoque["marcas"]:
        marcas.append(p)
    
    for indice, marca in enumerate(marcas, start=1):
        print(indice, "-", marca)

    print("\n0 - Tela inicial")
             
    opcao = int(input("\n Qual marca deseja ver?: "))
    limpar()

    if opcao == 0:
        menu.menu()

    if opcao <= len(marcas):
        marca = marcas[opcao - 1]
        filtrados = [p for p in estoque["produtos"] if p["marca"] == marca]

        print("=====", marca,"=====")
        for indice, produto in enumerate(filtrados, start=1):
            print(indice, "-", produto["nome"])
        
        print("\n0 - Marcas")
    
        opcao = int(input("\nQual produto deseja ver?: "))
        limpar()

        if opcao == 0:
            menuMarcas()

        if opcao <= len(filtrados):
            produto = filtrados[opcao - 1]
            print("=====", produto["nome"], "=====")
            print("Marca:", produto["marca"])
            print("Gênero:", produto["genero"])
            print("Tamanhos:", produto["tamanhos_disponiveis"])
            print("Cores:", produto["cores"])
            if produto["estoque"]>=1:
                print("Estoque: Disponível(", produto["estoque"],"un.)")
            else:
                print("Estoque: Indisponível")
            print("Preço: R$", produto["preco_original"])
            print("Link: ", produto["link"])
            
            opcao= str(input("\nDeseja comprar?(S/N): ")).capitalize()
            limpar()
            if opcao=="S":
                comprar(produto)
            else:
                menuMarcas()

    else:
        print("=====TEXAS CENTER=====")
        print("Opção inválida.\n")
        print("----------------------")
        menu.menu()

def comprar(produto):
    preco=[]
    print("=====COMPRAR=====")
    if produto["estoque"]>=1:
        print("Produto: ",produto["nome"])
        print("Preço: R$", produto["preco_original"])
        print("Estoque: Disponível(", produto["estoque"],"un.)")
        quantidade = int(input("Quantidade desejada: "))
        limpar()
        while quantidade>produto["estoque"] or quantidade<1:
            print("=====COMPRAR=====")
            print("Produto: ",produto["nome"])
            print("Preço: R$", produto["preco_original"])
            print("Estoque: Disponível(", produto["estoque"],"un.)")
            print("Quantidade inválida! Tente outra quantidade.")
            quantidade = int(input("Quantidade desejada: "))
            limpar()
    else:
        print("Produto indisponível no estoque...")
        print("Voltará em breve!")
        print("Veja outros produtos.")
        produtos()

    preco=produto["preco_original"]*quantidade
    print("==========")
    print("Final compra: R$", preco)
    print("1- Débito")
    print("2- Crétido")
    print("3- PIX")
    pagamento=int(input("Informe a forma de pagamento: "))
    cpf=int(input("Informe seu CPF: "))
    produto["estoque"]-=quantidade
    readEstoque.save_json("dataBase.json", estoque)
       
    if pagamento==1:
        limpar()
        print("=====TEXAS CENTER=====")
        print("A Disneylândia do Agro")
        print("Setor Sul, Goiânia - GO")
        print("----------------------")
        print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print("----------------------")
        print("CPF Cliente: ", cpf)
        print("Preço unitário: R$", produto["preco_original"])
        print("Quantidade: ",quantidade)
        print("Valor compra: R$",preco)
        print("Forma de pagamento: Débito")
        print("Valor final: R$",preco)
        print("----------------------")
        print("Descontos: R$0.00")
        print("----------------------")
        print("Obrigado pela prefrência!\n")
    elif pagamento == 2:
        limpar()
        print("=====TEXAS CENTER=====")
        print("A Disneylândia do Agro")
        print("Setor Sul, Goiânia - GO")
        print("----------------------")
        print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print("----------------------")
        print("CPF Cliente: ", cpf)
        print("Preço unitário: R$", produto["preco_original"])
        print("Quantidade: ",quantidade)
        print("Valor compra:  R$",preco)
        print("Forma de pagamento: Crédito")
        print("Descontos: R$0.00")
        print("----------------------")
        print("Valor final: R$",preco)
        print("----------------------")
        print("Obrigado pela prefrência!\n")
    elif pagamento==3:
        desconto = preco*(produto["desconto_pix"])
        precofinal = preco - desconto
        limpar()
        print("=====TEXAS CENTER=====")
        print("A Disneylândia do Agro")
        print("Setor Sul, Goiânia - GO")
        print("----------------------")
        print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print("----------------------")
        print("CPF Cliente: ", cpf)
        print("Preço unitário: R$", produto["preco_original"])
        print("Quantidade: ",quantidade)
        print(f"Valor compra: R${preco:.2f}")
        print("Forma de pagamento: PIX")
        print(f"Descontos: R${desconto:.2f}")
        print("----------------------")
        print(f"Valor final: R${precofinal:.2f}")
        print("----------------------")
        print("Obrigado pela prefrência!\n")

def loginDono():
    print("=====TEXAS CENTER=====")
    senha = ""
    while senha != estoque["loja"]["senha"]:
        senha = str(input("Informe a senha: "))
        limpar()
        if senha == estoque["loja"]["senha"]:
            menuDono()
        else:
            print("=====TEXAS CENTER=====")
            print("Senha incorreta! Tente novamente!\n")

def menuDono():
    print("=====Olá,", estoque["loja"]["dono"],"=====")
    print("|1- Conferir todo estoque")
    print("|2- Adicionar peças ao estoque")
    print("|3- Adicionar um novo produto ao estoque")
    print("|4- Conferir clientes")

    opcao = int(input("O que deseja fazer?: "))
    limpar()
    if opcao == 1:
        conferirEstoque(estoque)

def cadastrarCliente():
    print("=====TEXAS CENTER=====")
    email = str(input("Informe seu email: "))
    nome = str(input("Informe seu nome: ")).capitalize()
    senha = input("Crie uma senha: ")
    id = len(clientes["clientes"]) + 1
    
    novo_cliente={
        "id": id,
        "email": email,
        "nome": nome,
        "senha": senha
    }

    clientes["clientes"].append(novo_cliente)
    readClientes.save_json(clientes)
    limpar()
    
    print("=====TEXAS CENTER=====")
    print("Olá,",novo_cliente["nome"],"! Seja bem vindo à TEXAS CENTER!")
    input("Aperte 'enter' para ir ao menu: ")
    limpar()
    menu.menu()

def loginCliente():
    print("=====TEXAS CENTER=====")
    email = str(input("Informe seu email: "))
    cliente_encontrado = None

    for cliente in clientes["clientes"]:
        if cliente["email"] == email:
            cliente_encontrado = cliente
            break

    if cliente_encontrado:
        while True:
            senha = input("Informe sua senha: ")
            
            if senha == cliente_encontrado["senha"]:
                limpar()
                print("=====TEXAS CENTER=====")
                print("Olá,", cliente_encontrado["nome"], "!")
                input("Aperte 'enter' para ir ao menu: ")
                limpar()
                menu.menu()
                break
            else:
                limpar()
                print("=====TEXAS CENTER=====")
                print("Senha incorreta.")
                print("1- Tentar novamente")
                print("2- Esqueci minha senha")
                opcao = int(input("O que deseja fazer?: "))
                print("======================")
                if opcao == 2:
                    limpar()
                    esqueceuSenha()
                    break

    else:
        print("Email não encontrado.")
        print("1- Tentar novamente")
        print("2- Cadastrar-se")
        opcao = int(input("O que deseja fazer?: "))
        limpar()
        if opcao == 1:
            loginCliente()
        elif opcao == 2:
            cadastrarCliente()

def menuInicial():
    print("=====TEXAS CENTER=====")
    print("|1- Cadastre-se")
    print("|2- Já é cadastrado")
    opcao = int(input("O que deseja fazer?: "))
    limpar()
    if opcao == 1:
        cadastrarCliente()
    elif opcao == 2:
        loginCliente()
    elif opcao == 0:
        loginDono()
    else:
        print("Entrada inválida...\n")
        menuInicial()

def esqueceuSenha():
    clientes = readClientes.read_json()
    
    print("=====REDEFINIR SENHA=====")
    email = str(input("Informe seu email: "))
    
    cliente_encontrado = None
    for cliente in clientes["clientes"]:
        if cliente["email"] == email:
            cliente_encontrado = cliente
            break
    
    if cliente_encontrado:
        while True:
            nova_senha = input("Digite a nova senha: ")
            confirmar  = input("Confirme a nova senha: ")
            
            if not nova_senha.strip():
                print("A senha não pode ser vazia.")
            elif nova_senha == cliente_encontrado["senha"]:
                print("A nova senha não pode ser igual à atual.")
            elif nova_senha != confirmar:
                print("As senhas não coincidem. Tente novamente.")
            else:
                cliente_encontrado["senha"] = nova_senha
                readClientes.save_json(clientes)
                print("Senha redefinida com sucesso!")
                input("Aperte 'enter' para ir ao menu: ")
                limpar()
                menu.menu()
                break
    else:
        print("Email não encontrado.")
        input("Aperte 'enter' para tentar novamente: ")
        limpar()
        esqueceuSenha()

def conferirEstoque(estoque):
    print("=====TEXAS CENTER - ESTOQUE=====")
    for produto in estoque["produtos"]:
        print(produto["id"],"|",produto["nome"],"| R$",produto["preco_original"],"|",produto["desconto_pix"],"%|",produto["estoque"],"un.")



