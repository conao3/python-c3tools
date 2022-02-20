from typing import Any, Callable


def identity(elm: Any) -> Any:
    return elm


def keep_if(args: list[Any], pred: Callable[[Any], bool]) -> list[Any]:
    return [elm for elm in args if pred(elm)]


def keep(args: list[Any]):
    return keep_if(args, bool)
