"""Screen presenter — delegates to UIBoundary only (no direct Control imports)."""

from dataclasses import dataclass

from boundary.error_messages import message_for_code
from boundary.pipeline import SolveOutcome
from boundary.schemas import ErrorResponse
from boundary.ui_boundary import UIBoundary


@dataclass(frozen=True)
class ValidationSuccess:
    """Grid passed boundary size validation."""

    message: str = "Grid size is valid (4×4)."


@dataclass(frozen=True)
class SolveSuccess:
    """Domain solver returned a six-element solution."""

    solution: list[int]
    filled_grid: list[list[int]]


ScreenResult = ErrorResponse | ValidationSuccess | SolveSuccess


class ScreenPresenter:
    """Thin adapter between PyQt view and UIBoundary."""

    def __init__(self, ui_boundary: UIBoundary | None = None) -> None:
        self._ui = ui_boundary or UIBoundary()

    def validate(self, grid: list[list[int]] | None) -> ValidationSuccess | ErrorResponse:
        """Run boundary size validation and map the outcome for the view."""
        error = self._ui.validate(grid)
        if error is not None:
            return error
        return ValidationSuccess()

    def solve(self, grid: list[list[int]] | None) -> ScreenResult:
        """Resolve a puzzle grid through UIBoundary."""
        result = self._ui.solve(grid)
        if isinstance(result, ErrorResponse):
            return result
        return _map_solve_outcome(grid, result)


def _map_solve_outcome(
    grid: list[list[int]] | None, outcome: SolveOutcome
) -> ScreenResult:
    if outcome.kind == "success":
        if outcome.solution is None:
            msg = "success outcome requires solution"
            raise ValueError(msg)
        filled = _apply_solution(grid, outcome.solution)
        return SolveSuccess(solution=outcome.solution, filled_grid=filled)

    code = outcome.error_code or "UNKNOWN_ERROR"
    return ErrorResponse(code=code, message=message_for_code(code))


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
