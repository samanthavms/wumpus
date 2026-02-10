def criar_mundo():
    mundo = [
        [("V",), ("B",), ("P",), ("B",)],
        [("F",), ("V",), ("B",), ("V",)],
        [("W",), ("F",), ("V",), ("B",)],
        [("F",), ("V",), ("B",), ("O",)]
    ]
    return mundo


def obter_celula(mundo, posicao):
    linha, coluna = posicao
    return mundo[linha][coluna]


def verificar_perigos(mundo, agente):
    celula = obter_celula(mundo, agente["posicao"])

    if "P" in celula or "W" in celula:
        agente["vivo"] = False
        print("VOCÊ MORREU!")
def matar_wumpus(mundo, posicao):
    linha, coluna = posicao
    celula = mundo[linha][coluna]

    if "W" in celula:
        mundo[linha][coluna] = ("V",)
        print(" Você matou o Wumpus!")
        return True

    return False
