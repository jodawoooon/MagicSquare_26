"""Control layer — use-case orchestration."""

from control.factory import create_magic_square_resolver
from control.resolver import MagicSquareResolver, ResolveError

__all__ = ["MagicSquareResolver", "ResolveError", "create_magic_square_resolver"]
