import os
import re
from typing import Self

from tlab.bender_base import BenderBase


class EarthBender(BenderBase):
        DEFAULT_NO_ROCK_ROLL_PATTERN = "No Rock Ball :("
        VALIDATION_RGX = r"rock ball"

        def __init__(
                self: Self,
                name: str,
                power: int,
        ) -> None:
                self._verify_power(power)

                super().__init__(name, power, "Earthbending")

        def bend(
                self: Self,
        ) -> None:
                bend_message = os.getenv("EARTH_ATTACK") or ""

                if (
                        re.compile(EarthBender.VALIDATION_RGX, re.IGNORECASE).match(bend_message)
                        is None
                ):
                        bend_message = EarthBender.DEFAULT_NO_ROCK_ROLL_PATTERN
                        os.environ["EARTH_ATTACK"] = bend_message
                else:
                        bend_message = f"{bend_message} with power: {str(self._power).ljust(2, ' ')}.".lower()

                print(bend_message, end="")
