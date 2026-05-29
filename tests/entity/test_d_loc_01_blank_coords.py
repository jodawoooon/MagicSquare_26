"""Track B — D-LOC-01: row-major blank coordinates (FR-02).

Domain Mock 금지. SSOT: Report/06 §8.
"""

import pytest

from entity.services.blank_locator import find_blank_coords
from tests.entity.grids import GRID_G0, GRID_G1


class TestDLoc01BlankCoordsG1:
    """D-LOC-01 — G1 blanks in row-major order, 1-index."""

    def test_d_loc_01_find_blank_coords_g1_row_major_order(self) -> None:
        """D-LOC-01, AC-FR02-02 — G1 빈칸 [(2,2),(3,3)] 1-index."""
        coords = find_blank_coords(GRID_G1)

        assert coords == [(2, 2), (3, 3)]


class TestDLoc02BlankCountGuard:
    """D-LOC-02 — invalid blank count raises ValueError."""

    def test_d_loc_02_wrong_blank_count_raises_value_error(self) -> None:
        """D-LOC-02, I6 guard — 빈칸 0개 격자 ValueError."""
        with pytest.raises(ValueError, match="expected 2 blanks"):
            find_blank_coords(GRID_G0)
