from __future__ import annotations

import json
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, List, Protocol, TypeVar, Generic, runtime_checkable
from time import sleep


# ---------- Serialization Protocol ----------

@runtime_checkable
class DictConvertible(Protocol):
    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "DictConvertible": ...
    def to_dict(self) -> dict[str, Any]: ...


T = TypeVar("T", bound=DictConvertible)


# ---------- Abstract Base Repository (JSON-backed) ----------

class AbstractJsonCrudRepository(ABC, Generic[T]):
    """
    Generic JSON-backed CRUD repository.
    Subclasses define how to interact (prompts, fields, etc.).
    """

    def __init__(self, arquivo: str | Path):
        self.path = Path(arquivo)
        self._ensure_file()
        self.items: List[T] = self._load()

    # ----- File I/O -----

    def _ensure_file(self) -> None:
        """Create the JSON file with an empty list if it doesn't exist."""
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self._write_json_atomic(self.path, [])

    @classmethod
    def _read_json(cls, path: Path) -> list[dict[str, Any]]:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            return []
        try:
            data = json.loads(text or "[]")
            return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            return []

    @classmethod
    def _write_json_atomic(cls, path: Path, data: list[dict[str, Any]]) -> None:
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_text(json.dumps(data, indent=4, ensure_ascii=False), encoding="utf-8")
        tmp.replace(path)

    def _load(self) -> list[T]:
        raw = self._read_json(self.path)
        return [self._model_from_dict(d) for d in raw if self._is_valid_dict(d)]

    def _save(self) -> None:
        payload = [self._model_to_dict(x) for x in self.items]
        self._write_json_atomic(self.path, payload)

    # ----- Model hooks (implemented via DictConvertible by default) -----

    def _model_from_dict(self, d: dict[str, Any]) -> T:
        return self.model_cls().from_dict(d)  # type: ignore[return-value]

    def _model_to_dict(self, obj: T) -> dict[str, Any]:
        return obj.to_dict()

    @abstractmethod
    def model_cls(self) -> type[T]:
        """Return the dataclass/model type used in this repository."""

    @abstractmethod
    def _is_valid_dict(self, d: dict[str, Any]) -> bool:
        """Light validation before converting to model."""

    # ----- CRUD (abstract) -----

    @abstractmethod
    def list_all(self) -> None: ...
    @abstractmethod
    def create(self) -> None: ...
    @abstractmethod
    def update(self) -> None: ...
    @abstractmethod
    def delete(self) -> None: ...


# ---------- Concrete model ----------

@dataclass
class Pessoa(DictConvertible):
    nome: str
    idade: int

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Pessoa":
        return cls(nome=str(d["nome"]), idade=int(d["idade"]))

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


# ---------- Concrete Repository ----------

class RegisterPeoplesRepository(AbstractJsonCrudRepository[Pessoa]):
    """
    Pequeno repositório de pessoas baseado em JSON.
    Exponde métodos amigáveis em PT-BR e também os CRUD genéricos.
    """

    # ---- Model hooks ----

    def model_cls(self) -> type[Pessoa]:
        return Pessoa

    def _is_valid_dict(self, d: dict[str, Any]) -> bool:
        return isinstance(d, dict) and {"nome", "idade"} <= set(d)

    # ---- Input helpers ----
    @staticmethod
    def _input_str(prompt: str, allow_empty: bool = False) -> str:
        while True:
            try:
                s = input(prompt).strip()
                if not s and not allow_empty:
                    print("\033[0;31mCampo obrigatório.\033[m")
                    continue
                return s
            except KeyboardInterrupt:
                print()
                raise

    @staticmethod
    def _input_int(prompt: str, allow_empty: bool = False) -> int | None:
        while True:
            try:
                s = input(prompt).strip()
                if allow_empty and s == "":
                    return None
                try:
                    return abs(int(s))
                except ValueError:
                    print("\033[0;31mERRO! Digite um número inteiro.\033[m")
            except KeyboardInterrupt:
                print()
                raise

    def _choose_index(self, total: int, prompt: str) -> int:
        while True:
            try:
                val = int(input(prompt).strip())
                if 0 <= val < total:
                    return val
                print("\033[0;31mERRO! Digite um índice da lista.\033[m")
            except ValueError:
                print("\033[0;31mERRO! Digite um número da lista.\033[m")
            except KeyboardInterrupt:
                print()
                raise

    # ---- CRUD (English interface) ----

    def list_all(self) -> None:
        if not self.items:
            print("Nenhum cadastro encontrado! Crie um novo.")
            return
        for c in self.items:
            print(f"{c.nome:<20} {c.idade:>20}")
            sleep(2)

    def create(self) -> None:
        try:
            nome = self._input_str("Nome: ")
            idade = self._input_int("Idade: ")
            if idade is None:
                print("\033[0;31mIdade é obrigatória.\033[m")
                return
            self.items.append(Pessoa(nome=nome, idade=idade))
            self._save()
            print("Cadastro criado com sucesso!")
        except KeyboardInterrupt:
            pass
        except OSError:
            print("Erro ao salvar. Tente novamente.")

    def update(self) -> None:
        if not self.items:
            print("Nenhum cadastro encontrado! Crie um novo.")
            return
        for i, c in enumerate(self.items):
            print(f"{i} {c.nome:<20} {c.idade:>20}")
        try:
            idx = self._choose_index(len(self.items), "Qual cadastro você quer editar? ")
            atual = self.items[idx]
            novo_nome = self._input_str(f"Nome [{atual.nome}]: ", allow_empty=True)
            nova_idade = self._input_int(f"Idade [{atual.idade}]: ", allow_empty=True)

            if novo_nome != "":
                atual.nome = novo_nome
            if nova_idade is not None:
                atual.idade = nova_idade

            self._save()
            print("Cadastro editado com sucesso!")
        except KeyboardInterrupt:
            pass
        except OSError:
            print("Erro ao salvar. Tente novamente.")
        except Exception as e:
            print(f"Erro ao editar o cadastro: {e}")

    def delete(self) -> None:
        if not self.items:
            print("Nenhum cadastro encontrado! Crie um novo.")
            return
        for i, c in enumerate(self.items):
            print(f"{i} {c.nome:<20} {c.idade:>20}")
        try:
            idx = self._choose_index(len(self.items), "Qual cadastro você quer deletar? ")
            pessoa = self.items.pop(idx)
            self._save()
            print(f"Cadastro de '{pessoa.nome}' removido com sucesso!")
        except KeyboardInterrupt:
            pass
        except OSError:
            print("Erro ao salvar. Tente novamente.")

    # ---- PT-BR aliases (compat) ----

    def cadastro(self) -> None:
        self.list_all()

    def cadastrar(self) -> None:
        self.create()

    def editar(self) -> None:
        self.update()

    def apagar(self) -> None:
        self.delete()
