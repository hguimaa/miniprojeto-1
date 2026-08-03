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


def main():
    catalogo = Catalogo("catalogo_dev.json")

    mostrar_usuarios(catalogo)


if __name__ == "__main__":
    main()