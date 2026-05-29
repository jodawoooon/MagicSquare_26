"""Factory helpers for Control-layer use cases."""

from control.resolver import MagicSquareResolver
from entity.solver import MagicSquareSolver


def create_magic_square_resolver() -> MagicSquareResolver:
    """Return a resolver wired with the default domain solver."""
    return MagicSquareResolver(solver=MagicSquareSolver())
