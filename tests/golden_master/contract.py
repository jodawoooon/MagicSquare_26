"""Golden Master output contract assertions (GM-2)."""

import copy

from entity.constants import GRID_SIZE, MAGIC_CONSTANT
from entity.services.blank_locator import find_blank_coords
from entity.services.magic_square_validator import is_magic_square
from entity.services.missing_numbers import find_not_exist_nums

_COORD_MIN = 1
_COORD_MAX = GRID_SIZE
_SOLUTION_LENGTH = 6


def assert_int_six_format(solution: list[int]) -> None:
    """Verify success output is int[6] with numeric elements."""
    assert len(solution) == _SOLUTION_LENGTH, (
        f"expected int[6], got length {len(solution)}: {solution}"
    )
    assert all(isinstance(value, int) for value in solution), (
        f"all solution elements must be int: {solution}"
    )


def assert_one_index_coordinates(solution: list[int]) -> None:
    """Verify r1,c1,r2,c2 are 1-indexed coordinates in 1..4."""
    row_one, col_one, _, row_two, col_two, _ = solution
    for label, coord in (
        ("r1", row_one),
        ("c1", col_one),
        ("r2", row_two),
        ("c2", col_two),
    ):
        assert _COORD_MIN <= coord <= _COORD_MAX, (
            f"{label} must be 1-index in [{_COORD_MIN},{_COORD_MAX}], got {coord}"
        )


def assert_row_major_blank_assignment(grid: list[list[int]], solution: list[int]) -> None:
    """Verify solution coordinates follow row-major blank order."""
    (blank_one, blank_two) = find_blank_coords(grid)
    row_one, col_one, _, row_two, col_two, _ = solution
    assert (row_one, col_one) == blank_one, (
        f"first assignment must target row-major first blank {blank_one}, "
        f"got ({row_one},{col_one})"
    )
    assert (row_two, col_two) == blank_two, (
        f"second assignment must target row-major second blank {blank_two}, "
        f"got ({row_two},{col_two})"
    )


def assert_small_first_combination(grid: list[list[int]], solution: list[int]) -> None:
    """Verify small number maps to first blank and large to second."""
    small, large = find_not_exist_nums(grid)
    _, _, number_one, _, _, number_two = solution
    assert (number_one, number_two) == (small, large), (
        f"expected small-first ({small},{large}), got ({number_one},{number_two})"
    )


def assert_reverse_fallback_combination(grid: list[list[int]], solution: list[int]) -> None:
    """Verify reverse combination (large first blank, small second blank)."""
    small, large = find_not_exist_nums(grid)
    _, _, number_one, _, _, number_two = solution
    assert (number_one, number_two) == (large, small), (
        f"expected reverse ({large},{small}), got ({number_one},{number_two})"
    )

    (row_one, col_one), (row_two, col_two) = find_blank_coords(grid)
    small_first_candidate = copy.deepcopy(grid)
    small_first_candidate[row_one - 1][col_one - 1] = small
    small_first_candidate[row_two - 1][col_two - 1] = large
    assert not is_magic_square(small_first_candidate), (
        "small-first must fail before reverse succeeds"
    )


def assert_completed_magic_square(grid: list[list[int]], solution: list[int]) -> None:
    """Verify the filled candidate satisfies magic square rules."""
    row_one, col_one, number_one, row_two, col_two, number_two = solution
    candidate = copy.deepcopy(grid)
    candidate[row_one - 1][col_one - 1] = number_one
    candidate[row_two - 1][col_two - 1] = number_two
    assert is_magic_square(candidate), (
        f"filled grid is not a magic square (M={MAGIC_CONSTANT})"
    )


def assert_success_contract(
    grid: list[list[int]],
    solution: list[int],
    *,
    expect_small_first: bool,
) -> None:
    """Run all success-path Golden Master contract checks."""
    assert_int_six_format(solution)
    assert_one_index_coordinates(solution)
    assert_row_major_blank_assignment(grid, solution)
    if expect_small_first:
        assert_small_first_combination(grid, solution)
    else:
        assert_reverse_fallback_combination(grid, solution)
    assert_completed_magic_square(grid, solution)


def assert_error_contract(error_code: str, expected_code: str) -> None:
    """Verify standard error code contract."""
    assert error_code == expected_code, (
        f"expected error code {expected_code!r}, got {error_code!r}"
    )
