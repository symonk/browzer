from sylenium.command.command import Command
from sylenium.element.sylenium_element import SyleniumElement


class Find(Command[SyleniumElement]):
    def execute(self, *args, **kwargs) -> SyleniumElement:
        ...
