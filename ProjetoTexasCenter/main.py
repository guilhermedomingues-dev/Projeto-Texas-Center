import menu
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    limpar()
    print("Seja bem-vindo(a) ao sistema TEXAS CENTER...\n")
    menu.menu()