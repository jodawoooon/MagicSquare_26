"""UI boundary facade — validate/solve envelope contract (FR-01, FR-05)."""

from boundary.input_validator import InputValidator
from boundary.schemas import ErrorResponse
from boundary.validator import BoundaryValidator
from control.solve_partial import SolvePartialMagicSquare


class UIBoundary:
    """Single entry point for UI and integration solve flows."""

    def __init__(
        self,
        size_validator: BoundaryValidator | None = None,
        input_validator: InputValidator | None = None,
        solve_partial: SolvePartialMagicSquare | None = None,
    ) -> None:
        self._size_validator = size_validator or BoundaryValidator()
        self._input_validator = input_validator or InputValidator()
        self._solve_partial = solve_partial or SolvePartialMagicSquare()

    def validate(self, grid: list[list[int]] | None) -> ErrorResponse | None:
        """Run size and input contract validation.

        Args:
            grid: Puzzle matrix or None.

        Returns:
            ErrorResponse when validation fails; None when input is valid.

        Raises:
            NotImplementedError: When validation envelope contract is not wired.
        """
        raise NotImplementedError("UIBoundary.validate is not implemented yet.")

    def solve(self, grid: list[list[int]] | None) -> object:
        """Validate and solve, returning a success or failure envelope.

        Args:
            grid: Puzzle matrix or None.

        Returns:
            Envelope DTO with success flag and data or error fields.

        Raises:
            NotImplementedError: When solve envelope contract is not wired.
        """
        raise NotImplementedError("UIBoundary.solve is not implemented yet.")
