import re


def camel(arg: str) -> str:
    return "".join(x.capitalize() or " " for x in arg.split("_"))


def pascal(arg: str) -> str:
    return "".join(x.capitalize() for x in re.split(r"[-_ ]", arg))
