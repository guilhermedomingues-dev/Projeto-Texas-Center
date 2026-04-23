import json

path = r'C:\Users\USUARIO\Documents\ProjetoTexasCenter\clientes.json'

def read_json():
    with open(path, "r", encoding="utf-8") as arquivo:
        clientes = json.load(arquivo)
        return clientes

def save_json(path, clientes):
    with open(path, "w", encoding="utf-8") as arquivo:
        json.dump(clientes, arquivo, ensure_ascii=False, indent=2)