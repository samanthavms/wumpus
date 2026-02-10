import sys
import os
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

        # PEGAR OURO
        elif acao == "P":
            if "O" in celula:
                agente["ouro"] = True
                print("\n🏆 Você pegou o ouro!")
            else:
                print("\nNão há ouro aqui.")

        # ATIRAR FLECHA
        elif acao == "F":
            if agente["flechas"] == 0:
                print("\nVocê não tem mais flechas!")
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
                    print("Direção inválida!")
                    continue

                agente["flechas"] -= 1
                matou = matar_wumpus(mundo, alvo)

                if not matou:
                    print("A flecha não acertou nada.")


        # SAIR
        elif acao == "X":
            print("\nSaindo do jogo...")
            break

        # AÇÃO INVÁLIDA
        else:
            print("\nAção inválida!")

    limpar_tela()

    if agente["ouro"]:
        print(" PARABÉNS! Você venceu o jogo!")
    elif not agente["vivo"]:
        print(" FIM DE JOGO! Você morreu.")
    else:
        print(" Jogo encerrado.")


main()
