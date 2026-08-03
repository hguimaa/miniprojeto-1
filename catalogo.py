import json


class Catalogo:

    def __init__(self, caminho_json: str):
        with open(caminho_json, encoding="UTF-8") as arquivo:
            dados = json.load(arquivo)
        self.conteudos = dados["conteudos"]
        self.usuarios = dados["usuarios"]
    
    def listar_usuarios(self) -> list[str]:
        usuarios_ordenados = []
        for usuario in self.usuarios:
            usuarios_ordenados.append(usuario["nome"])
        return sorted(usuarios_ordenados)