# Exemplo de Acurácia e Precisão

Aplicativo para explicar a diferença entre acurácia e precisão.

Utiliza um gerador de números pseudoaletório para uma distribuição normal de média 200 e variância 0 em duas dimensões e exibe os pontos gerados numa tela de 400 x 400.

## Parâmetros

```
python3 main.py [--seed <seed>] [--dx <dx>] [--dy <dy>] [--sx <sx>] [--sy <sy>]
```

seed: semente para geração dos valores aleatórios.
dx: deslocamento no eixo **x** do gerador em torno da média (200).
dy: deslocamento no eixo **y** do gerador em torno da média (200).
sx: aumento da variância no eixo **x**.
sy: aumento da variância no eixo **y**.

## Dependências

```
python3 -m pip install -U pygame --user
```