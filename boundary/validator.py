"""FR-01 matrix size validation at the Boundary layer."""

from boundary.constants import (
    GRID_SIZE,
    INVALID_SIZE_CODE,
    INVALID_SIZE_MESSAGE,
)
from boundary.schemas import ErrorResponse


class BoundaryValidator:
    """Validates 4x4 grid dimensions before Control/Entity processing."""

    def validate(self, grid: list[list[int]] | None) -> ErrorResponse:
        """Return INVALID_SIZE when the grid is not 4x4.

        Args:
            grid: Puzzle matrix or None when input is missing.

        Returns:
            ErrorResponse with INVALID_SIZE when size rules are violated.

        Raises:
            NotImplementedError: When the grid passes size checks (out of scope).
        """
        if grid is None or self._has_invalid_size(grid):
            return ErrorResponse(
                code=INVALID_SIZE_CODE,
                message=INVALID_SIZE_MESSAGE,
            )
        raise NotImplementedError("Valid 4x4 grid is out of AC-FR-01-01 scope.")

    def _has_invalid_size(self, grid: list[list[int]]) -> bool:
        if len(grid) != GRID_SIZE:
            return True
        return any(len(row) != GRID_SIZE for row in grid)
