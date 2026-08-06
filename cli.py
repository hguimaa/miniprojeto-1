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

def mostrar_dados_conteudo(catalogo):
    id_conteudo = input("ID do conteúdo (ex.: t000001): ").strip().lower()

    conteudo = catalogo.buscar_conteudo_por_id(id_conteudo)

    if conteudo is not None:
        print(f'{conteudo["titulo"]} — {conteudo["artista"]} ({conteudo["tipo"]})')
    else:
        print("Conteúdo: —")

    rating = catalogo.rating_de(id_conteudo)
    print(f'rating: {rating if rating is not None else "—"}')

    duracao_secs = catalogo.duracao_total_de(id_conteudo)
    if duracao_secs is not None:
        minutos = duracao_secs // 60
        segundos = duracao_secs % 60
        duracao = f"{minutos}m{segundos}s"
    else:
        duracao = "—"
    print(f'duração: {duracao}')

    generos = catalogo.generos_de(id_conteudo)
    print(f'gêneros: {", ".join(generos) if generos else "—"}')

    plataformas = catalogo.plataformas_de(id_conteudo)
    print(f'plataformas: {", ".join(plataformas) if plataformas else "—"}')

    data = catalogo.data_adicionado_de(id_conteudo)
    print(f'adicionado em: {data if data is not None else "—"}')

    if conteudo is not None and conteudo["tipo"] == "musica":
        execucoes = catalogo.execucoes_de(id_conteudo)

        if execucoes is not None:
            execucoes = f"{execucoes:,}".replace(",", ".")

        print(f"execuções: {execucoes if execucoes is not None else '—'}")

def mostrar_conteudos_do_genero(catalogo):
    genero = input("Gênero (ex.: Pop): ").strip()

    conteudos_ids = catalogo.conteudos_do_genero(genero)

    print(f'\n{len(conteudos_ids)} conteúdos em "{genero}":\n')

    for conteudo_id in conteudos_ids:
        conteudo = catalogo.buscar_conteudo_por_id(conteudo_id)
        print(f'- {conteudo["titulo"]} — {conteudo["artista"]} ({conteudo["tipo"]}) ({conteudo["id"]})')

def enfileirar_conteudo(catalogo):
    id_conteudo = input("ID do conteúdo (ex.: t000001): ").strip()

    conteudo = catalogo.buscar_conteudo_por_id(id_conteudo)

    if conteudo is None:
        print(f"Conteúdo {id_conteudo} não existe.")
        return
    catalogo.enfileirar(id_conteudo)
    print(f'Enfileirado: {conteudo["titulo"]} — {conteudo["artista"]} — ({conteudo["tipo"]})')

def tocar_proximo(catalogo):
    conteudo = catalogo.buscar_conteudo_por_id(catalogo.fila_atual[0])
    if not catalogo.fila_atual:
        print("Fila vazia.")
        return
    print(f'Tocando: {conteudo["titulo"]} — {conteudo["artista"]} — ({conteudo["tipo"]})')
    catalogo.proximo()

def mostrar_fila(catalogo):
    if not catalogo.fila_atual:
        print("Fila vazia.")
        return
    print(f'\nFila atual ({len(catalogo.fila_atual)} itens, próximo primeiro):')
    for i, conteudo_id in enumerate(catalogo.fila_atual, start = 1):
        conteudo = catalogo.buscar_conteudo_por_id(conteudo_id)
        print(f'{i}. {conteudo["titulo"]} — {conteudo["artista"]} ({conteudo["tipo"]})')

def main():
    catalogo = Catalogo("catalogo_dev.json")
if __name__ == "__main__":
    main()