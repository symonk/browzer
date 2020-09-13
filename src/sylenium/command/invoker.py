from typing import Any
from typing import Dict

from sylenium.command.command import Command
from sylenium.command.find import Find
from sylenium.command.find_all import FindAll

COMMANDS: Dict[str, Command] = {}


def reset_commands() -> None:
    COMMANDS.clear()


def add_find_commands() -> None:
    COMMANDS["find"] = Find()
    COMMANDS["find_all"] = FindAll()


def execute(cmd: Command) -> Any:
    ...
