"""Track B — D-SOL-01~04: two-combination solution (FR-05).

Domain Mock 금지. SSOT: Report/06 §8, Golden Master GM-TC-01/02/05.
"""

import pytest

from entity.exceptions import UnsolvableDomainError
from entity.solver import solution
from tests.entity.grids import (
    D_SOL_01_EXPECTED,
    D_SOL_02_EXPECTED,
    GRID_G1_SOL,
    GRID_G2,
    GRID_G3,
)


class TestDSol01G1SmallFirst:
    """D-SOL-01 — G1_SOL Step A small-first success."""

    def test_d_sol_01_solution_g1_step_a_small_first_returns_expected_six_tuple(self) -> None:
        """D-SOL-01, AC-FR05-01 — GM-TC-01 small-first → [1,2,2,1,3,3]."""
        result = solution(GRID_G1_SOL)

        assert result == D_SOL_01_EXPECTED


class TestDSol02G2Reverse:
    """D-SOL-02 — G2 Step A fails, Step B succeeds."""

    def test_d_sol_02_solution_g2_step_a_fails_step_b_succeeds(self) -> None:
        """D-SOL-02, AC-FR05-02 — G2 reverse → [3,2,7,3,3,6]."""
        result = solution(GRID_G2)

        assert result == D_SOL_02_EXPECTED


class TestDSol03G3Unsolvable:
    """D-SOL-03 — G3 both steps fail → UnsolvableDomainError."""

    def test_d_sol_03_solution_g3_both_steps_fail_raises_unsolvable_domain_error(self) -> None:
        """D-SOL-03, AC-FR05-03 — G3 → UnsolvableDomainError."""
        with pytest.raises(UnsolvableDomainError):
            solution(GRID_G3)


class TestDSol04OutputShape:
    """D-SOL-04 — success output length 6 and 1-index coords."""

    def test_d_sol_04_solution_success_output_length_six_and_one_index_coords(self) -> None:
        """D-SOL-04, AC-FR05-04 — len=6; coords ∈ [1,4]."""
        result = solution(GRID_G1_SOL)

        assert len(result) == 6
        row_one, col_one, _, row_two, col_two, _ = result
        for coord in (row_one, col_one, row_two, col_two):
            assert 1 <= coord <= 4
