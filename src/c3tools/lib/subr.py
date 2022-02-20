from typing import Any, Callable


def identity(elm: Any) -> Any:
    return elm


def remove_if(pred: Callable[[Any], bool], seq: list[Any]) -> list[Any]:
    return [elm for elm in seq if not pred(elm)]


def keep_if(pred: Callable[[Any], bool], seq: list[Any]) -> list[Any]:
    return remove_if(lambda elm: not pred(elm), seq)


def remove(elt: Any, seq: list[Any]) -> list[Any]:
    return remove_if(lambda elm: elm == elt, seq)


def keep(seq: list[Any]):
    return keep_if(bool, seq)
