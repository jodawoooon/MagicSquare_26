"""Track A — FR-05 output contract (U-OUT-01~03).

Mock policy: U-OUT-01~02 execute stub only; U-OUT-03 real path. Domain mock 금지.
SSOT: Report/06 §7, docs/PRD_MagicSquare.md v0.2 (AC-FR05-04).
"""

from unittest.mock import MagicMock

from boundary.pipeline import SolveOutcome
from boundary.ui_boundary import UIBoundary
from tests.entity.grids import D_SOL_01_EXPECTED, GRID_G1, GRID_G3


class TestUOut01SuccessArrayLength:
    """U-OUT-01 — G1 solve returns success outcome with int[6]."""

    def test_u_out_01_solve_valid_g1_returns_success_array_length_six(self) -> None:
        """U-OUT-01, AC-FR05-04 — G1 성공 시 len(solution)==6."""
        ui = UIBoundary()
        ui._pipeline._solve_partial.execute = MagicMock(return_value=D_SOL_01_EXPECTED)

        result = ui.solve(GRID_G1)

        assert isinstance(result, SolveOutcome)
        assert result.kind == "success"
        assert result.solution is not None
        assert len(result.solution) == 6
        assert result.solution == D_SOL_01_EXPECTED


class TestUOut02OneIndexedCoordinates:
    """U-OUT-02 — success coordinates are 1-indexed in 1..4."""

    def test_u_out_02_solve_success_coordinates_one_indexed_in_1_to_4(self) -> None:
        """U-OUT-02, AC-FR05-04 — r,c 좌표 1-index, 범위 1~4."""
        ui = UIBoundary()
        ui._pipeline._solve_partial.execute = MagicMock(return_value=D_SOL_01_EXPECTED)

        result = ui.solve(GRID_G1)

        assert isinstance(result, SolveOutcome)
        assert result.solution is not None
        row_one, col_one, _, row_two, col_two, _ = result.solution
        for coord in (row_one, col_one, row_two, col_two):
            assert 1 <= coord <= 4


class TestUOut03UnsolvableEnvelope:
    """U-OUT-03 — G3 unsolvable returns failure outcome (no Python exception)."""

    def test_u_out_03_solve_g3_unsolvable_returns_failure_envelope(self) -> None:
        """U-OUT-03, AC-FR05-03 — G3 양 조합 실패 시 NO_VALID_ASSIGNMENT outcome."""
        ui = UIBoundary()

        result = ui.solve(GRID_G3)

        assert isinstance(result, SolveOutcome)
        assert result.kind == "error"
        assert result.error_code == "NO_VALID_ASSIGNMENT"
