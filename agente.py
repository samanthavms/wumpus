def inicializar_agente():
    return {
        "posicao": (0, 0),          # tupla ✔
        "vivo": True,
        "flechas": 1,
        "ouro": False,
        "historico": [(0, 0)]
    }


def mover(agente, direcao):
    linha, coluna = agente["posicao"]

    if direcao == "N":
        if linha > 0:
            linha -= 1
        else:
            print("Limite do mapa!")
    elif direcao == "S":
        if linha < 3:
            linha += 1
        else:
            print("Limite do mapa!")
    elif direcao == "L":
        if coluna < 3:
            coluna += 1
        else:
            print("Limite do mapa!")
    elif direcao == "O":
        if coluna > 0:
            coluna -= 1
        else:
            print("Limite do mapa!")

    agente["posicao"] = (linha, coluna)
    agente["historico"].append((linha, coluna))
