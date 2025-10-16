from meupacote import menu, pessoas


def main():
    while True:
        menu("MENU PRINCIPAL")
        print("\033[90mCtrl + C finaliza o programa\033[m")
        while True:
            try:
                opc = str(input("\033[32m Sua Opcao: \033[m"))
                if opc.isnumeric():
                    opc = int(opc)
                    if 1 <= opc <= 5:
                        break
                    else:
                        print("\033[0;31mERRO! Opcao invalida.\033[m")
                else:
                    print("\033[0;31mERRO! Opcao invalida.\033[m")
            except KeyboardInterrupt:
                opc = 5
                break

        if opc == 1:
            menu("PESSOAS CADASTRADAS", False)
            pessoas(opc)
        if opc == 2:
            menu("NOVO CADASTRO", False)
            pessoas(opc)
        if opc == 3:
            menu("EDITAR CADASTRO", False)
            pessoas(opc)
        if opc == 4:
            menu("DELETAR CADASTRO", False)
            pessoas(opc)
        if opc == 5:
            break

print("PROGRAMA FINALIZADO")

if __name__ == "__main__":
    main()
    