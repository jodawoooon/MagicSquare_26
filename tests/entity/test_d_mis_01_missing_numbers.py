"""Track B — D-MIS-01: missing numbers ascending (FR-03).

Domain Mock 금지. SSOT: Report/06 §8.
"""

import pytest

from entity.services.missing_number_finder import find_not_exist_nums


class TestDMis01MissingNumbersG1:
    """D-MIS-01 — G1 missing numbers (7, 10) ascending."""

    def test_d_mis_01_find_not_exist_nums_g1_returns_7_and_10_ascending(self) -> None:
        """D-MIS-01, AC-FR03-01/02 — G1 누락 숫자 (7, 10) 오름차순."""
        # Given
        # matrix = G1

        # When
        # missing = find_not_exist_nums(matrix)

        # Then — (7, 10) (GREEN)
        pytest.fail("RED: D-MIS-01 — G1 누락 숫자 (7, 10) 오름차순")
