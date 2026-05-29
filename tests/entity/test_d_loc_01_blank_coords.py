"""Track B — D-LOC-01: row-major blank coordinates (FR-02).

Domain Mock 금지. SSOT: Report/06 §8.
"""

from entity.services.blank_locator import find_blank_coords
from tests.entity.grids import GRID_G1


class TestDLoc01BlankCoordsG1:
    """D-LOC-01 — G1 blanks in row-major order, 1-index."""

    def test_d_loc_01_find_blank_coords_g1_row_major_order(self) -> None:
        """D-LOC-01, AC-FR02-02 — G1 빈칸 [(2,2),(3,3)] 1-index."""
        coords = find_blank_coords(GRID_G1)

        assert coords == [(2, 2), (3, 3)]
