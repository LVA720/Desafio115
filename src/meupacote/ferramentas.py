import json
from os.path import exists


def menu(txt, opc=True):
    print("-" * 30)
    print(f"{txt:^30}")
    print("-" * 30)
    if opc:
        escolhas = ["Ver Pessoas cadastradas", "Cadastrar nova Pessoa", "Editar cadastro","Apagar cadastro", "Sair do Sistema"]
        for index, element in enumerate(escolhas):
            print(f"\033[33m{index+1}\033[m - \033[34m {element}\033[m")

class humano:

    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.galera = self.carregar_dados()
        self.pessoa = {}
    def carregar_dados(self):
        try:
            with open("dados.json", "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except OSError:
            return []

    def salvar_dados(self):
        with open("dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(self.galera, arquivo, indent=4)

    def cadastro(self):
        try:
            with open("dados.json", "r", encoding="utf-8") as arquivo:
                galera = json.load(arquivo)
        except OSError:
            print("Nenhum cadastro encontrado! Crie um novo")
        for c in galera:
            print(f"{c['nome']:<20} {c['idade']:>20}")
    def cadastrar(self):
        try:
            self.pessoa["nome"] = str(input("Nome: "))
            while True:
                try:
                    self.pessoa["idade"] = abs(int(input("Idade: ")))
                # bruno gay
                except KeyboardInterrupt:
                    break
                except ValueError:
                    print("\033[0;31mERRO! por favor, digite um numero inteiro!\033[m")
                else:
                    self.galera.append(self.pessoa.copy())
                    self.salvar_dados()
                    self.pessoa.clear()
                    break
        except KeyboardInterrupt:
            print()
        except OSError:
            print("Nenhum cadastro encontrado! Crie um novo")

    def editar(self):
        try:
            with open ("dados.json", "r", encoding="utf-8") as arquivo:
                data = json.load(arquivo)
            for i, c in enumerate(data):
                print(f"{i} {c['nome']:<20} {c['idade']:>20}")
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
        except OSError:
            print("Nenhum cadastro encontrado! Crie um novo")
        except Exception as erro:
            print(f"Erro ao editar o cadastro {erro}")
    def apagar(self):
        try:
            with open ("dados.json", "r", encoding="utf-8") as arquivo:
                data = json.load(arquivo)
            for i, c in enumerate(data):
                print(f"{i} {c['nome']:<20} {c['idade']:>20}")
            while True:
                try:
                    esc = int(input("Qual cadastro voce quer deletar? "))
                    del self.galera[esc]
                    self.salvar_dados()

                except IndexError:
                    print("\033[0;31mDigite um numero da lista!\033[m")
                except ValueError:
                    print("\033[0;31mDigite um numero da lista!\033[m")
                except KeyboardInterrupt:
                    print()
                    break
                except OSError:
                    print("Nenhum cadastro encontrado! Crie um novo")
                else:
                    break
        except OSError:
            print("Nenhum cadastro encontrado! Crie um novo")

if exists("dados.json"):
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        galera = json.load(arquivo)
