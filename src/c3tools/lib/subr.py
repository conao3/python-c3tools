from typing import Any, Callable


def identity(elm: Any) -> Any:
    return elm


def keep_if(pred: Callable[[Any], bool], args: list[Any]) -> list[Any]:
    return [elm for elm in args if pred(elm)]


def keep(args: list[Any]):
    return keep_if(bool, args)


def remove_if(pred: Callable[[Any], bool], seq: list[Any]) -> list[Any]:
    return [elm for elm in seq if not pred(elm)]


def remove(elt: Any, seq: list[Any]) -> list[Any]:
    return remove_if(lambda elm: elm == elt, seq)
