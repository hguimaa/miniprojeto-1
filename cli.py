from catalogo import Catalogo


def mostrar_usuarios(catalogo):
    usuarios = catalogo.listar_usuarios()

    print(f"Exibindo os {len(usuarios)} usuários em ordem alfabética:\n")

    colunas = 3

    for i in range(0, len(usuarios), colunas):
        linha = usuarios[i:i + colunas]

        for usuario in linha:
            print(f"{usuario:<20}", end="")

        print()

def mostrar_playlist(catalogo):
    nome_usuario = input("Nome do usuário: ")
    id_usuario = catalogo.buscar_usuario_por_nome(nome_usuario)
    playlist = catalogo.playlist_de(id_usuario)

    print(f'Playlist de {nome_usuario} ({len(playlist)} músicas)\n')

    for i, conteudo_id in enumerate(playlist, start=1):
        conteudo = catalogo.buscar_conteudo_por_id(conteudo_id)
        print(f'{i}. {conteudo["titulo"]} — {conteudo["artista"]} ({conteudo["tipo"]})')
    
def mostrar_posicao(catalogo):
    nome_usuario = input("Nome do usuário: ").strip().lower()
    id_usuario = catalogo.buscar_usuario_por_nome(nome_usuario)
    playlist = catalogo.playlist_de(id_usuario)
    print(f"Playlist de {nome_usuario} tem {len(playlist)} itens. (Posições de 1 a {len(playlist)})")

    try:
        posicao = int(input("Posição: "))
    except ValueError:
        print("Insira uma posição válida.")
        return
    id_conteudo = catalogo.conteudo_na_posicao(id_usuario, posicao)
    conteudo = catalogo.buscar_conteudo_por_id(id_conteudo)

    print(f'Posição {posicao} de {nome_usuario}: {conteudo["titulo"]} — {conteudo["artista"]} ({conteudo["tipo"]})')

def mostrar_intersecao(catalogo):
    nomes_usuarios = input("Nome dos usuários separados por vírgula (Ex: Nicholas, Uchoa): ")
    lista_nomes = [nome.strip().lower() for nome in nomes_usuarios.split(",")]
    usuarios_ids = []
    for nome_usuario in lista_nomes:
        usuarios_ids.append(catalogo.buscar_usuario_por_nome(nome_usuario.strip().lower()))
    
    intersecao = catalogo.intersecao_playlists(usuarios_ids)

    if not intersecao:
        print("Sem interseção.")
        return
    
    print(f"Interseção {len(intersecao)} conteúdos:")
    for id_conteudo in intersecao:
        conteudo = catalogo.buscar_conteudo_por_id(id_conteudo)
        print(f"- {conteudo["titulo"]} — {conteudo["artista"]} — {conteudo["tipo"]} — {conteudo["id"]}")

def main():
    catalogo = Catalogo("catalogo_dev.json")


if __name__ == "__main__":
    main()