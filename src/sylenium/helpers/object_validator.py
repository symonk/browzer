from typing import Any
from typing import Iterable
from typing import Type


def enforce_type_of(
    expected: Any, value: Any, exc: Type[Exception] = ValueError, msg: str = None
) -> None:
    """
    Enforce a particular value is of an expected type
    :param expected: The type that the value should be of
    :param value: The object to be checked
    :param exc: The type of exception that should be raised upon failure, defaulting to ValueError
    :param msg: The message to be passed when raising the exception
    """
    if not isinstance(value, expected):
        raised_message = (
            msg
            or f"Expected the type of: {type(value)} to be of type: {type(expected)}"
        )
        raise exc(raised_message)


def raise_if_value_not_in(
    iterable: Iterable[Any], value: Any, exc: Type[Exception] = ValueError
) -> None:
    """
    Enforce a particular value is in another iterable
    :param iterable: The iterable sequence that the containment check should be part of
    :param value: The object to be checked
    :param exc: The type of exception that should be raised upon failure, defaulting to ValueError
    :param msg: The message to be passed when raising the exception
    """
    if value not in iterable:
        raised_message = f"{value} was not in {iterable}"
        raise exc(raised_message)
