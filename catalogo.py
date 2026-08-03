import json


class Catalogo:

    def __init__(self, caminho_json: str):
        with open(caminho_json, encoding="UTF-8") as arquivo:
            dados = json.load(arquivo)
        self.conteudos = dados["conteudos"]
        self.usuarios = dados["usuarios"]
    
    # -----Usuários e playlists-----
    def listar_usuarios(self) -> list[str]:
        usuarios_ordenados = []
        for usuario in self.usuarios:
            usuarios_ordenados.append(usuario["nome"])
        return sorted(usuarios_ordenados)

    def buscar_usuario_por_nome(self, nome: str) -> str | None:
        for usuario in self.usuarios:
            if nome.strip().lower() == usuario["nome"].lower():
                return usuario["id"]
        return None
    
    def buscar_usuario_por_id(self, usuario_id: str) -> str | None:
        for usuario in self.usuarios:
            if usuario["id"] == usuario_id:
                return usuario["nome"]
        return None

    def buscar_conteudo_por_id(self, conteudo_id: str) -> dict | None:
        for conteudo in self.conteudos:
            if conteudo["id"] == conteudo_id:
                return conteudo
        return None

    def playlist_de(self, usuario_id: str) -> list[str] | None:
        for usuario in self.usuarios:
            if usuario["id"] == usuario_id:
                return usuario["playlist"]
        return None
