from schemas.menu import MENU, ORDER


def pretty_print(title: str, show_options: bool = True) -> None:
    largura = max(30, len(title) + 4)
    linha = "-" * largura
    print(linha)
    print(title.center(largura))
    print(linha)
    if show_options:
        for i, (_, item) in enumerate(MENU.as_ordered_list(ORDER), start=1):
            print(f"\033[33m{i}\033[m - \033[34m{item.description}\033[m")
