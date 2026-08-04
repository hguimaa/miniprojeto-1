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
    
    def conteudo_na_posicao(self, usuario_id: str, posicao: int) -> str | None:
        playlist = self.playlist_de(usuario_id)

        if posicao < 1 or posicao > len(playlist):
            return None

        return playlist[posicao - 1]
    
    def intersecao_playlists(self, usuario_ids: list[str]) -> list[str]:
        if len(usuario_ids) < 2:
            return []

        playlists = []

        for usuario_id in usuario_ids:
            playlist = self.playlist_de(usuario_id)

            if playlist is None:
                return []

            playlists.append(playlist)

        intersecao = set(playlists[0])

        for playlist in playlists[1:]:
            intersecao &= set(playlist)

        return sorted(list(intersecao))
