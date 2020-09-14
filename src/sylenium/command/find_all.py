from typing import Any
from typing import List

from sylenium.command.command import Command
from sylenium.element.sylenium_element import SyleniumElement


class FindAll(Command[List[SyleniumElement]]):
    def execute(self, *args, **kwargs) -> Any:
        pass
