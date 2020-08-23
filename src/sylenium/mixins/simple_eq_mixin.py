class SimpleEQMixin:
    """
    Simple Equals mixin
    """

    def __eq__(self, other) -> bool:
        return type(other) is type(self) and self.__dict__ == other.__dict__
