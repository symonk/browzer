from abc import ABC
from abc import abstractmethod
from typing import Generic
from typing import TypeVar

T = TypeVar("T")


class Command(ABC, Generic[T]):
    @abstractmethod
    def execute(self, *args, **kwargs) -> T:
        raise NotImplementedError()
