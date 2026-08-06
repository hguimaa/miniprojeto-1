import json

with open("respostas.json", encoding="utf-8") as f:
    respostas = json.load(f)

with open("gabarito_publico.json", encoding="utf-8") as f:
    gabarito = json.load(f)

erros = 0

for chave in sorted(gabarito, key=int):
    r = respostas.get(chave, "<não existe>")
    g = gabarito.get(chave, "<não existe>")

    if r != g:
        erros += 1
        print(f"[{chave}]")
        print(f"Esperado: {g}")
        print(f"Obtido:   {r}\n")

print(f"{erros} diferenças.")