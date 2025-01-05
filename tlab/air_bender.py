from logging import INFO, log
from typing import Self

from tlab.bender_base import BenderBase


class AirBender(BenderBase):
        def __init__(
                self: Self,
                name: str,
                power: int,
        ) -> None:
                self._verify_power(power)

                super().__init__(
                        name, power, "Airbending"
                )  # maybe change to config instead of hardcode

        @property
        def power(self) -> int:
                return self._power

        @power.setter
        def power(self: Self, power: int) -> None:
                self._verify_power(power)

                self._power = power

        def bend(self) -> None:
                log(INFO, "Aang is using his airbending skill!")
