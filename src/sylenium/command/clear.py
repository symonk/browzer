from sylenium.command.command import Command


class Clear(Command):
    def execute(self, **kwargs) -> None:
        kwargs.pop("element").wrapped_element.clear()
