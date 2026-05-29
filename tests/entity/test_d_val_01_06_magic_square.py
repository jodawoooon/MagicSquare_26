"""Track B — D-VAL-01~06: is_magic_square decomposition (FR-04).

Domain Mock 금지. SSOT: Report/06 §8, Invariants I1~I5.
"""

import copy

from entity.services.magic_square_validator import is_magic_square
from tests.entity.grids import GRID_G0


class TestDVal01CompleteGridG0:
    """D-VAL-01 — G0 complete grid returns True."""

    def test_d_val_01_is_magic_square_g0_complete_grid_returns_true(self) -> None:
        """D-VAL-01, AC-FR04-01 — G0 완성 격자 True."""
        assert is_magic_square(GRID_G0) is True


class TestDVal02RowSumMismatch:
    """D-VAL-02 — row sum mismatch returns False."""

    def test_d_val_02_is_magic_square_row_sum_mismatch_returns_false(self) -> None:
        """D-VAL-02, I1 — G0[0][0]=15 시 행 합 불일치 False."""
        matrix = copy.deepcopy(GRID_G0)
        matrix[0][0] = 15

        assert is_magic_square(matrix) is False


class TestDVal03ColSumMismatch:
    """D-VAL-03 — column sum mismatch returns False."""

    def test_d_val_03_is_magic_square_col_sum_mismatch_returns_false(self) -> None:
        """D-VAL-03, I2 — G0 1열 합 깨짐 시 False."""
        matrix = copy.deepcopy(GRID_G0)
        matrix[0][0] = 1
        matrix[1][0] = 1
        matrix[2][0] = 1
        matrix[3][0] = 1

        assert is_magic_square(matrix) is False


class TestDVal04DiagonalMismatch:
    """D-VAL-04 — diagonal mismatch returns False."""

    def test_d_val_04_is_magic_square_diagonal_mismatch_returns_false(self) -> None:
        """D-VAL-04, I3 — 대각선 불일치 시 False."""
        matrix = copy.deepcopy(GRID_G0)
        matrix[0][0] = 1

        assert is_magic_square(matrix) is False


class TestDVal05DuplicateOrOutOfSet:
    """D-VAL-05 — duplicate or out-of-set returns False."""

    def test_d_val_05_is_magic_square_duplicate_returns_false(self) -> None:
        """D-VAL-05, I4 — G0 중복 8 시 False."""
        matrix = copy.deepcopy(GRID_G0)
        matrix[0][1] = 8
        matrix[0][2] = 8

        assert is_magic_square(matrix) is False


class TestDVal06CompleteGridWithZero:
    """D-VAL-06 — complete grid with zero returns False."""

    def test_d_val_06_is_magic_square_complete_grid_with_zero_returns_false(self) -> None:
        """D-VAL-06, I4 — G0에 0 존재 시 완성 격자 위반 False."""
        matrix = copy.deepcopy(GRID_G0)
        matrix[2][2] = 0

        assert is_magic_square(matrix) is False
