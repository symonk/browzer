from typing import Any
from typing import Optional

from sylenium import config


def open(
    url: Optional[str] = None, yielded_page_object: Optional[Any] = None
) -> Optional[Any]:
    url = url or config.base_url
    to_be_returned = yielded_page_object
    # Fetch a thread local drivers (or instantiate one if necessary)
    return yielded_page_object
