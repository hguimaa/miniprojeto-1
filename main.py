import json
from catalogo import Catalogo


def main():
    catalogo = Catalogo("catalogo_final.json")

    with open("consultas.json", encoding="utf-8") as arquivo:
        consultas = json.load(arquivo)["consultas"]

    respostas = {}

    for consulta in consultas:
        metodo = getattr(catalogo, consulta["tipo"])
        parametros = consulta["parametros"]

        resultado = metodo(**parametros)

        respostas[str(consulta["id"])] = resultado

    with open("respostas.json", "w", encoding="utf-8") as arquivo:
        json.dump(respostas, arquivo, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()