import typing
from threading import local
from typing import Optional

if typing.TYPE_CHECKING:
    from sylenium import SyleniumDriver


class SyleniumThreadLocal(local):
    def __init__(self) -> None:
        self.driver: Optional[SyleniumDriver] = None
