"""Control resolver happy path — valid grid delegates to domain solver."""

from control.resolver import MagicSquareResolver
from entity.solver import MagicSquareSolver
from tests.entity.grids import D_SOL_01_EXPECTED, GRID_G1_SOL


def test_valid_grid_resolve_returns_solver_result() -> None:
    """Non-null valid grid → domain solver int[6] (AC-FR01-05 complement)."""
    resolver = MagicSquareResolver(solver=MagicSquareSolver())

    result = resolver.resolve(GRID_G1_SOL)

    assert result == D_SOL_01_EXPECTED
