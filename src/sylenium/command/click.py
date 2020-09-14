from sylenium.command.command import Command


class Click(Command):
    def execute(self, *args, **kwargs) -> None:
        args[0].wrapped_element.click()
