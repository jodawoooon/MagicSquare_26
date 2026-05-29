"""Partial magic square solve use case (FR-05)."""

from control.exceptions import NoValidAssignmentError
from entity.exceptions import UnsolvableDomainError
from entity.solver import MagicSquareSolver


class SolvePartialMagicSquare:
    """Orchestrates locate→find→solve for validated 4×4 grids."""

    def __init__(self, solver: MagicSquareSolver | None = None) -> None:
        self._solver = solver or MagicSquareSolver()

    def execute(self, grid: list[list[int]]) -> list[int]:
        """Return int[6] solution for a grid that passed input validation.

        Args:
            grid: Validated 4×4 partial magic square matrix.

        Returns:
            Six-int solution ``[r1,c1,n1,r2,c2,n2]`` with 1-indexed coordinates.

        Raises:
            NoValidAssignmentError: When neither assignment combination works.
        """
        try:
            return self._solver.resolve(grid)
        except UnsolvableDomainError as exc:
            raise NoValidAssignmentError(str(exc)) from exc
