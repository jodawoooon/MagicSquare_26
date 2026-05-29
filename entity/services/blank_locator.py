"""Row-major blank coordinate discovery (FR-02)."""

from entity.constants import BLANK_VALUE, EXPECTED_BLANK_COUNT, GRID_SIZE


def find_blank_coords(grid: list[list[int]]) -> list[tuple[int, int]]:
    """Return 1-indexed blank coordinates in row-major order.

    Args:
        grid: Validated 4x4 grid with exactly two blank cells.

    Returns:
        Two (row, col) tuples in 1-indexed coordinates.
    """
    coords: list[tuple[int, int]] = []
    for row_index in range(GRID_SIZE):
        for col_index in range(GRID_SIZE):
            if grid[row_index][col_index] == BLANK_VALUE:
                coords.append((row_index + 1, col_index + 1))
    if len(coords) != EXPECTED_BLANK_COUNT:
        msg = f"expected {EXPECTED_BLANK_COUNT} blanks, found {len(coords)}"
        raise ValueError(msg)
    return coords
