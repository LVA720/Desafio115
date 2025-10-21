from schemas.menu import MENU
from utils.print_titles import pretty_print
import os
from time import sleep
from services.register_people import exec_command

def main():
    while True:
        os.system('clear')
        pretty_print("MENU")
        option = input("Selecione uma opção: ").strip()
        if option and option.isdigit() and 1 <= int(option) <= len(MENU.root) - 1:
            option = int(option)
            exec_command(option)
        elif option == str(len(MENU.root)):
            print("Saindo do programa...")
            sleep(1)
            break
        else:
            print("\033[0;31mERRO! Opcao invalida.\033[m")
        sleep(3)


if __name__ == "__main__":
    main()
