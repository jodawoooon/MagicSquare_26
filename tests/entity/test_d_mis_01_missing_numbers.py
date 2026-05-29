"""Track B — D-MIS-01: missing numbers ascending (FR-03).

Domain Mock 금지. SSOT: Report/06 §8.
"""

from entity.services.missing_numbers import find_not_exist_nums
from tests.entity.grids import GRID_G1


class TestDMis01MissingNumbersG1:
    """D-MIS-01 — G1 missing numbers (7, 10) ascending."""

    def test_d_mis_01_find_not_exist_nums_g1_returns_7_and_10_ascending(self) -> None:
        """D-MIS-01, AC-FR03-01/02 — G1 누락 숫자 (7, 10) 오름차순."""
        missing = find_not_exist_nums(GRID_G1)

        assert missing == (7, 10)
