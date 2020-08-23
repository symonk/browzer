class SimpleEQMixin:
    """
    Simple Equals mixin
    """

    def __eq__(self, other) -> bool:
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
