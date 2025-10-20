from meupacote import menu
from meupacote import humano

pessoa = humano("dados.json")

def main():
    def handle_command(command):
        match command:
            case 1:
                menu("PESSOAS CADASTRADAS", False)
                pessoa.cadastro()
            case 2:
                menu("NOVO CADASTRO", False)
                pessoa.cadastrar()
            case 3:
                menu("EDITAR CADASTRO", False)
                pessoa.editar()
            case 4:
                menu("DELETAR CADASTRO", False)
                pessoa.apagar()
            case 5:
                print("\nPROGRAMA FINALIZADO")
            case _:  # Default case, acts like 'else'
                print("\033[0;31mERRO! Opcao invalida.\033[m")
    while True:
        menu("MENU PRINCIPAL")
        print("\033[90mCtrl + C finaliza o programa\033[m")
        while True:
            try:
                opc = str(input("Sua Opcao: "))
                opc = int(opc) if opc.isdigit() else print("\033[0;31mERRO! Opcao invalida.\033[m")
                handle_command(opc)
            except KeyboardInterrupt:
                handle_command(5)
                break

if __name__ == "__main__":
    main()
