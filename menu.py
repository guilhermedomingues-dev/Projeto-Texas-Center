import readEstoque
import readClientes
import funcoes
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

estoque = readEstoque.read_json()
clientes = readClientes.read_json()

def menu():
    funcoes.telaInicial()
    opcao = int(input("\nO que deseja fazer?: "))
    limpar()

    if opcao == 1:
        funcoes.cadastrarCliente()
    
    elif opcao == 2:
        funcoes.produtos()
          
    elif opcao == 3:
        funcoes.masculino()
        
    elif opcao == 4:
        funcoes.feminino()
            
    elif opcao == 5:
        funcoes.menuMarcas()

    elif opcao == 0:
        funcoes.loginDono()