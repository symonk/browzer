from sylenium.command.command import Command
from sylenium.element.sylenium_element import SyleniumElement


class Find(Command):
    def execute(self, *args, **kwargs) -> SyleniumElement:
        ...
