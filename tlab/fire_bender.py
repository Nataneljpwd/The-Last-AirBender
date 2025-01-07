import random
from collections.abc import Callable
from typing import Self

from tlab.bender_base import BenderBase
from tlab.strategy_map_mixin import DefaultStrategyMapMixin


class FireBender(BenderBase, DefaultStrategyMapMixin):
        def __init__(
                self: Self,
                name: str,
                power: int,
                random_generator: random.Random = random.Random(),
                bend_strategy_map: dict[str, Callable] = {},
        ) -> None:
                super().__init__(name, power, "Firebending")
                super(BenderBase, self).__init__(bend_strategy_map)

                self._random_generator = random_generator

        def _get_default_strategy_map(self) -> dict[int, Callable]:
                s_map: dict[int, Callable] = {}

                s_map[0] = lambda: self._set_name("dead")
                s_map[6] = lambda: self._exit(6)

                return s_map

        def _set_name(self: Self, new_name: str) -> None:
                self._name = new_name

        def _exit(self: Self, code: int) -> None:
                raise SystemExit(code)

        def bend(
                self: Self,
        ) -> None:
                result = self._random_generator.randint(0, 6)

                strategy = self._strategy_map.get(result)

                if strategy is None:
                        return

                strategy()
