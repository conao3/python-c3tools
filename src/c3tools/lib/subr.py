from typing import Any, Callable


def identity(elm: Any) -> Any:
    return elm


def remove_if(pred: Callable[[Any], bool], seq: list[Any]) -> list[Any]:
    return [elm for elm in seq if not pred(elm)]


def keep_if(pred: Callable[[Any], bool], seq: list[Any]) -> list[Any]:
    return remove_if(lambda elm: not pred(elm), seq)


def some_if(pred: Callable[[Any], bool], seq: list[Any]) -> bool:
    return any(pred(elm) for elm in seq)


def every_if(pred: Callable[[Any], bool], seq: list[Any]) -> bool:
    return all(pred(elm) for elm in seq)


def find_if(pred: Callable[[Any], bool], seq, default=None):
    return next(filter(pred, seq), default)


def remove(elt: Any, seq: list[Any]) -> list[Any]:
    return remove_if(lambda elm: elm == elt, seq)


def keep(seq: list[Any]):
    return keep_if(bool, seq)


def some(seq: list[Any]):
    return some_if(bool, seq)


def every(seq: list[Any]):
    return every_if(bool, seq)


def find(elt: Any, seq: list[Any], default=None):
    return find_if(lambda elm: elm == elt, seq, default)
