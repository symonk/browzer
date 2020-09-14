from typing import Any
from typing import Dict

from sylenium.command.clear import Clear
from sylenium.command.click import Click
from sylenium.command.command import Command
from sylenium.command.find import Find
from sylenium.command.find_all import FindAll
from sylenium.command.press_enter import PressEnter
from sylenium.command.set_text import SetText
from sylenium.exception import IllegalElementCommandException

COMMANDS: Dict[str, Command] = {}


def add_find_commands() -> None:
    COMMANDS["find"] = Find()
    COMMANDS["find_all"] = FindAll()


def add_click_commands() -> None:
    COMMANDS["click"] = Click()


def add_text_commands() -> None:
    COMMANDS["set_text"] = SetText()
    # COMMANDS["get_text"] = GetText()
    COMMANDS["clear"] = Clear()


def add_key_commands() -> None:
    COMMANDS["press_enter"] = PressEnter()


def execute(command: str, **kwargs) -> Any:
    found_command = COMMANDS.get(command, None)
    if found_command is not None:
        return found_command.execute(**kwargs)
    raise IllegalElementCommandException(
        f"Attempting to perform an illegal command through the command invoker: {command}"
    )


# Register commands
add_find_commands()
add_click_commands()
add_text_commands()
add_key_commands()
