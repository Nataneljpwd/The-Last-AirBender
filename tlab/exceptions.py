from typing import Self


class InvalidPowerValueError(ValueError):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class InvalidPowerTypeError(TypeError):
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
