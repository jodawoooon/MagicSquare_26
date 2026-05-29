"""Partial magic square solve use case (FR-05)."""

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
        """
        return self._solver.resolve(grid)
