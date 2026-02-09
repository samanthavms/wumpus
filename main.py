from agente import inicializar_agente, mover
from mundo import criar_mundo, obter_celula, verificar_perigos
from util import limpar_tela, mostrar_menu, mostrar_percepcoes


def main():
    mundo = criar_mundo()
    agente = inicializar_agente()

    # Loop principal do jogo
    while agente["vivo"] and not agente["ouro"]:
        limpar_tela()

        print("=== MUNDO DO WUMPUS ===")
        print("Posição atual:", agente["posicao"])

        # Obtém a célula atual do agente
        celula = obter_celula(mundo, agente["posicao"])

        # Mostra percepções
        mostrar_percepcoes(celula)

        # Mostra menu
        print()
        mostrar_menu()

        acao = input("\nEscolha uma ação: ").upper()

        if acao in ["N", "S", "L", "O"]:
            mover(agente, acao)
            verificar_perigos(mundo, agente)

        elif acao == "P":
            if "O" in celula:
                agente["ouro"] = True
                print("\n Você pegou o ouro!")
                input("Pressione ENTER para continuar...")
            else:
                print("\n Não há ouro aqui.")
                input("Pressione ENTER para continuar...")

        elif acao == "F":
            print("\nVocê atirou a flecha! (função simples)")
            agente["flechas"] -= 1
            input("Pressione ENTER para continuar...")

        elif acao == "X":
            print("\nSaindo do jogo...")
            break

        else:
            print("\nAção inválida!")
            input("Pressione ENTER para continuar...")

    limpar_tela()

    if agente["ouro"]:
        print(" PARABÉNS! Você venceu o jogo!")
    elif not agente["vivo"]:
        print("FIM DE JOGO! Você morreu.")
    else:
        print("Jogo encerrado.")


main()
