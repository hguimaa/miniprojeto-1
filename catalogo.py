import json


class Catalogo:

    def __init__(self, caminho_json: str):
        with open(caminho_json, encoding="UTF-8") as arquivo:
            dados = json.load(arquivo)
        self.conteudos = dados["conteudos"]
        self.usuarios = dados["usuarios"]

        self.conteudos_por_id = {}
        for conteudo in self.conteudos:
            self.conteudos_por_id[conteudo["id"]] = conteudo

        self.usuarios_por_id = {}
        self.usuarios_por_nome = {}

        for usuario in self.usuarios:
            self.usuarios_por_id[usuario["id"]] = usuario
            self.usuarios_por_nome[usuario["nome"].lower()] = usuario
    
    # -----Usuários e playlists-----
    def listar_usuarios(self) -> list[str]:
        usuarios_ordenados = []
        for usuario in self.usuarios:
            usuarios_ordenados.append(usuario["nome"])
        return sorted(usuarios_ordenados)

    def buscar_usuario_por_nome(self, nome: str) -> str | None:
        usuario = self.usuarios_por_nome.get(nome.strip().lower())
        return usuario["id"] if usuario else None
    
    def buscar_conteudo_por_id(self, conteudo_id: str) -> dict | None:
        return self.conteudos_por_id.get(conteudo_id)

    def playlist_de(self, usuario_id: str) -> list[str] | None:
        usuario = self.usuarios_por_id.get(usuario_id)
        return usuario["playlist"] if usuario else None
    
    def conteudo_na_posicao(self, usuario_id: str, posicao: int) -> str | None:
        playlist = self.playlist_de(usuario_id)

        if playlist is None:
            return None

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

        return sorted(intersecao)

    # -----Dados de um conteúdo-----
    def rating_de(self, conteudo_id: str) -> float | None:
        conteudo = self.conteudos_por_id.get(conteudo_id)

        if conteudo is None:
            return None
        
        rating = conteudo.get("rating")
        
        return float(rating) if rating is not None else None
    
    def duracao_total_de(self, conteudo_id: str) -> int | None:
        conteudo = self.conteudos_por_id.get(conteudo_id)

        if conteudo is None:
            return None

        if conteudo["tipo"] == "musica":
            return conteudo.get("duracao_seg")

        total_secs = 0
        for musica in conteudo["faixas"]:
            duracao = musica.get("duracao_seg")
            
            if duracao is not None:
                total_secs += duracao

        return total_secs

    def achatar_generos(self, generos, resultado):
        for genero in generos:
            if isinstance(genero, list):
                self.achatar_generos(genero, resultado)
            else:
                resultado.append(genero)
    def generos_de(self, conteudo_id: str) -> list[str]:
        conteudo = self.conteudos_por_id.get(conteudo_id)

        if conteudo is None:
            return []

        generos = conteudo.get("generos")

        if generos is None:
            return []

        if isinstance(generos, str):
            return [generos]

        lista_generos = []
        self.achatar_generos(generos, lista_generos)
        return lista_generos