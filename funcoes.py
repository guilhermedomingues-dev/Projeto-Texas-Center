import readEstoque
import readClientes
import menu
import os
from datetime import datetime

estoque = readEstoque.read_json()
clientes = readClientes.read_json()

def telaInicial():
    print("=====TEXAS CENTER=====")
    print("|1- Cadastrar cliente")
    print("|2- Produtos")
    print("|3- Masculino")
    print("|4- Feminino")
    print("|5- Marcas")
    print("|0- Configurações")

def data_hora():
    agora = datetime.now()
    print(agora.strftime("%d/%m/%Y %H:%M:%S"))

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def produtos():

    indice = 1
    print("=====PRODUTOS=====")
    for produto in estoque["produtos"]:
        print(indice,"-",produto["nome"])
        indice+=1
    print("\n0 - Tela inicial")
             
    opcao = int(input("\n Qual produto deseja ver?: "))
    limpar()

    if opcao == 0:
        menu.menu()

    elif opcao <= len(estoque["produtos"]):
        produto = estoque["produtos"][opcao - 1]
        print("=====", produto["nome"], "=====")
        print("|Marca:", produto["marca"])
        print("|Gênero:", produto["genero"])
        print("|Tamanhos:", produto["tamanhos_disponiveis"])
        print("|Cores:", produto["cores"])
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
            produtos()

    else:
        print("=====TEXAS CENTER=====")
        print("Opção inválida.\n")
        print("----------------------")
        menu.menu()

def masculino():
    print("=====MASCULINO=====")
    indice = 1

    masculinos = []

    for p in estoque["produtos"]:
        if p["genero"] in ("Masculino", "Unissex"):
            masculinos.append(p)
    
    for indice, produto in enumerate(masculinos, start=1):
        print(indice, "-", produto["nome"])
                
    print("\n0 - Tela inicial")
             
    opcao = int(input("\n Qual produto deseja ver?: "))
    limpar()

    if opcao == 0:
        menu.menu()
                
    if opcao <= len(masculinos):
        produto = masculinos[opcao - 1]
        print("=====", produto["nome"], "=====")
        print("Marca:", produto["marca"])
        print("Gênero:", produto["genero"])
        print("Tamanhos:", produto["tamanhos_disponiveis"])
        print("Cores:", produto["cores"])
        if produto["estoque"] >= 1:
            print("Estoque: Disponível (", produto["estoque"], "un.)")
        else:
            print("Estoque: Indisponível")
        print("Preço: R$", produto["preco_original"])
        print("Link: ", produto["link"])
        
        opcao= str(input("\nDeseja comprar?(S/N): ")).capitalize()
        limpar()
        if opcao=="S":
            comprar(produto)
        else:
            masculino()
    else:
        print("=====TEXAS CENTER=====")
        print("Opção inválida.\n")
        print("----------------------")
        menu.menu()

def feminino():
    print("=====FEMININO=====")
    indice = 1
                
    femininos = []

    for p in estoque["produtos"]:
        if p["genero"] in ("Feminino", "Unissex"):
            femininos.append(p)
    
    for indice, produto in enumerate(femininos, start=1):
            print(indice, "-", produto["nome"])
                
    print("\n0 - Tela inicial")
             
    opcao = int(input("\n Qual produto deseja ver?: "))
    limpar()

    if opcao == 0:
        menu.menu()
                
    if opcao <= len(femininos):
        produto = femininos[opcao - 1]
        print("=====", produto["nome"], "=====")
        print("Marca:", produto["marca"])
        print("Gênero:", produto["genero"])
        print("Tamanhos:", produto["tamanhos_disponiveis"])
        print("Cores:", produto["cores"])
        if produto["estoque"] >= 1:
            print("Estoque: Disponível (", produto["estoque"], "un.)")
        else:
            print("Estoque: Indisponível")
        print("Preço: R$", produto["preco_original"])
        print("Link: ", produto["link"])

        opcao= str(input("\nDeseja comprar?(S/N): ")).capitalize()
        limpar()
        if opcao=="S":
            comprar(produto)
        else:
            feminino()
    else:
        print("=====TEXAS CENTER=====")
        print("Opção inválida.\n")
        print("----------------------")
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
    nomeUsuario=str(input("Informe seu nome: ")).capitalize()
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
        print("Cliente: ", nomeUsuario)
        print("Preço unitário: R$", produto["preco_original"])
        print("Quantidade: ",quantidade)
        print("Valor compra: ", preco)
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
        print("Cliente: ", nomeUsuario)
        print("Preço unitário: R$", produto["preco_original"])
        print("Quantidade: ",quantidade)
        print("Valor compra: ", preco)
        print("Forma de pagamento: Crédito")
        print("Descontos: R$0.00")
        print("----------------------")
        print("Valor final: R$",preco)
        print("----------------------")
        print("Obrigado pela prefrência!\n")
    elif pagamento==3:
        desconto = preco*(produto["desconto_pix"]/100)
        precofinal = preco - desconto
        limpar()
        print("=====TEXAS CENTER=====")
        print("A Disneylândia do Agro")
        print("Setor Sul, Goiânia - GO")
        print("----------------------")
        print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print("----------------------")
        print("Cliente: ", nomeUsuario)
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
            print("Senha incorrte! Tente novamente!\n")

def menuDono():
    print("=====Olá,", estoque["loja"]["dono"],"=====")

def cadastrarCliente():
    print("=====TEXAS CENTER=====")
    email = str(input("Informe seu email: "))
    nome = str(input("Informe seu nome: ")).capitalize()
    senha = input("Cire uma senha: ")
    
    novo_cliente={
        "email": email,
        "nome": nome,
        "senha": senha
    }

    clientes["clientes"].append(novo_cliente)
    readClientes.save_json(clientes)
    print("Cadastrado com sucesso!")