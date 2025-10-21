from repositories.register import RegisterPeoplesRepository

service = RegisterPeoplesRepository("register_people.json")

ACTIONS = {
    1: service.cadastro,   # listar
    2: service.cadastrar,  # criar
    3: service.editar,     # atualizar
    4: service.apagar,     # deletar
}

def exec_command(option: int) -> None:
    func = ACTIONS.get(option)
    if func is None:
        return
    func()
