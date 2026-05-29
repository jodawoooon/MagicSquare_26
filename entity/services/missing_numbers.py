"""Missing number discovery (FR-03)."""

from entity.constants import BLANK_VALUE, GRID_SIZE, MAX_CELL_VALUE, MIN_CELL_VALUE


def find_not_exist_nums(grid: list[list[int]]) -> tuple[int, int]:
    """Return the two missing numbers in ascending order.

    Args:
        grid: Validated 4x4 partial grid.

    Returns:
        Tuple (small, large) of missing values from 1..16.
    """
    present = {
        grid[row][col]
        for row in range(GRID_SIZE)
        for col in range(GRID_SIZE)
        if grid[row][col] != BLANK_VALUE
    }
    missing = [
        value
        for value in range(MIN_CELL_VALUE, MAX_CELL_VALUE + 1)
        if value not in present
    ]
    if len(missing) != 2:
        msg = f"expected 2 missing numbers, found {len(missing)}"
        raise ValueError(msg)
    return missing[0], missing[1]
