"""Control factory wiring smoke test."""

from control.factory import create_magic_square_resolver
from control.resolver import MagicSquareResolver
from tests.boundary.constants import INVALID_SIZE_CODE


def test_create_magic_square_resolver_returns_wired_resolver() -> None:
    """Factory returns a resolver that enforces size guard before domain entry."""
    resolver = create_magic_square_resolver()

    assert isinstance(resolver, MagicSquareResolver)
    result = resolver.resolve(None)
    assert result.code == INVALID_SIZE_CODE
