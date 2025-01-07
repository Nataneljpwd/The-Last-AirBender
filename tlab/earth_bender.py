import os
import re
from collections.abc import Callable
from typing import Self

from tlab.bender_base import BenderBase


class EarthBender(BenderBase):
        DEFAULT_NO_ROCK_ROLL_PATTERN = "No Rock Ball :("
        VALIDATION_RGX = re.compile(r"rock ball", re.IGNORECASE)

        def __init__(
                self: Self,
                name: str,
                power: int,
                writer: Callable = lambda *args: print(*args, end=""),
        ) -> None:
                super().__init__(name, power, "Earthbending")
                self._writer = writer

        def bend(
                self: Self,
        ) -> None:
                bend_message = os.getenv("EARTH_ATTACK") or ""

                if EarthBender.VALIDATION_RGX.match(bend_message) is None:
                        bend_message = EarthBender.DEFAULT_NO_ROCK_ROLL_PATTERN
                        os.environ["EARTH_ATTACK"] = bend_message
                else:
                        bend_message = f"{bend_message} with power: {str(self._power).ljust(2, ' ')}.".lower()

                self._writer(bend_message)
