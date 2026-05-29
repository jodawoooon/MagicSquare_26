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
        """Return INVALID_SIZE for null grid without calling the domain solver.

        Args:
            grid: Puzzle matrix or None.

        Returns:
            ResolveError when grid is None; solver result otherwise.
        """
        if grid is None:
            return ResolveError(
                code=_INVALID_SIZE_CODE,
                message=_INVALID_SIZE_MESSAGE,
            )
        return self._solver.resolve(grid)
