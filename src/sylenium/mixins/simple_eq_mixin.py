from __future__ import annotations


class SimpleEQMixin:
    """
    Simple Equals mixin
    """

    def __eq__(self, other: SimpleEQMixin) -> bool:
        return type(other) is type(self) and self.__dict__ == other.__dict__
