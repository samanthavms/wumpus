import sys
import os
import time

sys.path.append(os.path.dirname(__file__))

from agente import inicializar_agente, mover
from mundo import criar_mundo, obter_celula, verificar_perigos, matar_wumpus
from util import limpar_tela, mostrar_menu, mostrar_percepcoes


def main():
    mundo = criar_mundo()
    agente = inicializar_agente()

    while agente["vivo"] and not agente["ouro"]:
        limpar_tela()

        print("=== MUNDO DO WUMPUS ===")
        print("Posição atual:", agente["posicao"])
        print("Flechas:", agente["flechas"])

        celula = obter_celula(mundo, agente["posicao"])
        mostrar_percepcoes(celula)

        print()
        mostrar_menu()
        acao = input("\nEscolha uma ação: ").upper()

        # MOVIMENTO
        if acao in ["N", "S", "L", "O"]:
            mover(agente, acao)
            verificar_perigos(mundo, agente)
            time.sleep(1)

        # PEGAR OURO
        elif acao == "P":
            if "O" in celula:
                agente["ouro"] = True
                print("\n Você pegou o ouro!")
            else:
                print("\nNão há ouro aqui.")
            time.sleep(1.5)

        # ATIRAR FLECHA
        elif acao == "F":
            if agente["flechas"] == 0:
                print("\nVocê não tem mais flechas!")
                time.sleep(1.5)
            else:
                direcao = input("Direção da flecha (N/S/L/O): ").upper()
                linha, coluna = agente["posicao"]

                if direcao == "N" and linha > 0:
                    alvo = (linha - 1, coluna)
                elif direcao == "S" and linha < 3:
                    alvo = (linha + 1, coluna)
                elif direcao == "L" and coluna < 3:
                    alvo = (linha, coluna + 1)
                elif direcao == "O" and coluna > 0:
                    alvo = (linha, coluna - 1)
                else:
                    print("\nDireção inválida!")
                    time.sleep(1)
                    continue

                agente["flechas"] -= 1
                matou = matar_wumpus(mundo, alvo)

                if matou:
                    print("\n WUMPUS MORTO! ")
                    time.sleep(2)
                else:
                    print("\nA flecha não acertou nada.")
                    time.sleep(1.5)

        # SAIR
        elif acao == "X":
            print("\nSaindo do jogo...")
            time.sleep(1)
            break

        # AÇÃO INVÁLIDA
        else:
            print("\nAção inválida!")
            time.sleep(1)

    limpar_tela()

    if agente["ouro"]:
        print(" PARABÉNS! Você venceu o jogo!")
    elif not agente["vivo"]:
        print(" FIM DE JOGO! Você morreu.")
    else:
        print("Jogo encerrado.")


main()
