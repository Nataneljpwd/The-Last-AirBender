import random
from typing import Self

from tlab.bender_base import BenderBase


class FireBender(BenderBase):
        # Return type is None due to: https://peps.python.org/pep-0484/#the-meaning-of-annotations
        def __init__(
                self: Self,
                name: str,
                power: int,
                random_generator: random.Random = random.Random(),
        ) -> None:
                self._verify_power(power)

                self.random_generator = random_generator

                super().__init__(name, power, "Firebending")

        def bend(
                self: Self,
        ) -> None:
                result = self.random_generator.randint(0, 6)

                if result == 0:
                        self._name = "dead"
                elif result == 6:
                        raise SystemExit(result)
