"""End-to-end solve orchestration at the Boundary layer (FR-01, FR-05)."""

from dataclasses import dataclass
from typing import Literal

from boundary.constants import INVALID_SIZE_CODE
from boundary.input_validator import InputValidator
from boundary.schemas import ErrorResponse
from boundary.validator import BoundaryValidator
from control.exceptions import NoValidAssignmentError
from control.solve_partial import SolvePartialMagicSquare

_NO_VALID_ASSIGNMENT_CODE = "NO_VALID_ASSIGNMENT"


@dataclass(frozen=True)
class SolveOutcome:
    """Serialized solve result for Golden Master capture."""

    kind: Literal["success", "error"]
    solution: list[int] | None = None
    error_code: str | None = None


class MagicSquarePipeline:
    """Orchestrates boundary validation and control solve execution."""

    def __init__(
        self,
        size_validator: BoundaryValidator | None = None,
        input_validator: InputValidator | None = None,
        solve_partial: SolvePartialMagicSquare | None = None,
    ) -> None:
        self._size_validator = size_validator or BoundaryValidator()
        self._input_validator = input_validator or InputValidator()
        self._solve_partial = solve_partial or SolvePartialMagicSquare()

    def solve(self, grid: list[list[int]]) -> SolveOutcome:
        """Run the full solve flow and return a capture-friendly outcome.

        Args:
            grid: 4x4 puzzle matrix.

        Returns:
            Success outcome with int[6] solution or error outcome with code.
        """
        size_error = self._try_size_validation(grid)
        if size_error is not None:
            return SolveOutcome(kind="error", error_code=size_error.code)

        input_error = self._input_validator.validate(grid)
        if input_error is not None:
            return SolveOutcome(kind="error", error_code=input_error.code)

        try:
            solution = self._solve_partial.execute(grid)
        except NoValidAssignmentError:
            return SolveOutcome(kind="error", error_code=_NO_VALID_ASSIGNMENT_CODE)

        return SolveOutcome(kind="success", solution=solution)

    def _try_size_validation(self, grid: list[list[int]]) -> ErrorResponse | None:
        try:
            return self._size_validator.validate(grid)
        except NotImplementedError:
            return None
