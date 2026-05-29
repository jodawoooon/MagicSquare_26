"""Magic square validation (FR-04)."""

from entity.constants import (
    BLANK_VALUE,
    GRID_SIZE,
    MAGIC_CONSTANT,
    MAX_CELL_VALUE,
    MIN_CELL_VALUE,
)


def is_magic_square(grid: list[list[int]]) -> bool:
    """Return True when the grid satisfies 4x4 magic square rules.

    Args:
        grid: Completed 4x4 candidate grid.

    Returns:
        True when all rows, columns, diagonals sum to the magic constant
        and the value set is exactly {1..16} with no blanks.
    """
    if any(BLANK_VALUE in row for row in grid):
        return False

    expected_values = set(range(MIN_CELL_VALUE, MAX_CELL_VALUE + 1))
    actual_values = [grid[row][col] for row in range(GRID_SIZE) for col in range(GRID_SIZE)]
    if set(actual_values) != expected_values:
        return False

    for row in grid:
        if sum(row) != MAGIC_CONSTANT:
            return False

    for col in range(GRID_SIZE):
        if sum(grid[row][col] for row in range(GRID_SIZE)) != MAGIC_CONSTANT:
            return False

    if sum(grid[index][index] for index in range(GRID_SIZE)) != MAGIC_CONSTANT:
        return False

    if sum(grid[index][GRID_SIZE - 1 - index] for index in range(GRID_SIZE)) != MAGIC_CONSTANT:
        return False

    return True
