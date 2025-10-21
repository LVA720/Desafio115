# menu_schema.py
from __future__ import annotations

from enum import StrEnum
from pathlib import Path
from typing import Iterator, Tuple

from pydantic import BaseModel, RootModel


class Action(StrEnum):
    READ_PEOPLES   = "read_peoples"
    CREATE_PEOPLE  = "create_people"
    EDIT_PEOPLE    = "edit_people"
    DELETE_PEOPLE  = "delete_people"
    EXIT_PROGRAM   = "exit_program"


class MenuItem(BaseModel):
    title: str
    description: str


class MenuConfig(RootModel[dict[str, MenuItem]]):
    """
    RootModel around a dict[str, MenuItem].
    Keys should be the action strings (e.g. 'read_peoples').
    """

    @classmethod
    def from_file(cls, path: str | Path) -> MenuConfig:
        text = Path(path).read_text(encoding="utf-8")
        return cls.model_validate_json(text)

    # Convenience helpers
    def get(self, action: Action) -> MenuItem:
        return self.root[action.value]

    def items(self) -> Iterator[Tuple[Action, MenuItem]]:
        for k, v in self.root.items():
            yield Action(k), v

    def as_ordered_list(self, order: list[Action]) -> list[tuple[Action, MenuItem]]:
        return [(a, self.get(a)) for a in order]

MENU = MenuConfig.from_file("src/constants/menu.json")

# If you want a fixed numeric order for your CLI:
ORDER = [
    Action.READ_PEOPLES,
    Action.CREATE_PEOPLE,
    Action.EDIT_PEOPLE,
    Action.DELETE_PEOPLE,
    Action.EXIT_PROGRAM,
]
