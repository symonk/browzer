from abc import ABC
from abc import abstractmethod
from typing import Any


class Command(ABC):
    @abstractmethod
    def execute(self, **kwargs) -> Any:
        raise NotImplementedError()
