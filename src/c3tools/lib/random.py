import uuid
import string
import random


def uuid4() -> str:
    return str(uuid.uuid4())


def chars(length: int, population=string.ascii_lowercase + string.digits) -> str:
    return "".join(random.choices(population, k=length))
