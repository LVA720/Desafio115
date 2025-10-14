import json 
from os.path import exists
def menu(txt, opc=True):
    print("-" * 30)
    print(f"{txt:^30}")
    print("-" * 30)
    if opc:
        print("\033[33m1\033[m - \033[34m Ver Pessoas cadastradas\033[m")
        print("\033[33m2\033[m - \033[34m Cadastrar nova Pessoa\033[m")
        print("\033[33m3\033[m - \033[34m Editar cadastro\033[m")
        print("\033[33m4\033[m - \033[34m Apagar cadastro\033[m")
        print("\033[33m5\033[m - \033[34m Sair do Sistema\033[m")


def pessoas(n):
    global galera
    pessoa = {}
    if n == 1:
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            galera = json.load(arquivo)
        for c in galera:
            print(f"{c["nome"]:<20} {c["idade"]:>20}")
    if n == 2:
        try:
            pessoa["nome"] = str(input("Nome: "))
            while True:
                try:
                    pessoa["idade"] = abs(int(input("Idade: ")))
                       # bruno gay
                except KeyboardInterrupt:
                    break
                except:
                    print("\033[0;31mERRO! por favor, digite um numero inteiro!\033[m")
                else:
                    galera.append(pessoa.copy())
                    with open("dados.json", "w", encoding="utf-8") as arquivo:
                        json.dump(galera, arquivo, ensure_ascii=False, indent=4)
                    pessoa.clear()
                    break
        except KeyboardInterrupt:
            print()
    if n == 3:
        try:
            with open("dados.json", "r", encoding="utf-8") as arquivo:
                data = json.load(arquivo)
            for i, c in enumerate(data):
                print(f"{i} {c["nome"]:<20} {c["idade"]:>20}")
            while True:
                try:
                    esc = int(input("Qual cadastro voce quer editar? "))
                    pessoa = data[esc]
                    data[esc]["nome"] = str(input("Nome: "))
                    while True:
                        try:
                            data[esc]["idade"] = int(input("Idade: "))
                            print("Cadastro Editado com sucesso!")
                            break
                        except ValueError:
                            print("\033[0;31mERRO! por favor, digite um numero inteiro!\033[m")
                except IndexError:
                    print("\033[0;31mERRO! por favor, digite um numero da lista!\033[m")
                except ValueError:
                    print("\033[0;31mDigite um numero da lista!\033[m")
                except KeyboardInterrupt:
                        print()
                        break
                else:
                    data[esc] = pessoa
                    break
                
            with open("dados.json", "w", encoding="utf-8") as arquivo:
                json.dump(data, arquivo, indent=4)
        except Exception as erro:
                print(f"Erro ao editar o cadastro {erro}")
    if n == 4:
            with open("dados.json", "r", encoding="utf-8") as arquivo:
                data = json.load(arquivo)
                for i, c in enumerate(data):
                    print(f"{i} {c["nome"]:<20} {c["idade"]:>20}")
                while True:
                    try:
                        esc = int(input("Qual cadastro voce quer deletar? "))                   
                        del data[esc]
                        with open("dados.json", "w", encoding="utf-8") as arquivo:
                            json.dump(data, arquivo, indent=4)
                    except IndexError:
                        print("\033[0;31mDigite um numero da lista!\033[m")
                    except ValueError:
                            print("\033[0;31mDigite um numero da lista!\033[m")
                    except KeyboardInterrupt:
                        print()
                        break
                    else:
                        break
galera = []
if exists("dados.json"):
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        galera = json.load(arquivo)
