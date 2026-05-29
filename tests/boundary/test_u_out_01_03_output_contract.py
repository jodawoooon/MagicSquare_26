"""Track A — FR-05 output contract RED skeletons (U-OUT-01~03).

Mock policy: execute stub only (Control mock/spy). Domain mock 금지.
SSOT: Report/06 §7, docs/PRD_MagicSquare.md v0.2 (AC-FR05-04).
"""

import pytest

from boundary.ui_boundary import UIBoundary


class TestUOut01SuccessArrayLength:
    """U-OUT-01 — G1 solve returns success envelope with int[6]."""

    def test_u_out_01_solve_valid_g1_returns_success_array_length_six(self) -> None:
        """U-OUT-01, AC-FR05-04 — G1 성공 시 len(data)==6."""
        # Given
        # matrix = G1
        # ui = UIBoundary()
        # # Control mock: SolvePartialMagicSquare.execute stub → [2,2,7,3,3,10]

        # When
        # result = ui.solve(matrix)

        # Then — success==true; len(data)==6; array match (GREEN)
        pytest.fail("RED: U-OUT-01 — G1 성공 시 success envelope 및 int[6] 반환")


class TestUOut02OneIndexedCoordinates:
    """U-OUT-02 — success coordinates are 1-indexed in 1..4."""

    def test_u_out_02_solve_success_coordinates_one_indexed_in_1_to_4(self) -> None:
        """U-OUT-02, AC-FR05-04 — r,c 좌표 1-index, 범위 1~4."""
        # Given
        # matrix = G1
        # ui = UIBoundary()
        # # Control mock: execute stub → [2,2,7,3,3,10]

        # When
        # result = ui.solve(matrix)

        # Then — r,c ∈ {1..4} (GREEN)
        pytest.fail("RED: U-OUT-02 — 성공 좌표 1-index 및 1~4 범위")


class TestUOut03UnsolvableEnvelope:
    """U-OUT-03 — G3 unsolvable returns failure envelope (no Python exception)."""

    def test_u_out_03_solve_g3_unsolvable_returns_failure_envelope(self) -> None:
        """U-OUT-03, AC-FR05-03 — G3 양 조합 실패 시 표준 failure envelope."""
        # Given
        # matrix = G3  # placeholder until G3 confirmed
        # ui = UIBoundary()
        # # Control: real solution path; Domain Mock 금지

        # When
        # result = ui.solve(matrix)

        # Then — success==false; NO_VALID_ASSIGNMENT or mapped code (GREEN)
        pytest.fail("RED: U-OUT-03 — G3 불가 시 failure envelope 반환(예외 아님)")
