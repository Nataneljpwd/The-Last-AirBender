import os
from collections.abc import Callable
from typing import Self
from webbrowser import BaseBrowser

from tlab.bender_base import BenderBase


class WaterBender(BenderBase):

    def __init__(
        self: Self,
        name: str,
        power: int,
        browser: BaseBrowser | None = None,
        bend_strategy_map: dict[str, Callable[[BaseBrowser], None]] = {},
    ) -> None:

        self._verify_power(power)

        self.browser = browser

        self.bend_strategy_map = bend_strategy_map

        if not self.bend_strategy_map:
            self.bend_strategy_map = self._get_default_strategy_map()

        super().__init__(name, power, "Waterbending")

    def _get_default_strategy_map(self) -> dict[str, Callable[[BaseBrowser], None]]:
        s_map = {}

        s_map["NONE"] = lambda browser: browser.open_new(f"https://youtu.be/gk-aCL6eyGc?si=XX45XZzc3a8uCN0o&t={self._power}")

        s_map["FULL"] = lambda browser: browser.open_new("https://www.wikiwand.com/en/6")

        return s_map

    def _get_fallback_strategy(self: Self) -> Callable[[BaseBrowser], None]:
        result = lambda browser: browser.open_new("https://youtu.be/weZKm1kTrpc?si=_Unblsn5tPvzwfs7")

        return result

    def _decrement_power(self: Self, decrement_by: int = 1) -> None:
        self._power = max(self._power - decrement_by, 0)

    def bend(
        self: Self,
    ) -> None:

        moon_status = os.getenv("MOON", "NONE")

        if self.browser is None:
            self._decrement_power()
            return

        strategy = self.bend_strategy_map.get(moon_status)

        if strategy is None:  # special case, because dict key cannot be None
            self._get_fallback_strategy()(self.browser)
            self._decrement_power()
            return

        strategy(self.browser)

        self._decrement_power()

