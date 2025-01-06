from collections.abc import Callable
from typing import Self


def run_with_defered_instance_method(to_run_defered: Callable):

    def inner(func: Callable):

        def wrapper(*args):
            func(*args)
            to_run_defered(args[0])

        return wrapper

    return inner
