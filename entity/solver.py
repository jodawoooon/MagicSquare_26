"""Domain solver entry point (FR-05)."""

import copy

from entity.exceptions import UnsolvableDomainError
from entity.services.blank_locator import find_blank_coords
from entity.services.magic_square_validator import is_magic_square
from entity.services.missing_numbers import find_not_exist_nums


class MagicSquareSolver:
    """Resolves a valid partial magic square grid."""

    def resolve(self, grid: list[list[int]]) -> list[int]:
        """Return solution coordinates for a valid grid.

        Args:
            grid: Valid 4x4 partial magic square.

        Returns:
            Six-int solution ``[r1,c1,n1,r2,c2,n2]`` with 1-indexed coordinates.

        Raises:
            UnsolvableDomainError: When neither assignment combination works.
        """
        (row_one, col_one), (row_two, col_two) = find_blank_coords(grid)
        small, large = find_not_exist_nums(grid)

        small_first = self._attempt_assignment(
            grid,
            row_one,
            col_one,
            small,
            row_two,
            col_two,
            large,
        )
        if small_first is not None:
            return small_first

        reverse_order = self._attempt_assignment(
            grid,
            row_one,
            col_one,
            large,
            row_two,
            col_two,
            small,
        )
        if reverse_order is not None:
            return reverse_order

        raise UnsolvableDomainError("Neither assignment combination is valid.")

    def _attempt_assignment(
        self,
        grid: list[list[int]],
        row_one: int,
        col_one: int,
        value_one: int,
        row_two: int,
        col_two: int,
        value_two: int,
    ) -> list[int] | None:
        candidate = copy.deepcopy(grid)
        candidate[row_one - 1][col_one - 1] = value_one
        candidate[row_two - 1][col_two - 1] = value_two
        if not is_magic_square(candidate):
            return None
        return [row_one, col_one, value_one, row_two, col_two, value_two]
