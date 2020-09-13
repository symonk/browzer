from sylenium import SyleniumElement
from sylenium.command.command import Command


class Find(Command[SyleniumElement]):
    def execute(self, *args, **kwargs) -> SyleniumElement:
        ...
