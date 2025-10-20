from meupacote import menu
from meupacote import humano

pessoa = humano("dados.json")

def main():
    while True:
        menu("MENU PRINCIPAL")
        print("\033[90mCtrl + C finaliza o programa\033[m")
        while True:
            try:
                opc = str(input("Sua Opcao: "))
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
            pessoa.cadastro()
        if opc == 2:
            menu("NOVO CADASTRO", False)
            pessoa.cadastrar()
        if opc == 3:
            menu("EDITAR CADASTRO", False)
            pessoa.editar()
        if opc == 4:
            menu("DELETAR CADASTRO", False)
            pessoa.apagar()
        if opc == 5:
            print("\nPROGRAMA FINALIZADO")
            break

if __name__ == "__main__":
    main()
