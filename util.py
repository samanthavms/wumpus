import os


def limpar_tela():
    """
    Limpa o terminal (Windows / Linux / Mac)
    """
    if os.name == "nt":      # Windows
        os.system("cls")
    else:                    # Linux / Mac
        os.system("clear")


def mostrar_menu():
    print("====== MENU ======")
    print("N - Mover para o Norte")
    print("S - Mover para o Sul")
    print("L - Mover para o Leste")
    print("O - Mover para o Oeste")
    print("P - Pegar ouro")
    print("F - Atirar flecha")
    print("X - Sair do jogo")


def mostrar_percepcoes(celula):
    if "B" in celula:
        print("🌬️ Você sente uma brisa.")
    if "F" in celula:
        print("😷 Você sente um fedor.")
    if "O" in celula:
        print("✨ Você vê um brilho.")
