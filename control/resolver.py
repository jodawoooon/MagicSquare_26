"""Magic square resolution orchestration."""

from dataclasses import dataclass

from entity.solver import MagicSquareSolver

_INVALID_SIZE_CODE = "INVALID_SIZE"
_INVALID_SIZE_MESSAGE = "Grid must be 4x4."


@dataclass
class ResolveError:
    """Size validation failure returned without calling the domain solver."""

    code: str
    message: str


class MagicSquareResolver:
    """Orchestrates size checks and domain resolution."""

    def __init__(self, solver: MagicSquareSolver) -> None:
        self._solver = solver

    def resolve(
        self, grid: list[list[int]] | None
    ) -> ResolveError | list[int]:
        """Validate size and delegate to the domain solver when the grid is 4x4.

        Args:
            grid: Puzzle matrix or None.

        Returns:
            ResolveError when size validation fails; solver result when valid.
        """
        if grid is None or _has_invalid_size(grid):
            return ResolveError(
                code=_INVALID_SIZE_CODE,
                message=_INVALID_SIZE_MESSAGE,
            )
        return self._solver.resolve(grid)


def _has_invalid_size(grid: list[list[int]]) -> bool:
    if len(grid) != 4:
        return True
    return any(len(row) != 4 for row in grid)
