from typing import Any
from typing import Dict

from sylenium.command.click import Click
from sylenium.command.command import Command
from sylenium.command.find import Find
from sylenium.command.find_all import FindAll

COMMANDS: Dict[str, Command] = {}


def reset_commands() -> None:
    COMMANDS.clear()
    add_find_commands()


def add_find_commands() -> None:
    COMMANDS["find"] = Find()
    COMMANDS["find_all"] = FindAll()


def add_click_commands() -> None:
    COMMANDS["click"] = Click()


def execute(command: str, *args, **kwargs) -> Any:
    found_command = COMMANDS.get(command, None)
    if found_command is not None:
        return found_command.execute(*args, **kwargs)
    raise ValueError(
        f"Attempting to perform an illegal command through the command invoker: {command}"
    )


# Register commands
add_find_commands()
add_click_commands()
