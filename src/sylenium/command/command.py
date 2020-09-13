from abc import ABC
from abc import abstractmethod
from typing import Any


class Command(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        raise NotImplementedError()
