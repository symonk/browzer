from typing import Any
from typing import List

from sylenium import SyleniumElement
from sylenium.command.command import Command


class FindAll(Command[List[SyleniumElement]]):
    def execute(self, *args, **kwargs) -> Any:
        pass
