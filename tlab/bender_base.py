from abc import abstractmethod
from typing import Self

from tlab.exceptions import InvalidPowerTypeError, InvalidPowerValueError


class BenderBase:
        INVALID_POWER_LEVEL_ERROR_MESSAGE = "Power level must be a positive integer"

        def __init__(self: Self, name: str, power: int, skill: str) -> None:
                self._name = name
                self._power = power
                self._skill = skill

        @property
        def name(
                self: Self,
        ) -> str:
                return self._name

        @name.setter
        def name(
                self: Self,
                name: str,
        ) -> None:
                self._name = name

        @property
        def power(
                self: Self,
        ) -> int:
                return self._power

        @power.setter
        def power(
                self: Self,
                power: int,
        ) -> None:
                self._verify_power(power)

                self._power = power

        @property
        @abstractmethod
        def skill(
                self: Self,
        ) -> str:
                return self._skill

        def _verify_power(self: Self, power: int) -> None:
                if type(power) is not int:
                        raise InvalidPowerTypeError(BenderBase.INVALID_POWER_LEVEL_ERROR_MESSAGE)

                if power < 0:
                        raise InvalidPowerValueError(BenderBase.INVALID_POWER_LEVEL_ERROR_MESSAGE)

        @abstractmethod
        def bend(
                self: Self,
        ) -> None:
                raise NotImplementedError("You Should Implement this method")
