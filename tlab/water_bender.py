import os
from collections import defaultdict
from collections.abc import Callable
from typing import Self
from webbrowser import BaseBrowser

from tlab.bender_base import BenderBase
from tlab.method_utils import run_with_defered_instance_method
from tlab.strategy_map_mixin import DefaultStrategyMapMixin


class WaterBender(BenderBase, DefaultStrategyMapMixin):
        def __init__(
                self: Self,
                name: str,
                power: int,
                browser: BaseBrowser | None = None,
                bend_strategy_map: dict[str, Callable[[BaseBrowser], None]] = {},
        ) -> None:
                super().__init__(name, power, "Waterbending")
                super(BenderBase, self).__init__(bend_strategy_map)

                self.browser = browser

                self._strategy_map = defaultdict(lambda:self._get_fallback_strategy(), self._strategy_map)


        def _get_default_strategy_map(self) -> dict[str, Callable[[BaseBrowser], None]]:
                s_map = {}

                s_map["NONE"] = lambda browser: browser.open_new(
                        f"https://youtu.be/gk-aCL6eyGc?si=XX45XZzc3a8uCN0o&t={self._power}"
                )

                s_map["FULL"] = lambda browser: browser.open_new("https://www.wikiwand.com/en/6")

                return s_map

        def _get_fallback_strategy(self: Self) -> Callable[[BaseBrowser], None]:
                result = lambda browser: browser.open_new(
                        "https://youtu.be/weZKm1kTrpc?si=_Unblsn5tPvzwfs7"
                )

                return result

        def _decrement_power(self: Self, decrement_by: int = 1) -> None:
                self._power = max(self._power - decrement_by, 0)

        @run_with_defered_instance_method(_decrement_power)
        def bend(
                self: Self,
        ) -> None:
                moon_status = os.getenv("MOON", "NONE")

                if self.browser is None:
                        return

                strategy = self._strategy_map[moon_status]

                if strategy is None:
                    raise RuntimeError("Should never happen due to defaultdict")

                strategy(self.browser)

