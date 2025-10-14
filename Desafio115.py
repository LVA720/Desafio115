import ferramentas
while True:
    ferramentas.menu("MENU PRINCIPAL")
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
            ferramentas.menu("PESSOAS CADASTRADAS", False)
            ferramentas.pessoas(opc)
    if opc == 2:
            ferramentas.menu("NOVO CADASTRO", False)
            ferramentas.pessoas(opc)
    if opc == 3:
            ferramentas.menu("EDITAR CADASTRO", False)
            ferramentas.pessoas(opc)
    if opc == 4:
            ferramentas.menu("DELETAR CADASTRO", False)
            ferramentas.pessoas(opc)
    if opc == 5:
            break

print("PROGRAMA FINALIZADO")