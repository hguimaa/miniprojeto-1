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

def mostrar_playlist(catalogo, nome_usuario: str):
    id_usuario = catalogo.buscar_usuario_por_nome(nome_usuario)
    playlist = catalogo.playlist_de(id_usuario)

    print(f'Playlist de {nome_usuario} ({len(playlist)} músicas)\n')

    for i, conteudo_id in enumerate(playlist, start=1):
        conteudo = catalogo.buscar_conteudo_por_id(conteudo_id)
        print(f'{i}. {conteudo["titulo"]} — {conteudo["artista"]} ({conteudo["tipo"]})')

def main():
    catalogo = Catalogo("catalogo_dev.json")



if __name__ == "__main__":
    main()