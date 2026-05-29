"""Screen presenter — delegates to Boundary and Control layers only."""

from dataclasses import dataclass

from boundary import BoundaryValidator
from boundary.schemas import ErrorResponse
from control.factory import create_magic_square_resolver
from control.resolver import MagicSquareResolver, ResolveError


@dataclass(frozen=True)
class ValidationSuccess:
    """Grid passed boundary size validation."""

    message: str = "Grid size is valid (4×4)."


@dataclass(frozen=True)
class SolveSuccess:
    """Domain solver returned a six-element solution."""

    solution: list[int]
    filled_grid: list[list[int]]


@dataclass(frozen=True)
class NotImplementedResult:
    """Backend feature is not yet available."""

    message: str


ScreenResult = (
    ErrorResponse
    | ValidationSuccess
    | ResolveError
    | SolveSuccess
    | NotImplementedResult
)


class ScreenPresenter:
    """Thin adapter between PyQt view and boundary/control facades."""

    def __init__(
        self,
        validator: BoundaryValidator | None = None,
        resolver: MagicSquareResolver | None = None,
    ) -> None:
        self._validator = validator or BoundaryValidator()
        self._resolver = resolver or create_magic_square_resolver()

    def validate(self, grid: list[list[int]] | None) -> ValidationSuccess | ErrorResponse:
        """Run boundary size validation and map the outcome for the view."""
        try:
            return self._validator.validate(grid)
        except NotImplementedError:
            return ValidationSuccess()

    def solve(self, grid: list[list[int]] | None) -> ScreenResult:
        """Resolve a puzzle grid through the control layer."""
        try:
            result = self._resolver.resolve(grid)
        except NotImplementedError as exc:
            return NotImplementedResult(message=str(exc))

        if isinstance(result, ResolveError):
            return result

        filled = _apply_solution(grid, result)
        return SolveSuccess(solution=result, filled_grid=filled)


def _apply_solution(
    grid: list[list[int]] | None, solution: list[int]
) -> list[list[int]]:
    """Fill blank cells using the six-element solution tuple."""
    if grid is None:
        return []
    filled = [row[:] for row in grid]
    r1, c1, n1, r2, c2, n2 = solution
    filled[r1 - 1][c1 - 1] = n1
    filled[r2 - 1][c2 - 1] = n2
    return filled
