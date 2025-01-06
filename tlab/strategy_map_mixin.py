from collections.abc import Callable
from typing import Self, Any


class DefaultStrategyMapMixin:
    
    def __init__(self: Self, strategy_map: dict[Any, Callable]) -> None:
        self._strategy_map = strategy_map

        if not self._strategy_map:
            self._strategy_map = self._get_default_strategy_map()


    def _get_default_strategy_map(self) -> dict[Any, Callable]:
        raise NotImplemented("You need to implement the method")
