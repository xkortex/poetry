from typing import TYPE_CHECKING
from typing import List


if TYPE_CHECKING:
    from poetry.core.packages.package import Package


class Transaction:
    def __init__(
        self, current_packages: List["Package"], result_packages: List["Package"]
    ) -> None:
        self._current_packages = current_packages
