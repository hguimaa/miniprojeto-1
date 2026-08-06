# Decisões de Arquitetura

## Indexação dos dados

Durante a inicialização da classe `Catalogo`, são construídos dicionários auxiliares para acesso rápido aos dados:

- `conteudos_por_id`
- `usuarios_por_id`
- `usuarios_por_nome`
- `conteudos_por_genero`

Esses índices substituem buscas lineares repetidas por acessos diretos em tempo constante (`O(1)`), melhorando o desempenho das consultas frequentes.

---

## Tratamento de dados inconsistentes

Alguns campos do catálogo possuem formatos diferentes dependendo do conteúdo (por exemplo, gêneros podem aparecer como string, lista ou listas aninhadas).

Para lidar com isso foi criada uma função recursiva (`achatar_generos`) responsável por normalizar essas estruturas antes de retorná-las às demais funções do sistema.

---

## Interseção de playlists

A interseção entre playlists foi implementada utilizando conjuntos (`set`).

A primeira playlist é convertida em conjunto e, em seguida, é feita a interseção sucessiva com as demais playlists utilizando o operador `&=`.

Essa abordagem simplifica a implementação e possui melhor desempenho do que comparar todos os elementos manualmente.

---

## Execução das consultas

O `main.py` utiliza `getattr` para localizar dinamicamente o método correspondente ao tipo de consulta presente em `consultas.json`.

Dessa forma, não é necessário manter uma sequência de `if`/`elif` para cada operação, tornando a solução mais simples e facilmente extensível caso novas consultas sejam adicionadas.