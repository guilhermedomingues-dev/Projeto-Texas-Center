import json

path = "dataBase.json"

def read_json():
    with open(path, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        return dados

def save_json(path, dados):
    with open(path, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)