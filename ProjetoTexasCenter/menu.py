import readJSON
import funcoes
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

estoque = readJSON.read_json() 

def menu():
            funcoes.telaInicial()
            opcao = int(input("\nO que deseja fazer?: "))
            limpar()
            
            if opcao == 1:
                funcoes.produtos()
            
            elif opcao == 2:
                funcoes.masculino()
            
            elif opcao == 3:
                funcoes.feminino()
            
            elif opcao == 4:
                funcoes.menuMarcas()