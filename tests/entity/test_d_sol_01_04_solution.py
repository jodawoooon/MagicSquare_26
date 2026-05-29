"""Track B — D-SOL-01~04: two-combination solution (FR-05).

Domain Mock 금지. SSOT: Report/06 §8.
"""

import pytest

from control.solver import solution
from entity.exceptions import UnsolvableDomainError


class TestDSol01G1SmallFirst:
    """D-SOL-01 — G1 Step A small-first success."""

    def test_d_sol_01_solution_g1_step_a_small_first_returns_expected_six_tuple(self) -> None:
        """D-SOL-01, AC-FR05-01 — G1 → [2,2,7,3,3,10]."""
        # Given
        # matrix = G1

        # When
        # result = solution(matrix)

        # Then
        pytest.fail("RED: D-SOL-01 — G1 small-first [2,2,7,3,3,10]")


class TestDSol02G2Reverse:
    """D-SOL-02 — G2 Step A fails, Step B succeeds."""

    def test_d_sol_02_solution_g2_step_a_fails_step_b_succeeds(self) -> None:
        """D-SOL-02, AC-FR05-02 — G2 reverse → [3,2,7,3,3,6]."""
        pytest.fail("RED: D-SOL-02 — G2 TBD")


class TestDSol03G3Unsolvable:
    """D-SOL-03 — G3 both steps fail → UnsolvableDomainError."""

    def test_d_sol_03_solution_g3_both_steps_fail_raises_unsolvable_domain_error(self) -> None:
        """D-SOL-03, AC-FR05-03 — G3 placeholder → UnsolvableDomainError."""
        # Given
        # matrix = G3  # placeholder

        # When / Then — pytest.raises(UnsolvableDomainError) (GREEN)
        pytest.fail("RED: D-SOL-03 — G3 양 조합 실패 시 UnsolvableDomainError")


class TestDSol04OutputShape:
    """D-SOL-04 — success output length 6 and 1-index coords."""

    def test_d_sol_04_solution_success_output_length_six_and_one_index_coords(self) -> None:
        """D-SOL-04, AC-FR05-04 — len=6; coords ∈ [1,4]."""
        # Given
        # matrix = G1 or G2

        # When
        # result = solution(matrix)

        # Then
        pytest.fail("RED: D-SOL-04 — 성공 결과 len=6, 좌표 1-index 1~4")
